from api.query_api import make_api_call
from unittest import mock


def test_make_api_call_no_query():
    # Mock requests.post to prevent actual HTTP call
    with mock.patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"status": "success"}
        
        # Test with a URL that has no query
        result = make_api_call("http://some-server.com")
        mock_post.assert_called_once_with("http://some-server.com")
        assert result == {"status": "success"}


def test_make_api_call_with_query():
    # Mock requests.post to prevent actual HTTP call
    with mock.patch("requests.post") as mock_post:
        result = make_api_call("http://some-server.com?test=true")
        
        # Ensure that no API call is made when a query string is present
        mock_post.assert_not_called()
        assert result is None