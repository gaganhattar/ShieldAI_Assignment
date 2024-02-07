#!/usr/bin/env python3
"""
Module to delete a file.
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

This module provides functionality to delete a file.

Usage:
    To delete a file named "example.txt":
    ```bash
    python delete_file.py example.txt
    ```

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented functionality to delete files.

"""

import argparse
import os

def delete_file(filename):
    """Delete a file.

    Args:
        filename (str): Name of the file to delete.
    """
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete a file")
    parser.add_argument("filename", help="Name of the file to delete")
    args = parser.parse_args()

    delete_file(args.filename)
