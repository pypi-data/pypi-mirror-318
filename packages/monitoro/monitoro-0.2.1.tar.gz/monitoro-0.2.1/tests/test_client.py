import unittest
from unittest.mock import patch, Mock
from monitoro_client import MonitoroClient, MonitoroAPIError


class TestMonitoroClient(unittest.TestCase):
    def setUp(self):
        self.client = MonitoroClient("test_token")

    @patch("requests.Session.post")
    def test_extract_data_success(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "data": {"key": "value"}}
        mock_post.return_value = mock_response

        result = self.client.extract_data("monitor_id", "https://example.com")
        self.assertEqual(result, {"success": True, "data": {"key": "value"}})

    @patch("requests.Session.post")
    def test_extract_data_failure(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        with self.assertRaises(MonitoroAPIError):
            self.client.extract_data("monitor_id", "https://example.com")


if __name__ == "__main__":
    unittest.main()
