import unittest
from unittest.mock import patch, Mock

from connectivity_tool_cli.index import main_function
from tests.test_unit_global import ConnTestCase, test_dir


class E2ETestDirect(ConnTestCase):

    @patch('sys.argv', [
        'index.py',
        '-p',
        'dns',
        '-d',
        'google.com'
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_test_dns(self, mock_print: Mock):
        self.run_cli()
        mock_print.assert_called()
        # Retrieve the arguments passed to `print`
        first_print = mock_print.call_args_list[0][0]
        self.assertIn("(Test #1)", str(first_print))

    @patch('sys.argv', [
        'index.py',
        '-p',
        'https',
        '-u',
        'https://google.com'
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_test_https(self, mock_print: Mock):
        self.run_cli()
        mock_print.assert_called()
        # Retrieve the arguments passed to `print`
        first_print = mock_print.call_args_list[0][0]
        self.assertIn("(Test #1)", str(first_print))

    @patch('sys.argv', [
        'index.py',
        '-p',
        'http',
        '-u',
        'http://google.com'
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_test_http(self, mock_print: Mock):
        self.run_cli()
        mock_print.assert_called()
        # Retrieve the arguments passed to `print`
        first_print = mock_print.call_args_list[0][0]
        self.assertIn("(Test #1)", str(first_print))

    @patch('sys.argv', [
        'index.py',
        '--protocol',
        'invalid_protocol'
    ])
    def test_cli_invalid_protocol(self):
        """Test invalid protocol input."""
        with self.assertRaises(SystemExit) as cm:
            self.run_cli()
        self.assertNotEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
