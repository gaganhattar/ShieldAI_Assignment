#!/usr/bin/env python3
"""
Unit tests for delete_file.py module.
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

This module contains unit tests for the delete_file.py module.

The delete_file module provides functionality to delete a file.

Usage:
    To run the unit tests, use the following command:
    ```bash
    python -m unittest test_delete_file.py
    ```

For testing purposes, this module contains tests for the `delete_file` function.

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented unit test to delete file functionality.

"""
import sys
sys.path.append('/opt/shieldai_assignment/lib')
sys.path.append('../fileOperations')


import unittest
import os
from delete_file import delete_file


class TestDeleteFile(unittest.TestCase):
    """Test cases for delete_file.py module."""

    def setUp(self):
        """Set up test environment."""
        with open("test.txt", "w") as f:
            f.write("This is a test file.")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists("test.txt"):
            os.remove("test.txt")

    def test_delete_file(self):
        """Test delete_file function."""
        try:
            delete_file("test.txt")
            self.assertFalse(os.path.exists("test.txt"))
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()
