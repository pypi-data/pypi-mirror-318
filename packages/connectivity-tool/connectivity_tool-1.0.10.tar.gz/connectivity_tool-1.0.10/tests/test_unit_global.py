import unittest
from pathlib import Path

from connectivity_tool_cli.index import main_function
from connectivity_tool_cli.store.store_manager import StoreManager

# A class member var to hold the test file name
test_dir = Path("test_dist")

class ConnTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Tests started')

    @classmethod
    def tearDownClass(self):
        print('Tests finished')

    def run_cli(self):
        # Make sure the store is re-initialized
        StoreManager._instance = None
        # Run the main function
        main_function()


if __name__ == "__main__":
    unittest.main()
