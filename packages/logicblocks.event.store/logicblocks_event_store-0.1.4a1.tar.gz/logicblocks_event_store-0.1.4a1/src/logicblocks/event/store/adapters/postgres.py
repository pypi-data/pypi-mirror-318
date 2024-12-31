from collections.abc import AsyncIterator, Set
from dataclasses import dataclass
from functools import singledispatch
from typing import Any, Sequence, Tuple
from uuid import uuid4

from psycopg import AsyncConnection, AsyncCursor, abc, sql
from psycopg.rows import class_row
from psycopg.types.json import Jsonb
from psycopg_pool import AsyncConnectionPool

from logicblocks.event.store.adapters import StorageAdapter
from logicblocks.event.store.adapters.base import Saveable, Scannable
from logicblocks.event.store.conditions import WriteCondition
from logicblocks.event.types import (
    NewEvent,
    StoredEvent,
    identifier,
)


@dataclass(frozen=True)
class ConnectionParameters(object):
    host: str
    port: int
    dbname: str
    user: str
    password: str

    def __init__(
        self, *, host: str, port: int, dbname: str, user: str, password: str
    ):
        object.__setattr__(self, "host", host)
        object.__setattr__(self, "port", port)
        object.__setattr__(self, "dbname", dbname)
        object.__setattr__(self, "user", user)
        object.__setattr__(self, "password", password)

    def __repr__(self):
        return (
            f"ConnectionParameters("
            f"host={self.host}, "
            f"port={self.port}, "
            f"dbname={self.dbname}, "
            f"user={self.user}, "
            f"password={"*" * len(self.password)})"
        )

    def to_connection_string(self) -> str:
        userspec = f"{self.user}:{self.password}"
        hostspec = f"{self.host}:{self.port}"
        return f"postgresql://{userspec}@{hostspec}/{self.dbname}"


ConnectionSource = ConnectionParameters | AsyncConnectionPool[AsyncConnection]


@dataclass(frozen=True)
class TableParameters(object):
    events_table_name: str

    def __init__(self, *, events_table_name: str = "events"):
        object.__setattr__(self, "events_table_name", events_table_name)


ParameterisedQuery = Tuple[abc.Query, Sequence[Any]]


@singledispatch
def scan_query(
    target: Scannable, table_parameters: TableParameters
) -> ParameterisedQuery:
    raise TypeError(f"No scan query for target: {target}")


@scan_query.register(identifier.Log)
def scan_query_log(
    _target: identifier.Log, table_parameters: TableParameters
) -> ParameterisedQuery:
    return (
        sql.SQL(
            """
            SELECT * 
            FROM {0}
            ORDER BY sequence_number;
            """
        ).format(sql.Identifier(table_parameters.events_table_name)),
        [],
    )


@scan_query.register(identifier.Category)
def scan_query_category(
    target: identifier.Category, table_parameters: TableParameters
) -> ParameterisedQuery:
    return (
        sql.SQL(
            """
            SELECT * 
            FROM {0}
            WHERE category = (%s)
            ORDER BY sequence_number;
            """
        ).format(sql.Identifier(table_parameters.events_table_name)),
        [target.category],
    )


@scan_query.register(identifier.Stream)
def scan_query_stream(
    target: identifier.Stream, table_parameters: TableParameters
) -> ParameterisedQuery:
    return (
        sql.SQL(
            """
            SELECT * 
            FROM {0}
            WHERE category = (%s)
            AND stream = (%s)
            ORDER BY sequence_number;
            """
        ).format(sql.Identifier(table_parameters.events_table_name)),
        [target.category, target.stream],
    )


def lock_query(table_parameters: TableParameters) -> ParameterisedQuery:
    return (
        sql.SQL(
            """
            LOCK TABLE ONLY {0} IN EXCLUSIVE MODE;
            """
        ).format(sql.Identifier(table_parameters.events_table_name)),
        [],
    )


def read_last_query(
    target: identifier.Stream, table_parameters: TableParameters
) -> ParameterisedQuery:
    return (
        sql.SQL(
            """
            SELECT * 
            FROM {0}
            WHERE category = (%s)
            AND stream = (%s)
            ORDER BY position DESC 
            LIMIT 1;
            """
        ).format(sql.Identifier(table_parameters.events_table_name)),
        [target.category, target.stream],
    )


def insert_query(
    target: Saveable,
    event: NewEvent,
    position: int,
    table_parameters: TableParameters,
) -> ParameterisedQuery:
    return (
        sql.SQL(
            """
            INSERT INTO {0} (
              id, 
              name, 
              stream, 
              category, 
              position, 
              payload, 
              observed_at, 
              occurred_at
            )
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
              RETURNING *;
            """
        ).format(sql.Identifier(table_parameters.events_table_name)),
        [
            uuid4().hex,
            event.name,
            target.stream,
            target.category,
            position,
            Jsonb(event.payload),
            event.observed_at,
            event.occurred_at,
        ],
    )


async def lock_table(
    cursor: AsyncCursor[StoredEvent], *, table_parameters: TableParameters
):
    await cursor.execute(*lock_query(table_parameters))


async def read_last(
    cursor: AsyncCursor[StoredEvent],
    *,
    target: identifier.Stream,
    table_parameters: TableParameters,
):
    await cursor.execute(*read_last_query(target, table_parameters))
    return await cursor.fetchone()


async def insert(
    cursor: AsyncCursor[StoredEvent],
    *,
    target: Saveable,
    event: NewEvent,
    position: int,
    table_parameters: TableParameters,
):
    await cursor.execute(
        *insert_query(target, event, position, table_parameters)
    )
    stored_event = await cursor.fetchone()

    if not stored_event:
        raise Exception("Insert failed")

    return stored_event


class PostgresStorageAdapter(StorageAdapter):
    connection_pool: AsyncConnectionPool[AsyncConnection]
    connection_pool_owner: bool
    table_parameters: TableParameters

    def __init__(
        self,
        *,
        connection_source: ConnectionSource,
        table_parameters: TableParameters = TableParameters(),
    ):
        if isinstance(connection_source, ConnectionParameters):
            self.connection_pool_owner = True
            self.connection_pool = AsyncConnectionPool[AsyncConnection](
                connection_source.to_connection_string(), open=False
            )
        else:
            self.connection_pool_owner = False
            self.connection_pool = connection_source

        self.table_parameters = table_parameters

    async def open(self) -> None:
        if self.connection_pool_owner:
            await self.connection_pool.open()

    async def close(self) -> None:
        if self.connection_pool_owner:
            await self.connection_pool.close()

    async def save(
        self,
        *,
        target: Saveable,
        events: Sequence[NewEvent],
        conditions: Set[WriteCondition] = frozenset(),
    ) -> Sequence[StoredEvent]:
        async with self.connection_pool.connection() as connection:
            async with connection.cursor(
                row_factory=class_row(StoredEvent)
            ) as cursor:
                await lock_table(
                    cursor, table_parameters=self.table_parameters
                )

                last_event = await read_last(
                    cursor,
                    target=target,
                    table_parameters=self.table_parameters,
                )

                for condition in conditions:
                    condition.ensure(last_event)

                current_position = last_event.position + 1 if last_event else 0

                return [
                    await insert(
                        cursor,
                        target=target,
                        event=event,
                        position=position,
                        table_parameters=self.table_parameters,
                    )
                    for position, event in enumerate(events, current_position)
                ]

    async def scan(
        self,
        *,
        target: Scannable = identifier.Log(),
    ) -> AsyncIterator[StoredEvent]:
        async with self.connection_pool.connection() as connection:
            async with connection.cursor(
                row_factory=class_row(StoredEvent)
            ) as cursor:
                async for record in await cursor.execute(
                    *scan_query(target, table_parameters=self.table_parameters)
                ):
                    yield record
