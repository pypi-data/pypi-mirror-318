"""Class that handles the local Raindrop data."""

##############################################################################
# Backward compatibility.
from __future__ import annotations

##############################################################################
# Python imports.
from datetime import datetime
from json import dumps, loads
from pathlib import Path
from typing import Any, Callable, Counter, Iterable, Iterator, Self, Sequence

##############################################################################
# pytz imports.
from pytz import UTC

##############################################################################
# Local imports.
from ...raindrop import (
    API,
    Collection,
    Raindrop,
    SpecialCollection,
    Tag,
    TagData,
    User,
    get_time,
)
from .locations import data_dir


##############################################################################
def local_data_file() -> Path:
    """The path to the file holds the local Raindrop data.

    Returns:
        The path to the local data file.
    """
    return data_dir() / "raindrops.json"


##############################################################################
class Raindrops:
    """Class that holds a group of Raindrops."""

    def __init__(
        self,
        title: str = "",
        raindrops: Iterable[Raindrop] | None = None,
        tags: Sequence[Tag] | None = None,
        search_text: tuple[str, ...] | None = None,
        source: Raindrops | None = None,
    ) -> None:
        """Initialise the Raindrop grouping.

        Args:
            title: The title for the Raindrop grouping.
            raindrops: The raindrops to hold in the group.
        """
        self._title = title
        """The title for the group of Raindrops."""
        self._raindrops = [] if raindrops is None else list(raindrops)
        """The raindrops."""
        self._tags = () if tags is None else tags
        """The list of tags that resulted in this Raindrop group."""
        self._search_text = () if search_text is None else search_text
        """The search text related to this Raindrop group."""
        self._source = source or self
        """The original source for the Raindrops."""

    def set_to(self, raindrops: Iterable[Raindrop]) -> Self:
        """Set the group to the given group of Raindrops.

        Args:
            raindrops: The raindrops to set the group to.

        Returns:
            Self.
        """
        self._raindrops = list(raindrops)
        return self

    @property
    def title(self) -> str:
        """The title of the group."""
        return self._title

    @property
    def is_filtered(self) -> bool:
        """Are the Raindrops filtered in some way?"""
        return bool(self._tags) or bool(self._search_text)

    @property
    def unfiltered(self) -> Raindrops:
        """The original source of the Raindrops, unfiltered."""
        return self._source

    @property
    def description(self) -> str:
        """The description of the content of the Raindrop grouping."""
        filters = []
        if search_text := [f'"{text}"' for text in self._search_text]:
            filters.append(f"contains {' and '.join(search_text)}")
        if self._tags:
            filters.append(f"tagged {', '.join(str(tag) for tag in self._tags)}")
        return f"{'; '.join((self._title, *filters))} ({len(self)})"

    @property
    def tags(self) -> list[TagData]:
        """The list of unique tags found amongst the Raindrops."""
        tags: list[Tag] = []
        for raindrop in self:
            tags.extend(set(raindrop.tags))
        return [TagData(name, count) for name, count in Counter(tags).items()]

    def tagged(self, *tags: Tag) -> Raindrops:
        """Get the raindrops with the given tags.

        Args:
            tags: The tags to look for.

        Returns:
            The subset of Raindrops that have the given tags.
        """
        return Raindrops(
            self.title,
            (raindrop for raindrop in self if raindrop.is_tagged(*tags)),
            tuple(set((*self._tags, *tags))),
            self._search_text,
            self._source,
        )

    def containing(self, search_text: str) -> Raindrops:
        """Get the raindrops containing the given text.

        Args:
            search_text: The text to search for.

        Returns:
            The subset of Raindrops that contain the given text.
        """
        return Raindrops(
            self.title,
            (raindrop for raindrop in self if search_text in raindrop),
            self._tags,
            (*self._search_text, search_text),
            self._source,
        )

    def __iter__(self) -> Iterator[Raindrop]:
        return iter(self._raindrops)

    def __len__(self) -> int:
        return len(self._raindrops)


##############################################################################
class LocalData:
    """Holds and manages the local copy of the Raindrop data."""

    def __init__(self, api: API) -> None:
        """Initialise the object.

        Args:
            api: The Raindrop API client object.
        """
        self._api = api
        """The API client object."""
        self._user: User | None = None
        """The details of the user who is the owner of the Raindrops."""
        self._all: Raindrops = Raindrops("All")
        """All non-trashed Raindrops."""
        self._trash: Raindrops = Raindrops("Trash")
        """All Raindrops in trash."""
        self._collections: dict[int, Collection] = {}
        """An index of all of the Raindrops we know about."""
        self._last_downloaded: datetime | None = None
        """The time the data was last downloaded from the server."""

    @property
    def last_downloaded(self) -> datetime | None:
        """The time the data was downloaded, or `None` if not yet."""
        return self._last_downloaded

    @property
    def user(self) -> User | None:
        """The user that the data relates to."""
        return self._user

    @property
    def all(self) -> Raindrops:
        """All non-trashed raindrops."""
        return self._all

    @property
    def unsorted(self) -> Raindrops:
        """All unsorted raindrops."""
        return Raindrops(
            "Unsorted",
            (raindrop for raindrop in self._all if raindrop.is_unsorted),
        )

    @property
    def untagged(self) -> Raindrops:
        """A non-trashed untagged raindrops."""
        return Raindrops(
            "Untagged",
            (raindrop for raindrop in self._all if not raindrop.tags),
        )

    @property
    def broken(self) -> Raindrops:
        """All non-trashed broken raindrops."""
        return Raindrops(
            "Broken",
            (raindrop for raindrop in self._all if raindrop.broken),
        )

    @property
    def trash(self) -> Raindrops:
        """All trashed raindrops."""
        return self._trash

    def in_collection(self, collection: Collection) -> Raindrops:
        """Get all Raindrops within a given collection.

        Args:
            collection: The collection to get the Raindrops for.

        Returns:
            The raindrops within that collection.
        """
        match collection.identity:
            case SpecialCollection.ALL:
                return self.all
            case SpecialCollection.UNSORTED:
                return self.unsorted
            case SpecialCollection.UNTAGGED:
                return self.untagged
            case SpecialCollection.TRASH:
                return self.trash
            case SpecialCollection.BROKEN:
                return self.broken
            case user_collection:
                return Raindrops(
                    collection.title,
                    [
                        raindrop
                        for raindrop in self._all
                        if raindrop.collection == user_collection
                    ],
                )

    def collection_size(self, collection: Collection) -> int:
        """Get the size of a given collection.

        Args:
            collection: The collection to get the count for.

        Returns:
            The count of raindrops in the collection.
        """
        # Favour the collection's own idea of its count, but if it doesn't
        # have one then do an actual count. The main reason for this is that
        # real collections have real counts, "special" ones don't (but we
        # can work it out).
        return collection.count or len(self.in_collection(collection))

    def collection(self, identity: int) -> Collection:
        """Get a collection from its ID.

        Args:
            identity: The identity of the collection.

        Returns:
            The collection with that identity.
        """
        return self._collections[identity]

    @property
    def collections(self) -> list[Collection]:
        """A list of all known collections."""
        return list(self._collections.values())

    def mark_downloaded(self) -> Self:
        """Mark the raindrops as having being downloaded at the time of calling."""
        self._last_downloaded = datetime.now(UTC)
        return self

    @staticmethod
    def _update_raindrop_count(
        status_update: Callable[[str], None], message: str
    ) -> Callable[[int], None]:
        """Create a raindrop download count update function.

        Args:
            status_update: The function that updates the status.
            message: The message to show against the count.

        Returns:
            A callable that can be passed to the API wrapper.
        """

        def _update(count: int) -> None:
            status_update(f"{message} ({count})")

        return _update

    async def download(self, user: User, status_update: Callable[[str], None]) -> Self:
        """Download all available Raindrops from the server.

        Args:
            user: The user details we're downloading for.

        Returns:
            Self.
        """
        self._user = user
        self._all.set_to(
            await self._api.raindrops(
                SpecialCollection.ALL,
                self._update_raindrop_count(status_update, "Downloading all Raindrops"),
            )
        )
        self._trash.set_to(
            await self._api.raindrops(
                SpecialCollection.TRASH,
                self._update_raindrop_count(status_update, "Downloading trash"),
            )
        )
        status_update("Downloading all collections")
        self._collections = {
            collection.identity: collection
            for collection in await self._api.collections("all")
        }
        return self.mark_downloaded()

    @property
    def _local_json(self) -> dict[str, Any]:
        """All the Raindrops in a JSON-friendly format."""
        return {
            "last_downloaded": None
            if self._last_downloaded is None
            else self._last_downloaded.isoformat(),
            "user": None if self._user is None else self._user.raw,
            "all": [raindrop.raw for raindrop in self._all],
            "trash": [raindrop.raw for raindrop in self._trash],
            "collections": {k: v.raw for k, v in self._collections.items()},
        }

    def save(self) -> Self:
        """Save a local copy of the Raindrop data.

        Returns:
            Self.
        """
        local_data_file().write_text(
            dumps(self._local_json, indent=4), encoding="utf-8"
        )
        return self

    def load(self) -> Self:
        """Load the local copy of the Raindrop data.

        Returns:
            Self.
        """
        if local_data_file().exists():
            data = loads(local_data_file().read_text(encoding="utf-8"))
            self._last_downloaded = get_time(data, "last_downloaded")
            self._user = User.from_json(data.get("user", {}))
            self._all.set_to(
                Raindrop.from_json(raindrop) for raindrop in data.get("all", [])
            )
            self._trash.set_to(
                Raindrop.from_json(raindrop) for raindrop in data.get("trash", [])
            )
            self._collections = {
                int(k): Collection.from_json(v)
                for k, v in data.get("collections", {}).items()
            }
        return self


### local.py ends here
