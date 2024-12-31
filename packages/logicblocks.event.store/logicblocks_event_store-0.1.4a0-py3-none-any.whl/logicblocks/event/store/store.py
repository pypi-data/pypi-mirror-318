from collections.abc import Sequence, Set

from logicblocks.event.store.adapters import StorageAdapter
from logicblocks.event.store.conditions import WriteCondition
from logicblocks.event.types import NewEvent, StoredEvent, identifier


class EventStream(object):
    """A class for interacting with a specific stream of events.

    Events can be published into the stream using the `publish` method, and
    then entire stream can be read using the `read` method. Streams are also
    iterable, supporting `iter`.

    Attributes:
        adapter: The storage adapter to use for interacting with the stream.
        category: The name of the category of the stream.
        stream: The name of the stream.
    """

    adapter: StorageAdapter
    category: str
    stream: str

    def __init__(self, adapter: StorageAdapter, category: str, stream: str):
        self.adapter = adapter
        self.category = category
        self.stream = stream

    def __iter__(self):
        """Iterate over the events in the stream from position 0 to the end."""
        return self.adapter.scan(
            target=identifier.Stream(
                category=self.category, stream=self.stream
            )
        )

    def publish(
        self,
        *,
        events: Sequence[NewEvent],
        conditions: Set[WriteCondition] = frozenset(),
    ) -> Sequence[StoredEvent]:
        """Publish a sequence of events into the stream."""
        target = identifier.Stream(category=self.category, stream=self.stream)

        return self.adapter.save(
            target=target,
            events=events,
            conditions=conditions,
        )

    def read(self) -> Sequence[StoredEvent]:
        """Read all events from the stream.

        All events will be read into memory so stream iteration should be
        preferred in order to give storage adapters the opportunity to page
        events as they are read from the underlying persistence."""
        return list(iter(self))


class EventCategory(object):
    """A class for interacting with a specific category of events.

    Since a category consists of zero or more streams, the category
    can be narrowed to a specific stream using the `stream` method.

    Events in the category can be read using the `read` method. Categories are
    also iterable, supporting `iter`.

    Attributes:
        adapter: The storage adapter to use for interacting with the category.
        category: the name of the category.
    """

    adapter: StorageAdapter
    category: str

    def __init__(self, adapter: StorageAdapter, category: str):
        self.adapter = adapter
        self.category = category

    def __iter__(self):
        """Iterate over the events in the category."""
        return self.adapter.scan(
            target=identifier.Category(category=self.category)
        )

    def stream(self, *, stream: str) -> EventStream:
        """Get a stream of events in the category.

        Args:
            stream (str): The name of the stream.

        Returns:
            an event store scoped to the specified stream.
        """
        return EventStream(
            adapter=self.adapter, category=self.category, stream=stream
        )

    def read(self) -> Sequence[StoredEvent]:
        """Read all events from the category.

        All events will be read into memory so stream iteration should be
        preferred in order to give storage adapters the opportunity to page
        events as they are read from the underlying persistence."""
        return list(iter(self))


class EventStore(object):
    """The primary interface into the store of events.

    An [`EventStore`][logicblocks.event.store.EventStore] is backed by a
    [`StorageAdapter`][logicblocks.event.store.adapters.StorageAdapter]
    which implements event storage. Typically, events are stored in an immutable
    append only log, the details of which are storage implementation specific.

    The event store is partitioned into _streams_, a sequence of events relating
    to the same "thing", such as an entity, a process or a state machine, and
    _categories_, a logical grouping of streams that share some characteristics.

    For example, a stream might exist for each order in a commerce system, with
    the category of such streams being "orders".

    Streams and categories are each identified by a string name. The combination
    of a category name and a stream name acts as an identifier for a specific
    stream of events.
    """

    adapter: StorageAdapter

    def __init__(self, adapter: StorageAdapter):
        self.adapter = adapter

    def stream(self, *, category: str, stream: str) -> EventStream:
        """Get a stream of events from the store.

        This method alone doesn't result in any IO, it instead returns a scoped
        event store for the stream identified by the category and stream names,
        as part of a fluent interface.

        Categories and streams implicitly exist, i.e., calling this method for a
        category or stream that has never been written to will not result in an
        error.

        Args:
            category (str): The name of the category of the stream.
            stream (str): The name of the stream.

        Returns:
            an event store scoped to the specified stream.
        """
        return EventStream(
            adapter=self.adapter, category=category, stream=stream
        )

    def category(self, *, category: str) -> EventCategory:
        """Get a category of events from the store.

        This method alone doesn't result in any IO, it instead returns a scoped
        event store for the category identified by the category name,
        as part of a fluent interface.

        Categories implicitly exist, i.e., calling this method for a category
        that has never been written to will not result in an error.

        Args:
            category (str): The name of the category.

        Returns:
            an event store scoped to the specified category.
        """
        return EventCategory(adapter=self.adapter, category=category)
