import unittest
from pathlib import Path

# A class member var to hold the test file name
test_dir = Path("test_dist")

class ConnTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Tests started')

    @classmethod
    def tearDownClass(self):
        print('Tests finished')

if __name__ == "__main__":
    unittest.main()
