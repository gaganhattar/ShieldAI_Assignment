#!/usr/bin/env python3
"""
Unit tests for copy_file.py module.
Copyright (C) 2024 Gagan J Singh

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
This module contains unit tests for the copy_file.py module.

The copy_file module provides functionality to copy a file from source to destination.

Usage:
    To run the unit tests, use the following command:
    ```bash
    python -m unittest test_copy_file.py
    ```

For testing purposes, this module contains tests for the `copy_file` function.

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented unit test to file copy functionality.

"""
import sys
sys.path.append('/opt/shieldai_assignment/lib')
sys.path.append('../fileOperations')

import unittest
import os
from copy_file     import copy_file

class TestCopyFile(unittest.TestCase):
    """Test cases for copy_file.py module."""

    def setUp(self):
        """Set up test environment."""
        with open("source.txt", "w") as f:
            f.write("This is the source file content.")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists("source.txt"):
            os.remove("source.txt")
        if os.path.exists("destination.txt"):
            os.remove("destination.txt")

    def test_copy_file(self):
        """Test copy_file function."""
        try:
            copy_file("source.txt", "destination.txt")
            self.assertTrue(os.path.exists("destination.txt"))
        except Exception as e:
            self.fail(f"An error occurred: {e}")

    def test_copied_content_matches_source(self):
        """Test if the content of copied file matches with the source file."""
        try:
            copy_file("source.txt", "destination.txt")
            with open("source.txt", "r") as source_file:
                source_content = source_file.read()
            with open("destination.txt", "r") as copied_file:
                copied_content = copied_file.read()
            self.assertEqual(source_content, copied_content)
        except Exception as e:
            self.fail(f"An error occurred: {e}")

    def test_copied_file_empty_when_source_empty(self):
        """Test if the copied file is empty when the source file is empty."""
        try:
            with open("source.txt", "w") as source_file:
                source_file.write("")
            copy_file("source.txt", "destination.txt")
            with open("destination.txt", "r") as copied_file:
                copied_content = copied_file.read()
            self.assertEqual(copied_content, "")
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()
