import os
import unittest
from unittest.mock import patch

from connectivity_tool_cli.index import main_function
from tests.test_unit_global import ConnTestCase, test_dir


class TestConnectivityToolCLI(ConnTestCase):

    @patch('sys.argv', [
        'index.py',
        '--generate-path',
        str(test_dir / "./test_suite")
    ])
    def test_cli_generate_example_suite(self):
        """Test the `--generate-path` option."""
        temp_dir = test_dir / "./test_suite"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        main_function()

        self.assertTrue(os.path.exists(os.path.join(temp_dir, "test_suite.yaml")))

        # Cleanup
        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            os.rmdir(temp_dir)

    @patch('sys.argv', [
        'index.py',
        '--protocol',
        'invalid_protocol'
    ])
    def test_cli_invalid_protocol(self):
        """Test invalid protocol input."""
        with self.assertRaises(SystemExit) as cm:
            main_function()
        self.assertNotEqual(cm.exception.code, 0)



if __name__ == "__main__":
    unittest.main()
