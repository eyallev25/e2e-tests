from e2e_tests.consts import CACHE_BASE_URL
import requests

# Define a function to clean a single cache server
def clean_cache(cache_url):
    # Make a request to the cache server to clean it
    response = requests.post(f"{CACHE_BASE_URL}/clean")

    # Check that the response was successful (status code 200)
    assert response.status_code == 200
