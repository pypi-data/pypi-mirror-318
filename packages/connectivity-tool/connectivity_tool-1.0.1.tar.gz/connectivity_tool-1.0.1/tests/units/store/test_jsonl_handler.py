import os
import unittest
from connectivity_tool_cli.store.jsonl_handler import JsonLineHandler
from tests.test_unit_global import ConnTestCase


class JsonlHandlerTestCase(ConnTestCase):

    def setUp(self):
        """
        Create a temporary file for testing.
        """
        self.test_file = os.path.join(self.test_dir, "test.jsonl")
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)
        # Ensure the file is empty before each test
        with open(self.test_file, "w"):
            pass

    def tearDown(self):
        """
        Remove the temporary file after testing.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_append_and_iterate(self):
        """
        Test appending JSON objects and iterating over them.
        """
        handler = JsonLineHandler(self.test_file)

        obj1 = {"name": "Alice", "age": 30}
        obj2 = {"name": "Bob", "age": 25}
        handler.append(obj1)
        handler.append(obj2)

        # Test forward iteration
        results = list(handler.iterate())
        self.assertEqual(results, [obj1, obj2])

        # Test reverse iteration
        results = list(handler.iterate(reverse=True))
        self.assertEqual(results, [obj2, obj1])

    def test_empty_file_iteration(self):
        """
        Test iterating over an empty file.
        """
        handler = JsonLineHandler(self.test_file)

        # Test forward iteration
        results = list(handler.iterate())
        self.assertEqual(results, [])

        # Test reverse iteration
        results = list(handler.iterate(reverse=True))
        self.assertEqual(results, [])

    def test_no_file_creation(self):
        """
        Test iterating over an empty file.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        handler = JsonLineHandler(self.test_file)
        results = list(handler.iterate())
        self.assertEqual(results, [])


    def test_large_file_iteration(self):
        """
        Test iterating over a large file.
        """
        handler = JsonLineHandler(self.test_file)

        # Append a large number of objects
        for i in range(1000):
            handler.append({"index": i})

        # Forward iteration
        for idx, obj in enumerate(handler.iterate()):
            self.assertEqual(obj, {"index": idx})

        # Reverse iteration
        for idx, obj in enumerate(handler.iterate(reverse=True)):
            self.assertEqual(obj, {"index": 999 - idx})

if __name__ == "__main__":
    unittest.main()
