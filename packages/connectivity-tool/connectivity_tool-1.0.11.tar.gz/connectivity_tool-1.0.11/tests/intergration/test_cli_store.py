import os
import unittest
from unittest.mock import patch, Mock

from connectivity_tool_cli.index import main_function
from tests.test_unit_global import ConnTestCase, test_dir


store_data = \
"""{"protocol": "dns", "success": true, "alert": false, "timestamp": "2025-01-03T19:37:24.848487", "asset": "google.com"}
{"protocol": "http", "success": true, "alert": false, "timestamp": "2025-01-03T20:17:11.656082", "asset": "http://www.google.com", "latency": {"value": 0.4438755512237549, "unit": "Second"}}
"""

class E2ETestStore(ConnTestCase):

    @patch('sys.argv', [
        'index.py',
        '-o',
        '-1',
        '-s',
        str(test_dir / './store_data/print_test.jsonl')
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_print_all_store(self, mock_print: Mock):
        # Define the test directory and file path
        path = test_dir / 'store_data' / 'print_test.jsonl'
        # Create necessary directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)  # Creates 'store_data' if it doesn't exist

        # Write data to the file
        with open(path, 'w') as file:
            file.write(store_data)
        self.run_cli()
        first_print = mock_print.call_args_list[0][0]
        second_print = mock_print.call_args_list[1][0]
        self.assertIn('"protocol": "http"', str(first_print))
        self.assertIn('"protocol": "dns"', str(second_print))

    @patch('sys.argv', [
        'index.py',
        '-o',
        '1',
        '-s',
        str(test_dir / './store_data/print_test.jsonl')
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_print_x_lines_store(self, mock_print: Mock):
        # Define the test directory and file path
        path = test_dir / 'store_data' / 'print_test.jsonl'

        # Create necessary directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)  # Creates 'store_data' if it doesn't exist

        # Write data to the file
        with open(path, 'w') as file:
            file.write(store_data)
        self.run_cli()
        first_print = mock_print.call_args_list[0][0]
        try:
            second_print = mock_print.call_args_list[1][0]
        except IndexError:
            second_print = ""
        self.assertIn('"protocol": "http"', str(first_print))
        self.assertNotIn('"protocol": "dns"', str(second_print))



if __name__ == "__main__":
    unittest.main()
