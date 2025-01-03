import asyncio
import unittest
from unittest.mock import patch, MagicMock
from src.fireapi import AsyncFireAPI
from src.fireapi._exceptions import APIAuthenticationError, APIRequestError


class TestFireAPIAsyncClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.client = AsyncFireAPI(api_key=self.api_key)

    @patch("aiohttp.ClientSession.request")
    async def test_get_config_success(self, mock_request):
        # Mock a successful API response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = asyncio.coroutine(
            lambda: {"status": "success", "data": {}}
        )
        mock_request.return_value.__aenter__.return_value = mock_response

        response = await self.client.vm.get_config()
        self.assertEqual(response.status, "success")
        mock_request.assert_called_once()

    @patch("aiohttp.ClientSession.request")
    async def test_authentication_error(self, mock_request):
        # Mock an authentication error response
        mock_response = MagicMock()
        mock_response.status = 401
        mock_response.raise_for_status.side_effect = APIAuthenticationError(
            "Authentication failed."
        )
        mock_request.return_value.__aenter__.return_value = mock_response

        with self.assertRaises(APIAuthenticationError):
            await self.client.vm.get_config()

    @patch("aiohttp.ClientSession.request")
    async def test_request_error(self, mock_request):
        # Simulate a network error
        mock_request.side_effect = Exception("Network error")

        with self.assertRaises(APIRequestError):
            await self.client.vm.get_config()


if __name__ == "__main__":
    unittest.main()
