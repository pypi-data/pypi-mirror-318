import os
import unittest
from unittest.mock import patch, Mock

from connectivity_tool_cli.common.utils import yaml_to_json

from connectivity_tool_cli.common.example_generator import yaml_example

from connectivity_tool_cli.index import main_function
from tests.test_unit_global import ConnTestCase, test_dir


class E2ETestGenerate(ConnTestCase):

    @patch('sys.argv', [
        'index.py',
        '--generate-path',
        str(test_dir / "./test_suite")
    ])
    def test_cli_generate_example_suite(self):
        """Test the `--generate-path` option."""
        # Define the test directory and file path
        path = test_dir / 'test_suite'
        file_path = path / "test_suite.yaml"
        # Create necessary directories if they don't exist
        path.mkdir(parents=True, exist_ok=True)  # Creates 'store_data' if it doesn't exist

        self.run_cli()

        self.assertTrue(os.path.exists(file_path))

        ## Read the file into string
        with open(file_path, "r") as file:
            content = file.read()
            self.assertEqual(content, yaml_example)

        os.remove(file_path)

    @patch('sys.argv', [
        'index.py',
        '--generate-path',
        str(test_dir / "./test_suite"),
        '--type-format',
        'json'
    ])
    def test_cli_generate_example_suite_json(self):
        """Test the `--generate-path` option."""
        # Define the test directory and file path
        path = test_dir / 'test_suite'
        file_path = path / "test_suite.json"
        # Create necessary directories if they don't exist
        path.mkdir(parents=True, exist_ok=True)  # Creates 'store_data' if it doesn't exist

        self.run_cli()

        self.assertTrue(os.path.exists(file_path))

        ## Read the file into string
        with open(file_path, "r") as file:
            content = file.read()
            self.assertEqual(content, yaml_to_json(yaml_example))

        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
