from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plextraktsync.plex.PlexGuid import PlexGuid


class PlexGuidProviderTVDB:
    def __init__(self, guid: PlexGuid):
        self.guid = guid

    @property
    def link(self):
        return f"https://www.thetvdb.com/dereferrer/{self.guid.type}/{self.guid.id}"

    @property
    def title(self):
        return f"{self.guid.provider}:{self.guid.type}:{self.guid.id}"
