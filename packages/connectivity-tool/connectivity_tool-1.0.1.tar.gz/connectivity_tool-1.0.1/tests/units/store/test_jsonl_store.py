import unittest
from unittest.mock import MagicMock
from unitsnet_py.units.bit_rate import BitRate
from unitsnet_py.units.duration import Duration

from connectivity_tool_cli.common.interfances import Protocols
from connectivity_tool_cli.models.conn_result import ConnResult
from connectivity_tool_cli.store.jsonl_handler import JsonLineHandler
from connectivity_tool_cli.store.jsonl_store import JsonlStore  # Replace with correct import
from tests.test_unit_global import ConnTestCase


class TestJsonlStore(ConnTestCase):

    def setUp(self):
        """ Set up a sample ConnResult instance and mock JsonLineHandler. """
        self.mock_jsonl_handler = MagicMock(spec=JsonLineHandler)
        self.store = JsonlStore(path="temp/test.jsonl")
        self.store.jsonl_handler = self.mock_jsonl_handler  # Replace the handler with the mock

        # Set up a sample ConnResult instance
        self.result = ConnResult()
        self.result.protocol = Protocols.HTTPS
        self.result.success = True
        self.result.alert = False
        self.result.deviation = Duration.from_seconds(0)
        self.result.error_message = None
        self.result.timestamp = '2025-01-01T00:00:00'
        self.result.asset = 'example.com'
        self.result.latency = Duration.from_seconds(50)
        self.result.upload_bandwidth = BitRate.from_bits_per_second(1000)
        self.result.download_bandwidth = BitRate.from_bits_per_second(2000)

    def test_log_results(self):
        """ Test the log_results method. """
        # Call log_results
        self.store.log_results(self.result)

        # Check if append was called on jsonl_handler with the expected dictionary
        self.mock_jsonl_handler.append.assert_called_once_with(self.result.to_dics())

    def test_get_latest_result(self):
        """ Test the get_last_result method to make sure we get the latest result even if there are previous results """
        # Prepare a mock to return data for the iterate method
        mock_result = self.result.to_dics()  # Use the result in dictionary format
        mock_result2 = self.result.to_dics()  # Use the result in dictionary format
        mock_result['success'] = False  # Change the success to False
        self.mock_jsonl_handler.iterate.return_value = [mock_result,
                                                        mock_result2]  ## put the modified result first for testing

        # Call get_last_result
        last_result = self.store.get_last_result(self.result)

        # Assert the result returned matches the expected ConnResult
        self.assertIsNotNone(last_result)
        self.assertEqual(last_result.protocol, Protocols.HTTPS)
        self.assertEqual(last_result.asset, 'example.com')
        self.assertFalse(last_result.success)

    def test_get_last_result_found_skip_diff_protocol(self):
        """ Test the get_last_result method when a matching result is found and skips diff protocol """
        # Prepare a mock to return data for the iterate method
        mock_result = self.result.to_dics()  # Use the result in dictionary format
        mock_result2 = self.result.to_dics()  # Use the result in dictionary format
        mock_result2['protocol'] = Protocols.HTTP  # Change the protocol to HTTP
        mock_result2['success'] = False  # Change the success to False
        self.mock_jsonl_handler.iterate.return_value = [mock_result2,
                                                        mock_result]  ## put the modified result first for testing

        # Call get_last_result
        last_result = self.store.get_last_result(self.result)

        # Assert the result returned matches the expected ConnResult
        self.assertIsNotNone(last_result)
        self.assertEqual(last_result.protocol, Protocols.HTTPS)
        self.assertEqual(last_result.asset, 'example.com')
        self.assertTrue(last_result.success)

    def test_get_last_result_found_skip_diff_asset(self):
        """ Test the get_last_result method when a matching result is found and skips diff asset """
        # Prepare a mock to return data for the iterate method
        mock_result = self.result.to_dics()  # Use the result in dictionary format
        mock_result2 = self.result.to_dics()  # Use the result in dictionary format
        mock_result2['asset'] = 'example.org'  # Change the asset to example.org
        mock_result2['success'] = False  # Change the success to False
        self.mock_jsonl_handler.iterate.return_value = [mock_result2,
                                                        mock_result]  ## put the modified result first for testing

        # Call get_last_result
        last_result = self.store.get_last_result(self.result)

        # Assert the result returned matches the expected ConnResult
        self.assertIsNotNone(last_result)
        self.assertEqual(last_result.protocol, Protocols.HTTPS)
        self.assertEqual(last_result.asset, 'example.com')
        self.assertTrue(last_result.success)

    def test_get_last_result_in_empty(self):
        """ Test the get_last_result method when it's empty. """
        # Prepare a mock to return no matching result
        self.mock_jsonl_handler.iterate.return_value = []

        # Call get_last_result
        last_result = self.store.get_last_result(self.result)

        # Assert that the result is None
        self.assertIsNone(last_result)

    def test_get_last_result_not_found(self):
        """ Test the get_last_result method when no matching result is found. """
        # Prepare a mock to return data for the iterate method
        mock_result = self.result.to_dics()  # Use the result in dictionary format
        mock_result2 = self.result.to_dics()  # Use the result in dictionary format
        mock_result['asset'] = 'example.org'  # Change the asset to example.org
        mock_result2['protocol'] = Protocols.HTTP  # Change the protocol to HTTP
        self.mock_jsonl_handler.iterate.return_value = [mock_result, mock_result2]

        # Call get_last_result
        last_result = self.store.get_last_result(self.result)

        # Assert that the result is None
        self.assertIsNone(last_result)


if __name__ == '__main__':
    unittest.main()
