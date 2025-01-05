import os
import unittest
from pathlib import Path
from unittest.mock import patch, Mock

from unitsnet_py.units.bit_rate import BitRateUnits
from unitsnet_py.units.duration import DurationUnits

from connectivity_tool_cli.store.store_manager import StoreManager

from connectivity_tool_cli.common.utils import yaml_to_json

from connectivity_tool_cli.common.example_generator import yaml_example

from connectivity_tool_cli.index import main_function
from tests.test_unit_global import ConnTestCase, test_dir

current_dir = Path(os.getcwd())

class E2ETestFileSuite(ConnTestCase):

    @patch('sys.argv', [
        'index.py',
        '-f',
        str(current_dir / test_dir / "1test_suite.yaml"),
        '-s',
        str(current_dir / test_dir / "1test_suite.jsonl")
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_run_full_test(self, mock_print: Mock):
        # Define the test directory and file path
        path = current_dir / test_dir # Path to the test directory
        file_path = path / "1test_suite.yaml"
        store_path = path / "1test_suite.jsonl"
        # Create necessary directories if they don't exist
        path.mkdir(parents=True, exist_ok=True)  # Creates 'store_data' if it doesn't exist

        with open(str(file_path), 'w') as file:
            file.write(yaml_example)
        with open(str(store_path), 'w') as file:
            file.write('''{"protocol":"https","success":true,"alert":false,"timestamp":"2025-01-04T20:05:52.984939","asset":"https://www.facebook.com","latency":{"value":0.000000000000009,"unit":"Second"}}\n''')

        self.run_cli()
        first_print = mock_print.call_args_list[0][0]
        self.assertIn('(Test #1)', str(first_print))
        self.assertIn('dns', str(first_print))
        self.assertIn('ynet.co.il', str(first_print))

        forth_print = mock_print.call_args_list[3][0]
        self.assertIn('(Test #4)', str(forth_print))
        self.assertIn('https', str(forth_print))
        self.assertIn('https://www.facebook.com', str(forth_print))
        self.assertIn('with a deviation of', str(forth_print))

        # Get all results...
        store_lines = StoreManager.store().get_last_results(None)
        self.assertEqual(5, len(store_lines))

        ## Last one with bandwidth check
        data = store_lines[0].to_dics()
        self.assertEqual(data['protocol'], 'https')
        self.assertEqual(data['asset'], 'https://www.facebook.com')
        self.assertEqual(data['latency']['unit'], DurationUnits.Second.value)
        self.assertEqual(data['upload_bandwidth']['unit'], BitRateUnits.MegabytePerSecond.value)
        self.assertEqual(data['download_bandwidth']['unit'], BitRateUnits.MegabytePerSecond.value)

        ## The third one with no bandwidth check
        data = store_lines[1].to_dics()
        self.assertEqual(data['protocol'], 'http')
        self.assertEqual(data['asset'], 'http://www.google.com')
        self.assertEqual(data['latency']['unit'], DurationUnits.Second.value)
        self.assertEqual(data.get('upload_bandwidth'), None)
        self.assertEqual(data.get('download_bandwidth'), None)

        ## The second one with not bandwidth and latency check
        data = store_lines[2].to_dics()
        self.assertEqual(data['protocol'], 'dns')
        self.assertEqual(data['asset'], 'yahoo.com')
        self.assertEqual(data.get('latency'), None)
        self.assertEqual(data.get('upload_bandwidth'), None)
        self.assertEqual(data.get('download_bandwidth'), None)

    @patch('sys.argv', [
        'index.py',
        '-f',
        str(current_dir / test_dir / "2test_suite.json"),
        '-s',
        str(current_dir / test_dir / "2test_suite.jsonl"),
        '-t',
        'json'
    ])
    @patch("builtins.print")  # Mock the built-in print function
    def test_cli_run_full_test_json(self, mock_print: Mock):
        # Define the test directory and file path
        path = current_dir / test_dir # Path to the test directory
        file_path = path / "2test_suite.json"
        store_path = path / "2test_suite.jsonl"
        # Create necessary directories if they don't exist
        path.mkdir(parents=True, exist_ok=True)  # Creates 'store_data' if it doesn't exist

        with open(str(file_path), 'w') as file:
            file.write('''{"suite":[{"protocol":"DNS","domain":"yahoo.com"}]}''')
        with open(str(store_path), 'w') as file:
            file.write('')

        StoreManager._instance = None
        self.run_cli()
        first_print = mock_print.call_args_list[0][0]
        self.assertIn('(Test #1)', str(first_print))
        self.assertIn('dns', str(first_print))
        self.assertIn('yahoo.com', str(first_print))

        # Get all results...
        store_lines = StoreManager.store().get_last_results(None)
        self.assertEqual(1, len(store_lines))





if __name__ == "__main__":
    unittest.main()
