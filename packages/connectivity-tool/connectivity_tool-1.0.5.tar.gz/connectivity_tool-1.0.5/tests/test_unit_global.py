import unittest

class ConnTestCase(unittest.TestCase):

    # A class member var to hold the test file name
    test_dir = "test_dist"

    @classmethod
    def setUpClass(self):
        print('Tests started')

    @classmethod
    def tearDownClass(self):
        print('Tests finished')

if __name__ == "__main__":
    unittest.main()
