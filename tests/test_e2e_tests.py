import logging
import pytest
import requests
import json
from e2e_tests.consts import MONITOR_URL, ROUTER_URL, CACHE_BASE_URL
from .utils.helper import clean_cache

logging.basicConfig(filename="tests.log", level=logging.DEBUG)


@pytest.fixture(scope="module")
def get_cache_servers():
    response = requests.get(MONITOR_URL)

    # Check that the response was successful (status code 200)
    assert response.status_code == 200

    # Parse the JSON data from the response
    cache_states = json.loads(response.text)

    # Loop through the cache states and check that they are either "Available" or "Not available"
    for cache_name, cache_state in cache_states.items():
        assert cache_state in [
            "Available",
            "Not available",
        ], f"Invalid cache state: {cache_state}"

    # Create a list of only the available cache servers
    available_servers = [
        cache_name
        for cache_name, cache_state in cache_states.items()
        if cache_state == "Available"
    ]

    return available_servers


@pytest.fixture(scope="module")
def clean_caches_module():

    # List of cache server URLs
    cache_urls = [
        f"{CACHE_BASE_URL}-1",
        f"{CACHE_BASE_URL}-2",
        f"{CACHE_BASE_URL}-3",
    ]

    # Clean each cache server
    for cache_url in cache_urls:
        clean_cache(cache_url)


@pytest.mark.parametrize(
    "times",
    [
        (2),
        (10),
        (15),
    ],
)
def test_example(clean_caches_module, get_cache_servers, times):

    for i in range(1, times + 1):
        # Make a request for video content
        res = requests.get(ROUTER_URL)

        # Verify that the response is a 302 redirect
        logging.debug(f"Response status code: {res.status_code}")
        assert res.status_code == 302

        # Verify that the location header contains the correct cache hostname
        logging.debug(f"Location header: {res.headers['Location']}")

        location = res.headers["Location"]
        assert any(
            location.startswith(f"https://{cache_host}")
            for cache_host in get_cache_servers
        ), f"Unexpected cache host: {location}"

        # Follow the redirect and verify the final response from the cache
        res = requests.get(res.headers["Location"])
        logging.debug(f"Response status code: {res.status_code}")
        assert res.status_code == 200
        logging.debug(f"Content-Type header: {res.headers['Content-Type']}")
        assert res.headers["Content-Type"].startswith("video/")
