#!/usr/bin/env python3
"""
Module to create a file with optional text.
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

This module provides functionality to create a file with optional text content.

Usage:
    To create a file named "example.txt" with the text "Hello, World!":
    ```bash
    python create_file.py example.txt -t "Hello, World!"
    ```

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented functionality to create files.

"""

import argparse

def create_file(filename, text=None):
    """Create a file with optional text.

    Args:
        filename (str): Name of the file to be created.
        text (str, optional): Text content to write into the file.
    """
    try:
        with open(filename, 'w') as f:
            if text:
                f.write(text)
    except Exception as e:
        print(f"Error occurred while creating file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a file with optional text")
    parser.add_argument("filename", help="Name of the file to be created")
    parser.add_argument("-t", "--text", help="Text content to write into the file")
    args = parser.parse_args()

    create_file(args.filename, args.text)
