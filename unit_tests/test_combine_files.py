#!/usr/bin/env python3
""" 
Unit tests for combine_files.py module.
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

This module contains unit tests for the combine_files.py module.

The combine_files module provides functionality to combine content of two files into a third file.

Usage:
    To run the unit tests, use the following command:
    ```bash
    python -m unittest test_combine_files.py
    ```

For testing purposes, this module contains tests for the `combine_files` function.

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented to unit test combine files functionality.

"""
import sys
sys.path.append('/opt/shieldai_assignment/lib')
sys.path.append('../fileOperations')

import unittest
import os
from combine_files import combine_files

class TestCombineFiles(unittest.TestCase):
    """Test cases for combine_files.py module."""

    def setUp(self):
        """Set up test environment."""
        with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
            f1.write("This is the content of file1.")
            f2.write("This is the content of file2.")

    def tearDown(self):
        """Clean up test environment."""
        files_to_remove = ["file1.txt", "file2.txt", "output.txt"]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_combine_files(self):
        """Test combine_files function."""
        try:
            combine_files("file1.txt", "file2.txt", "output.txt")

            content = ""
            with open("output.txt", "r") as f:
                content = f.read()
            
            self.assertTrue("This is the content of file1." in content)
            self.assertTrue("This is the content of file2." in content)
        except Exception as e:
            self.fail(f"An error occurred: {e}")

    def test_combined_content_order(self):
        """Test if the combined output contains the content of each input file in order."""
        try:
            combine_files("file1.txt", "file2.txt", "output.txt")
            
            content_combined = ""; content_f1 = ""; content_f2 = "";
            with open("output.txt", "r") as f:
                content_combined = f.read()

            with open("file1.txt", "r") as f1:
                content_f1 = f1.read()
                
            with open("file2.txt", "r") as f2:
                content_f2 = f2.read()
            
            self.assertLess(content_combined.find(content_f1), 
                            content_combined.find(content_f2),
                            f"Debug: \
                              File1_content = {content_combined.find(content_f1)}, \
                              File2_content = {content_combined.find(content_f2)}")
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()
