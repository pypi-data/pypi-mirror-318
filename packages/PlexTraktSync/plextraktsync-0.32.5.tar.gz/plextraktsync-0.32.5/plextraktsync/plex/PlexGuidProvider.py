from __future__ import annotations

from typing import TYPE_CHECKING

from plextraktsync.plex.PlexGuidProviderIMDB import PlexGuidProviderIMDB
from plextraktsync.plex.PlexGuidProviderLocal import PlexGuidProviderLocal
from plextraktsync.plex.PlexGuidProviderMbid import PlexGuidProviderMbid
from plextraktsync.plex.PlexGuidProviderTMDB import PlexGuidProviderTMDB
from plextraktsync.plex.PlexGuidProviderTVDB import PlexGuidProviderTVDB
from plextraktsync.plex.PlexGuidProviderYoutube import PlexGuidProviderYoutube

if TYPE_CHECKING:
    from plextraktsync.plex.PlexGuid import PlexGuid


class PlexGuidProvider:
    @classmethod
    def create(cls, guid: PlexGuid):
        if guid.provider == "imdb":
            return PlexGuidProviderIMDB(guid)
        if guid.provider == "tmdb":
            return PlexGuidProviderTMDB(guid)
        if guid.provider == "tvdb":
            return PlexGuidProviderTVDB(guid)
        if guid.provider == "mbid":
            return PlexGuidProviderMbid(guid)
        if guid.provider == "youtube":
            return PlexGuidProviderYoutube(guid)
        if guid.provider in ["local", "none"]:
            return PlexGuidProviderLocal(guid)

        raise RuntimeError(f"Unsupported provider: {guid.provider}")
