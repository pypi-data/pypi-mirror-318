import os
import unittest
from unittest.mock import patch, mock_open

from connectivity_tool_cli.common.example_generator import generate_example_suite_file, yaml_example
from connectivity_tool_cli.common.interfances import SuiteFormats
from connectivity_tool_cli.common.utils import yaml_to_json
from tests.test_unit_global import ConnTestCase


class TestGenerateExampleSuiteFile(ConnTestCase):

    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_example_suite_file_yaml(self, mock_open_file, mock_path_exists, mock_makedirs):
        path = "test_directory"
        format_type = SuiteFormats.YAML

        # Call the function
        generate_example_suite_file(path, format_type)

        # Assertions for directory creation
        mock_path_exists.assert_called_once_with(path)
        mock_makedirs.assert_called_once_with(path)

        # Assertions for file creation
        mock_open_file.assert_called_once_with(os.path.join(path, 'test_suite.yaml'), 'w')
        handle = mock_open_file()
        handle.write.assert_called_once_with("""
suite:
  - protocol: DNS
    domain: "ynet.co.il"

  - protocol: DNS
    domain: "yahoo.com"

  - protocol: HTTP
    url: "http://www.google.com"

  - protocol: HTTPS
    url: "https://www.facebook.com"
    latency_threshold_deviation:
      value: 1
      unit: Millisecond
    test_upload_bandwidth: true
    test_download_bandwidth: true
""")

    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_example_suite_file_json(self, mock_open_file, mock_path_exists, mock_makedirs):
        path = "test_directory"
        format_type = SuiteFormats.JSON

        # Call the function
        generate_example_suite_file(path, format_type)

        # Assertions for directory creation
        mock_path_exists.assert_called_once_with(path)
        mock_makedirs.assert_called_once_with(path)

        # Assertions for file creation
        mock_open_file.assert_called_once_with(os.path.join(path, 'test_suite.json'), 'w')

        handle = mock_open_file()
        handle.write.assert_called_once_with(yaml_to_json(yaml_example))


if __name__ == '__main__':
    unittest.main()
