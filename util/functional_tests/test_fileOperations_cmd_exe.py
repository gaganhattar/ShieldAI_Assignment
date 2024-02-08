#!/usr/bin/env python3
"""
Functional tests for fileOperations_cmd executable.
Copyright (C) 2024 Gagan J Singh

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

These functional tests validate the functionality provided by the fileOperations_cmd executable.

Usage:
    To run the functional tests, use the following command:
    ```bash
    python test_fileOperations_cmd_exe.py
    ```

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented functional testing for all functionality provided by fileOperations_cmd.

"""


import unittest
import subprocess
import os

class TestFileOperationsCmdExe(unittest.TestCase):
    """Functional tests for fileOperations_cmd executable."""
    
    def test_create_file(self):
        """Test creating a file."""
        try:
            # Execute the fileOperations_cmd to create a file
            subprocess.run(["fileOperations_cmd", "create", "test_create.txt", "-t", "Hello, World!"], check=True)

            # Check if the file is created
            self.assertTrue(os.path.exists("test_create.txt"))
        finally:
            # Clean up
            if os.path.exists("test_create.txt"):
                os.remove("test_create.txt")

    def test_copy_file(self):
        """Test copying a file."""
        # Create a source file
        with open("source.txt", "w") as f:
            f.write("This is a source file.")

        try:
            # Execute the fileOperations_cmd to copy the file
            subprocess.run(["fileOperations_cmd", "copy", "source.txt", "destination.txt"], check=True)

            # Check if the file is copied
            self.assertTrue(os.path.exists("destination.txt"))
        finally:
            # Clean up
            os.remove("source.txt")
            if os.path.exists("destination.txt"):
                os.remove("destination.txt")

    def test_combine_files(self):
        """Test combining two files."""
        # Create source files
        with open("file1.txt", "w") as f:
            f.write("This is file 1 content.")
        with open("file2.txt", "w") as f:
            f.write("This is file 2 content.")

        try:
            # Execute the fileOperations_cmd to combine the files
            subprocess.run(["fileOperations_cmd", "combine", "file1.txt", "file2.txt", "output.txt"], check=True)

            # Check if the output file is created and contains the content of both files
            with open("output.txt", "r") as f:
                content = f.read()
            self.assertTrue("This is file 1 content." in content)
            self.assertTrue("This is file 2 content." in content)
        finally:
            # Clean up
            os.remove("file1.txt")
            os.remove("file2.txt")
            os.remove("output.txt")

    def test_delete_file(self):
        """Test deleting a file."""
        # Create a file to delete
        with open("test_delete.txt", "w") as f:
            f.write("This is a test file.")

        try:
            # Execute the fileOperations_cmd to delete the file
            subprocess.run(["fileOperations_cmd", "delete", "test_delete.txt"], check=True)

            # Check if the file is deleted
            self.assertFalse(os.path.exists("test_delete.txt"))
        finally:
            # Clean up
            if os.path.exists("test_delete.txt"):
                os.remove("test_delete.txt")
    
    def test_help_option(self):
        """Test the help option."""
        # Execute the fileOperations_cmd with the help option
        result = subprocess.run(["fileOperations_cmd", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", check=True)

        # Check if the help message is displayed
        self.assertIn("usage:", result.stdout)
        self.assertEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()
