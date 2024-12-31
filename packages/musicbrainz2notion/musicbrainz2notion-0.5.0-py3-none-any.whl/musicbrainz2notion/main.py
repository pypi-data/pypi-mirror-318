"""Main module."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, cast

import attrs
import frosch  # pyright: ignore[reportMissingTypeStubs]
import tomlkit
import typed_settings as ts
from cyclopts import App, Parameter
from dotenv import load_dotenv
from kajihs_utils.loguru import prompt, setup_logging
from loguru import logger
from notion_client import Client
from toolz import dicttoolz  # pyright: ignore[reportMissingTypeStubs]

from musicbrainz2notion.__about__ import (
    PROJECT_ROOT,
    __app_name__,
    __author_email__,
    __repo_url__,
    __version__,
)
from musicbrainz2notion.canonical_data_processing import (
    MissingCanonicalDataError,
    load_canonical_release_data,
    update_canonical_data,
)
from musicbrainz2notion.config import (
    CONFIG_PATH,
    Settings,
)
from musicbrainz2notion.database_entities import (
    Artist,
    ArtistDBProperty,
    Recording,
    Release,
    ReleaseDBProperty,
    TrackDBProperty,
)
from musicbrainz2notion.database_utils import (
    DATA_DIR,
    compute_mbid_to_page_id_map,
    fetch_artists_to_update,
    get_release_map_with_auto_update,
    move_to_trash_outdated_entity_pages,
)
from musicbrainz2notion.environment import EnvironmentVar
from musicbrainz2notion.musicbrainz_data_retrieval import (
    browse_release_groups_by_artist,
    extract_recording_mbids_and_track_number,
    fetch_artist_data,
    fetch_recording_data,
    fetch_release_data,
    initialize_musicbrainz_client,
)
from musicbrainz2notion.musicbrainz_utils import EntityType, MBDataDict
from musicbrainz2notion.notion_utils import (
    OBJECT_ID_LENGTH,
    extract_id_from_url,
    find_databases_with_properties,
    format_checkbox,
    is_valid_notion_key,
    is_valid_page_id,
)

if TYPE_CHECKING:
    from tomlkit.container import Container as TomlkitContainer

try:
    frosch.hook()  # enable frosch for easier debugging

    setup_logging(log_dir=PROJECT_ROOT / "logs")

    loaded_settings = ts.load(
        Settings,
        appname=__app_name__,
        config_files=[CONFIG_PATH],
        env_prefix=None,
    )

    app = App(version=__version__)
except Exception:
    logger.exception(f"Exception arose during the app setup")
    raise


@app.default
@logger.catch(reraise=True)  # Should be after @app.default
def sync_databases(
    notion_api_key: Annotated[
        str | None,
        Parameter(["--notion", "-n"], env_var=EnvironmentVar.NOTION_API_KEY),
    ] = loaded_settings.notion_api_key or None,
    artist_db_id: Annotated[
        str | None,
        Parameter(["--artist", "-a"], env_var=EnvironmentVar.ARTIST_DB_ID),
    ] = loaded_settings.artist_db_id or None,
    release_db_id: Annotated[
        str | None,
        Parameter(["--release", "-r"], env_var=EnvironmentVar.RELEASE_DB_ID),
    ] = loaded_settings.release_db_id or None,
    track_db_id: Annotated[
        str | None,
        Parameter(["--track", "--recording", "-t"], env_var=EnvironmentVar.TRACK_DB_ID),
    ] = loaded_settings.track_db_id or None,
    fanart_api_key: Annotated[
        str | None,
        Parameter(["--fanart", "-f"], env_var=EnvironmentVar.FANART_API_KEY),
    ] = loaded_settings.fanart_api_key,
    *,
    loaded_settings: Annotated[Settings, Parameter(parse=False)] = loaded_settings,
) -> None:
    """
    Synchronize Notion's Artist, Release, and Track databases with MusicBrainz data.

    Args:
        notion_api_key: Notion API key.
        artist_db_id: Artist database ID.
        release_db_id: Release database ID.
        track_db_id: Track database ID.
        fanart_api_key: Fanart API key.
        loaded_settings: Settings loaded from the configuration file.
    """
    # Get a valid notion API key
    # TODO: Make a separate functions for this in config module
    if notion_api_key is None:
        notion_api_key = prompt("Notion API key")
        while not is_valid_notion_key(notion_api_key):
            logger.warning("Invalid API key")
            notion_api_key = prompt("Notion API key")
        logger.success("Notion API key: OK")

        # Update the config
        with CONFIG_PATH.open() as f:
            full_settings = tomlkit.load(f)
            config = cast("TomlkitContainer", full_settings["musicbrainz2notion"])

        config["notion_api_key"] = notion_api_key
        with CONFIG_PATH.open("w") as f:
            tomlkit.dump(full_settings, f)

    # Initialize the Notion client
    notion_client = Client(auth=notion_api_key)

    # Get valid database ids
    if None in {artist_db_id, release_db_id, track_db_id}:
        main_page_id = prompt("Main page ID or link")
        main_page_id = (
            extract_id_from_url(url=main_page_id, link_1_or_2=1)
            if len(main_page_id) > OBJECT_ID_LENGTH
            else main_page_id
        )
        while not is_valid_page_id(client=notion_client, page_id=main_page_id):
            logger.warning("Invalid main page ID or url")
            main_page_id = prompt("Main page ID or link")
            main_page_id = (
                extract_id_from_url(url=main_page_id, link_1_or_2=1)
                if len(main_page_id) > OBJECT_ID_LENGTH
                else main_page_id
            )
        logger.success("Page ID: OK")
        logger.info("Searching database IDs...")

        # Search database ids in main page
        db_ids = find_databases_with_properties(
            client=notion_client,
            prop_names=[
                (ArtistDBProperty.RELEASES, ArtistDBProperty.TRACKS),
                (ReleaseDBProperty.ARTIST, ReleaseDBProperty.TRACKS),
                (TrackDBProperty.ARTIST, TrackDBProperty.RELEASE),
            ],
            block_id=main_page_id,
        )
        artist_db_id = db_ids[0][0]
        release_db_id = db_ids[1][0]
        track_db_id = db_ids[2][0]

        # Update the config
        with CONFIG_PATH.open() as f:
            full_settings = tomlkit.load(f)
            config = cast("TomlkitContainer", full_settings["musicbrainz2notion"])

        # Update the config
        config["artist_db_id"] = artist_db_id
        config["release_db_id"] = release_db_id
        config["track_db_id"] = track_db_id
        with CONFIG_PATH.open("w") as f:
            tomlkit.dump(full_settings, f)

    settings = attrs.evolve(
        loaded_settings,
        notion_api_key=notion_api_key,
        artist_db_id=artist_db_id,
        release_db_id=release_db_id,
        track_db_id=track_db_id,
        fanart_api_key=fanart_api_key,
    )

    # Initialize the MusicBrainz client
    initialize_musicbrainz_client(__app_name__, __version__, __author_email__)
    logger.info("MusicBrainz client initialized.")

    # TODO: Replace by a TypeDict
    database_ids = {
        EntityType.ARTIST: settings.artist_db_id,
        EntityType.RELEASE: settings.release_db_id,
        EntityType.RECORDING: settings.track_db_id,
    }

    # Loading canonical data
    # Create data dir if it doesn't exist
    DATA_DIR.mkdir(exist_ok=True)
    if settings.force_update_canonical_data or not DATA_DIR.iterdir():
        canonical_release_df = update_canonical_data(DATA_DIR)
    else:
        try:
            canonical_release_df = load_canonical_release_data(DATA_DIR)
        except MissingCanonicalDataError:
            logger.warning(f"Canonical data not found in {DATA_DIR}. Updating...")
            canonical_release_df = update_canonical_data(DATA_DIR)

    # === Retrieve artists to update and compute mbid to page id map === #
    to_update_artist_mbids, artist_mbid_to_page_id_map = fetch_artists_to_update(
        notion_client, settings.artist_db_id
    )
    to_update_artist_mbids += settings.artists_to_update
    logger.info(f"Updating {len(to_update_artist_mbids)} artists.")

    release_mbid_to_page_id_map = compute_mbid_to_page_id_map(notion_client, settings.release_db_id)
    recording_mbid_to_page_id_map = compute_mbid_to_page_id_map(notion_client, settings.track_db_id)

    mbid_to_page_id_map: dict[str, str] = dicttoolz.merge(
        artist_mbid_to_page_id_map, release_mbid_to_page_id_map, recording_mbid_to_page_id_map
    )
    # TODO: Don't fetch all mbids because it doesn't scale well for large databases

    # === Fetch and update each artists data and retrieve their release groups === #
    all_release_groups_data: list[MBDataDict] = []
    for artist_mbid in to_update_artist_mbids:
        artist_data = fetch_artist_data(artist_mbid)
        if artist_data is None:
            continue

        artist = Artist.from_musicbrainz_data(
            artist_data=artist_data,
            auto_added=False,
            min_nb_tags=settings.min_nb_tags,
            fanart_api_key=fanart_api_key,
        )
        artist.synchronize_notion_page(
            notion_api=notion_client,
            database_ids=database_ids,
            mbid_to_page_id_map=mbid_to_page_id_map,
            min_nb_tags=settings.min_nb_tags,
            fanart_api_key=fanart_api_key,
        )

        release_groups_data = browse_release_groups_by_artist(
            artist_mbid=artist_mbid,
            release_type=settings.release_type_filter,
            secondary_type_exclude=settings.release_secondary_type_exclude,
        )
        release_groups_data = release_groups_data or []

        all_release_groups_data += release_groups_data

    # === Fetch and update each canonical release data === #
    release_group_mbids = [release_group["id"] for release_group in all_release_groups_data]

    release_group_to_release_map = get_release_map_with_auto_update(
        release_group_mbids=release_group_mbids,
        data_dir=DATA_DIR,
        canonical_release_df=canonical_release_df,
    )
    del canonical_release_df

    updated_recording_page_ids = set()
    for release_group_data in all_release_groups_data:
        release_group_mbid = release_group_data["id"]
        release_mbid = release_group_to_release_map[release_group_mbid]

        release_data = fetch_release_data(release_mbid)
        if release_data is None:
            continue

        release = Release.from_musicbrainz_data(
            release_data=release_data,
            release_group_data=release_group_data,
            min_nb_tags=settings.min_nb_tags,
            cover_size=settings.cover_size,
        )
        release.synchronize_notion_page(
            notion_api=notion_client,
            database_ids=database_ids,
            mbid_to_page_id_map=mbid_to_page_id_map,
            min_nb_tags=settings.min_nb_tags,
            fanart_api_key=fanart_api_key,
        )

        # === Fetch and update each recording data === #
        for recording_mbid, track_number in extract_recording_mbids_and_track_number(release_data):
            recording_data = fetch_recording_data(recording_mbid)
            if recording_data is None:
                continue
            recording = Recording.from_musicbrainz_data(
                recording_data=recording_data,
                formatted_track_number=track_number,
                release=release,
                min_nb_tags=settings.min_nb_tags,
                add_thumbnail=settings.add_track_thumbnail,
            )
            recording.synchronize_notion_page(
                notion_api=notion_client,
                database_ids=database_ids,
                mbid_to_page_id_map=mbid_to_page_id_map,
                min_nb_tags=settings.min_nb_tags,
                fanart_api_key=fanart_api_key,
            )

            updated_recording_page_ids.add(mbid_to_page_id_map[recording_mbid])

    # === Check for old releases and recordings to delete === #
    updated_artist_page_ids = {
        artist_mbid_to_page_id_map[artist_mbid] for artist_mbid in to_update_artist_mbids
    }
    updated_release_page_ids = {
        mbid_to_page_id_map[release_mbid] for release_mbid in release_group_to_release_map.values()
    }

    move_to_trash_outdated_entity_pages(
        notion_api=notion_client,
        database_id=database_ids[EntityType.RELEASE],
        entity_type=EntityType.RELEASE,
        updated_entity_page_ids=updated_release_page_ids,
        artist_page_ids=updated_artist_page_ids,
        artist_property=ReleaseDBProperty.ARTIST,
    )

    move_to_trash_outdated_entity_pages(
        notion_api=notion_client,
        database_id=database_ids[EntityType.RECORDING],
        entity_type=EntityType.RECORDING,
        updated_entity_page_ids=updated_recording_page_ids,
        artist_page_ids=updated_artist_page_ids,
        artist_property=TrackDBProperty.TRACK_ARTIST,
    )

    # === Update "To update" property of artists === #
    for artist_mbid in to_update_artist_mbids:
        page_id = artist_mbid_to_page_id_map[artist_mbid]
        notion_client.pages.update(
            page_id=page_id,
            properties={ArtistDBProperty.TO_UPDATE: format_checkbox(False)},
        )


def main() -> None:
    """Initialize and launch the app."""
    logger.info(f"🎉 Starting database synchronization! 🎉")
    logger.debug(f"Project root directory set to {PROJECT_ROOT}")
    load_dotenv(PROJECT_ROOT / ".env")

    app()


if __name__ == "__main__":
    main()
