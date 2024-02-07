#!/usr/bin/env python3
"""
Module to combine content of two files into a third file.
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

This module provides functionality to combine content of two files into a third file.

Usage:
    To combine "file1.txt" and "file2.txt" into "output.txt":
    ```bash
    python combine_files.py file1.txt file2.txt output.txt
    ```

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented functionality to combine files.

"""

import argparse

def combine_files(file1, file2, output):
    """Combine content of file1 and file2 into output file.

    Args:
        file1 (str): First file to combine.
        file2 (str): Second file to combine.
        output (str): Output file after combining.
    """
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
            out.write(f1.read())
            out.write(f2.read())
    except Exception as e:
        print(f"Error occurred while combining files: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine two files into a third")
    parser.add_argument("file1", help="First file to combine")
    parser.add_argument("file2", help="Second file to combine")
    parser.add_argument("output", help="Output file after combining")
    args = parser.parse_args()

    combine_files(args.file1, args.file2, args.output)
