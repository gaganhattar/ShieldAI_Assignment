#!/usr/bin/env python3

import sys
sys.path.append('/opt/shieldai_assignment/lib')
sys.path.append('../fileOperations')


import unittest
import os
from create_file   import create_file
from copy_file     import copy_file
from combine_files import combine_files
from delete_file   import delete_file

class TestMain(unittest.TestCase):
    """Test cases for main.py module."""

    def setUp(self):
        """Set up test environment."""
        with open("source.txt", "w") as f:
            f.write("This is a source file.")
        with open("file1.txt", "w") as f:
            f.write("This is file 1 content.")
        with open("file2.txt", "w") as f:
            f.write("This is file 2 content.")

    def tearDown(self):
        """Clean up test environment."""
        files_to_remove = ["source.txt", "file1.txt", "file2.txt", "destination.txt", "output.txt"]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_create_file(self):
        """Test create_file function."""
        try:
            create_file("test.txt", "Hello, World!")
            self.assertTrue(os.path.exists("test.txt"))
        except Exception as e:
            self.fail(f"create_file raised an unexpected exception: {e}")

    def test_copy_file(self):
        """Test copy_file function."""
        try:
            copy_file("source.txt", "destination.txt")
            self.assertTrue(os.path.exists("destination.txt"))
        except Exception as e:
            self.fail(f"copy_file raised an unexpected exception: {e}")

    def test_combine_files(self):
        """Test combine_files function."""
        try:
            combine_files("file1.txt", "file2.txt", "output.txt")
            with open("output.txt", "r") as f:
                content = f.read()
            self.assertTrue("This is file 1 content." in content)
            self.assertTrue("This is file 2 content." in content)
        except Exception as e:
            self.fail(f"combine_files raised an unexpected exception: {e}")

    def test_delete_file(self):
        """Test delete_file function."""
        try:
            with open("test.txt", "w") as f:
                f.write("This is a test file.")
            delete_file("test.txt")
            self.assertFalse(os.path.exists("test.txt"))
        except Exception as e:
            self.fail(f"delete_file raised an unexpected exception: {e}")

if __name__ == "__main__":
    unittest.main()
