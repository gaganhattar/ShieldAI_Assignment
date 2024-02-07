#!/usr/bin/env python3
"""
Unit tests for create_file.py module.
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

This module contains unit tests for the create_file.py module.

The create_file module provides functionality to create a file with optional text content.

Usage:
    To run the unit tests, use the following command:
    ```bash
    python -m unittest test_create_file.py
    ```

For testing purposes, this module contains tests for the `create_file` function.

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented unit test to create file functionality.

"""
import sys
sys.path.append('/opt/shieldai_assignment/lib')
sys.path.append('../fileOperations')

import unittest
import os
from create_file   import create_file

class TestCreateFile(unittest.TestCase):
    """Test cases for create_file.py module."""

    def test_create_file_without_text(self):
        """Test create_file function without text."""
        try:
            create_file("test.txt")
            self.assertTrue(os.path.exists("test.txt"))
        except Exception as e:
            self.fail(f"An error occurred: {e}")

    def test_create_file_with_text(self):
        """Test create_file function with text."""
        try:
            create_file("test.txt", "Hello, World!")
            with open("test.txt", "r") as f:
                content = f.read()
            self.assertEqual(content, "Hello, World!")
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()
