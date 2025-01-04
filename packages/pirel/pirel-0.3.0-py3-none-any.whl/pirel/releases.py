from __future__ import annotations

import datetime
import json
import logging
import urllib.error
import urllib.request
from typing import Any, Optional

import humanize
import typer
from rich.table import Table

from . import _cache, _utils, python_cli

DATE_NOW = datetime.date.today()
RELEASE_CYCLE_URL = "https://raw.githubusercontent.com/python/devguide/refs/heads/main/include/release-cycle.json"

STATUS_TO_TEXT = {
    "feature": "is [bold]not released yet[/bold] and still accepts new features",
    "prerelease": "is [bold]not released yet[/bold] and still accepts new fixes",
    "bugfix": "is actively maintained (bugfixes) and has security support for more than {eol_delta}",
    "security": "has security support for more than {eol_delta}",
    "end-of-life": "has reached end-of-life! Please upgrade to a newer version of Python",
}

STATUS_TO_EMOJI = {
    "feature": ":sparkles:",
    "prerelease": ":eyes:",
    "bugfix": ":rocket:",
    "security": ":heavy_check_mark:",
    "end-of-life": ":warning:",
}

logger = logging.getLogger("pirel")


def parse_date(date_str: str) -> datetime.date:
    if len(date_str) == len("yyyy-mm"):
        # We need a full yyyy-mm-dd, so let's approximate
        return datetime.date.fromisoformat(date_str + "-01")
    return datetime.date.fromisoformat(date_str)


def date_style(date: datetime.date) -> str:
    """Returns the style for a date for rich table."""
    if date > DATE_NOW:
        # Future, add italics
        return "italic"
    return ""


def status_style(status: str) -> str:
    if status == "end-of-life":
        return "red"
    elif status == "security":
        return "yellow"
    elif status == "bugfix":
        return "green"
    elif status == "prerelease":
        return "blue"
    elif status == "feature":
        return "magenta"
    else:
        raise ValueError(f"Unkown status {status}")


def eol_color(eol: datetime.date) -> str:
    if DATE_NOW >= eol:
        return "red"
    elif datetime.timedelta(days=30 * 6) + DATE_NOW > eol:
        return "dark_orange"
    elif datetime.timedelta(days=365) + DATE_NOW > eol:
        return "yellow"
    else:
        return "green"


def wrap_style(text: str, style: str) -> str:
    if not style:
        return text
    return f"[{style.strip()}]{text}[/{style.strip()}]"


class PythonRelease(_utils.VersionLike):
    def __init__(self, version: str, data: dict[str, Any]):
        self._version = version
        self._status: str = data["status"]
        self._released = parse_date(data["first_release"])
        self._end_of_life = parse_date(data["end_of_life"])
        self._release_manager = data["release_manager"]

    def __str__(self) -> str:
        status_info = STATUS_TO_TEXT[self._status].format(
            eol_delta=humanize.naturaldelta(self._end_of_life - DATE_NOW)
        )
        main_style = status_style(self._status)
        _eol_color = eol_color(self._end_of_life)
        return (
            f"{STATUS_TO_EMOJI[self._status]} [{main_style} bold]"
            f"You are using Python {self.version}[/] which {status_info}"
            f" [{_eol_color}](EOL {self._end_of_life})[/{_eol_color}]"
        )

    def __repr__(self) -> str:
        return f"PythonRelease({self.version})"

    @property
    def version(self) -> str:
        return self._version

    @property
    def version_tuple(self) -> tuple[int, ...]:
        return tuple(map(int, self._version.split(".")))

    @property
    def status(self) -> str:
        return wrap_style(self._status, status_style(self._status))

    @property
    def released(self) -> str:
        return wrap_style(str(self._released), style=date_style(self._released))

    @property
    def end_of_life(self) -> str:
        font_style = date_style(self._end_of_life)
        color = eol_color(self._end_of_life)
        return wrap_style(str(self._end_of_life), style=f"{font_style} {color}")

    @property
    def is_eol(self) -> bool:
        return self._status == "end-of-life"


class PythonReleases:
    def __init__(self, releases_data: dict[str, dict[str, Any]]) -> None:
        self.releases = {
            version: PythonRelease(version, data)
            for version, data in releases_data.items()
        }

    def __getitem__(self, version: str) -> PythonRelease:
        return self.releases[version]

    def to_list(self) -> list[PythonRelease]:
        return list(self.releases.values())

    def to_table(
        self, active_python_version: Optional[python_cli.PythonVersion] = None
    ) -> Table:
        table = Table(title="Python Releases")

        table.add_column("Version", justify="right", style="cyan", no_wrap=True)
        table.add_column("Status", justify="right", no_wrap=True)
        table.add_column("Released", justify="right", style="grey66", no_wrap=True)
        table.add_column("End-of-life", justify="right", no_wrap=True)

        for release in self.releases.values():
            row_style = None
            _version = release.version
            if (
                active_python_version
                and active_python_version.as_release == release.version
            ):
                _version = f"* [bold]{release.version}[/bold]"
                row_style = "bold"

            table.add_row(
                _version,
                release.status,
                release.released,
                release.end_of_life,
                style=row_style,
            )

        return table


def load_releases() -> PythonReleases:
    """Downloads the release cycle data (JSON) from the Python devguide repo."""
    cache_file = _cache.get_latest_cache_file()
    if cache_file and _cache.calc_cache_age_days(cache_file) <= 7:
        logger.info(
            f"Loading Python release cycle data from cache file {str(cache_file)!r}"
        )
        releases_data = _cache.load(cache_file)
    else:
        logger.info(
            f"Downloading Python release cycle data from URL {RELEASE_CYCLE_URL!r}"
        )
        try:
            with urllib.request.urlopen(RELEASE_CYCLE_URL) as f:
                releases_data = json.load(f)
            _cache.save(releases_data)
        except urllib.error.URLError as ex:
            logger.warning(
                f"Failed to load data from URL {RELEASE_CYCLE_URL!r} due to {ex}"
            )
            if cache_file:
                logger.warning(f"Falling back to old cache file {str(cache_file)!r}")
                releases_data = _cache.load(cache_file)
            else:
                logger.error("Could not load data from URL or cache!")
                raise typer.Exit(code=1)

    return PythonReleases(releases_data)
