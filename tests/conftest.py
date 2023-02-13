from e2e_tests.consts import CACHE_BASE_URL
from .utils.helper import clean_cache
import pytest


@pytest.fixture(scope="function", autouse=True)
def clean_caches():

    # List of cache server URLs
    cache_urls = [
        f"{CACHE_BASE_URL}-1",
        f"{CACHE_BASE_URL}-2",
        f"{CACHE_BASE_URL}-3",
    ]

    # Clean each cache server
    for cache_url in cache_urls:
        clean_cache(cache_url)
