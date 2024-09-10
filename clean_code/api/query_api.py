import requests
from urllib.parse import urlparse


def make_api_call(url: str) -> dict:
    """
    Makes an API call to the provided URL if there is no query string.
    Returns the response JSON or None if the request is not made.
    """
    parsed_url = urlparse(url)
    
    # Only make the request if the query is empty
    if not parsed_url.query:
        response = requests.post(url)
        return response.json()
    
    # Return None if the URL contains a query (e.g., during tests)
    return None