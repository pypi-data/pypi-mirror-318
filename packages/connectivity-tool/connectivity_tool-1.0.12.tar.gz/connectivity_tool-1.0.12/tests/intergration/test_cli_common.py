import logging
import os
import unittest
from unittest.mock import patch, Mock

from connectivity_tool_cli.common.logger import logger

from connectivity_tool_cli.index import main_function
from tests.test_unit_global import ConnTestCase, test_dir


class E2ETestCommon(ConnTestCase):

    @patch('sys.argv', [
        'index.py',
        '--info'
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_info_print(self, mock_print: Mock):
        """Test the `--info` option."""
        self.run_cli()
        mock_print.assert_called()
        # Retrieve the arguments passed to `print`
        first_print = mock_print.call_args_list[0][0]
        second_print = mock_print.call_args_list[1][0]
        self.assertIn("Connectivity Tool CLI by Haim Kastner <hello@haim-kastner.com>", str(first_print))
        self.assertIn("cli_version", str(second_print))

    @patch('sys.argv', [
        'index.py',
        '-o 1',
        '--verbose'
    ])
    @patch("connectivity_tool_cli.common.logger.logging.Logger.info")
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_verbose(self, mock_print: Mock, mock_logger_info: Mock):
        self.run_cli()
        mock_print.assert_called()
        # Retrieve the arguments passed to `print`
        first_print = mock_print.call_args_list[0][0]
        second_print = mock_print.call_args_list[1][0]
        self.assertIn("Connectivity Tool CLI", str(first_print))
        self.assertIn("cli_version", str(second_print))

        mock_logger_info.assert_called()
        # Retrieve the arguments passed to `print`
        first_print = mock_logger_info.call_args_list[0][0]
        self.assertIn("Printing ", str(first_print))

    @patch('sys.argv', [
        'index.py',
        '-o 1',
        '--verbose'
    ])
    def test_cli_verbose_on(self):
        self.run_cli()
        self.assertEqual(logger.getEffectiveLevel(), logging.INFO)

    @patch('sys.argv', [
        'index.py',
        '-o 1',
    ])
    def test_cli_verbose_off(self):
        self.run_cli()
        self.assertEqual(logger.getEffectiveLevel(), logging.CRITICAL)


if __name__ == "__main__":
    unittest.main()
