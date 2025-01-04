import logging
from pathlib import Path

import pytest
import requests_cache

from nauscopia.setting import datasets_cache_path

logger = logging.getLogger()


@pytest.fixture
def cached_session():
    return requests_cache.CachedSession(cache_name=datasets_cache_path, backend="filesystem")


@pytest.fixture
def standard_void_png_content(cached_session) -> bytes:
    logger.debug(f"PNG content cache: {cached_session.cache.cache_name}")
    response = cached_session.get(
        "https://codeberg.org/sarcam/datasets/media/branch/main/sarcam/2024/standard/standard_void.png",
    )
    response.raise_for_status()
    return response.content


@pytest.fixture
def standard_void_png_file(standard_void_png_content, tmp_path) -> Path:
    # If you want to load the test asset from your local filesystem, do it like this.
    # return Path("/path/to/datasets/sarcam/2024/standard/standard_void.png")

    path = tmp_path / "standard_void.png"
    path.write_bytes(standard_void_png_content)
    return path


@pytest.fixture
def standard_boat_horizon_png_content(cached_session) -> bytes:
    logger.debug(f"PNG content cache: {cached_session.cache.cache_name}")
    response = cached_session.get(
        "https://codeberg.org/sarcam/datasets/media/branch/main/sarcam/2024/standard/standard_boat_horizon_medium.png"
    )
    response.raise_for_status()
    return response.content


@pytest.fixture
def standard_boat_horizon_png_file(standard_boat_horizon_png_content, tmp_path) -> Path:
    # If you want to load the test asset from your local filesystem, do it like this.
    # return Path("/path/to/datasets/sarcam/2024/standard/standard_boat_horizon_medium.png")  # noqa: E501

    path = tmp_path / "standard_boat_horizon_medium.png"
    path.write_bytes(standard_boat_horizon_png_content)
    return path
