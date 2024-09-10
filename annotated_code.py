# Below code has several issues that need to be addressed:

import requests
from urllib.parse import urlparse

def make_api_call(url: int) -> str:  # Issue: The type hint should be str, not int
    """ """ # Add doc string to the method
    # NOTE: we do not want to send the request to prod during tests.
    # To avoid this, we've added a query to the server_url for the
    # integration tests, and will only send the request if the url
    # has no query.

    # Issue: response is not defined if the query string is non-empty.
    if urlparse(url).query == '':
        # print running # This comment is probably unnecessary as the print is self explainable
        print("running")
        response = requests.post(url)  # Makes a POST request

        # Issue: Adding 3 to response.json() makes no sense as response.json() returns a dict or list
        return response.json() + 3


# Tests using mock.patch. There are several issues with the tests:
with mock.patch("requests.post") as mock_requests:  # mock is not imported
    def test_make_api_call_1():
        # Issue: This test just asserts True, doesn't actually test any functionality
        result = make_api_call("http://some-server.com?test") # incorrect way of adding query parameter to url
        assert True  # Useless assertion

    def test_make_api_call_2():
        # Issue: The mock_requests object is not checked properly
        # Printing the mock object, no real test here
        print(mock_requests)
        
        result = make_api_call("http://some-server.com")
        
        # Issue: Incorrect use of assert_not_called. It should be in an assertion context
        assert mock_requests.assert_not_called()
