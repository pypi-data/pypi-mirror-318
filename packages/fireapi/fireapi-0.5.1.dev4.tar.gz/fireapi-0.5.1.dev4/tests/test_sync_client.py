import unittest
from unittest.mock import patch, MagicMock
from src.fireapi import FireAPI
from src.fireapi._exceptions import APIAuthenticationError, APIRequestError


class TestFireAPISyncClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.client = FireAPI(api_key=self.api_key)

    @patch("requests.Session.request")
    def test_get_config_success(self, mock_request):
        # Mock a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "data": {}}
        mock_request.return_value = mock_response

        response = self.client.vm.get_config()
        self.assertEqual(response.status, "success")
        mock_request.assert_called_once()

    @patch("requests.Session.request")
    def test_authentication_error(self, mock_request):
        # Mock an authentication error response
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = APIAuthenticationError(
            "Authentication failed."
        )
        mock_request.return_value = mock_response

        with self.assertRaises(APIAuthenticationError):
            self.client.vm.get_config()

    @patch("requests.Session.request")
    def test_request_error(self, mock_request):
        # Simulate a network error
        mock_request.side_effect = Exception("Network error")

        with self.assertRaises(APIRequestError):
            self.client.vm.get_config()


if __name__ == "__main__":
    unittest.main()
