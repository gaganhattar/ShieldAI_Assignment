
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
    python -m unittest test_pkg_install_uninstall.py
    ```

For testing purposes, this module contains tests for the `combine_files` function.

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented to functional test package install and unistall.

"""
import unittest
import subprocess
import os

class TestFileOperationsDebPackageFunction(unittest.TestCase):
    """Functional tests for shieldai.assignment_all.deb package."""

    def test_package_generation1(self):
        """Test package generation."""
        try:
            # Generate the deb package
            subprocess.run(["python3", "./create_package.py", "-e"])

            # Check if the package is generated
            self.assertTrue(os.path.exists("shieldai.assignment_1.0_all.deb"))
        except Exception as e:
            self.fail(f"Failed to generate package: {e}")

    def test_package_installation2(self):
        """Test package installation."""
        try:
            # Install the deb package
            subprocess.run(["sudo", "dpkg", "-i", "shieldai.assignment_1.0_all.deb"])

            # Check if the package is installed
            result = subprocess.run(["dpkg", "-l", "shieldai.assignment"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
            self.assertIn("shieldai.assignment", result.stdout)

            # Check if all the expected files are installed
            expected_files = ["copy_file.py", "combine_files.py", "delete_file.py", "create_file.py"]
                              #"test_copy_file.py", "test_combine_files.py", "test_delete_file.py", "test_main.py"]
            
            for file in expected_files:
                self.assertTrue(os.path.exists(f"/usr/local/lib/shieldai_assignment/{file}"))
        except Exception as e:
            self.fail(f"Failed to install package: {e}")

    def test_package_uninstallation3(self):
        """Test package uninstallation."""
        try:
            # Uninstall the deb package
            subprocess.run(["sudo", "dpkg", "-r", "shieldai.assignment"])

            # Check if the package is uninstalled
            result = subprocess.run(["dpkg", "-l", "shieldai.assignment"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
            self.assertNotIn("shieldai.assignment", result.stdout)

            # Check if all the expected files are removed
            print("*****************   Checking Uninstallation  *****************")
            self.assertFalse(os.path.exists(f"/usr/local/lib/shieldai_assignment"))
            self.assertFalse(os.path.exists(f"/usr/local/bin/fileOperations_cmd"))
            self.assertFalse(os.path.exists(f"/usr/local/shieldai_assignment_tests"))
            self.assertFalse(os.path.exixts(f"/usr/share/doc/shieldai_assignment"))
        except Exception as e:
            self.fail(f"Failed to uninstall package: {e}")            

if __name__ == "__main__":
    unittest.main()
