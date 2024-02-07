#!/usr/bin/env python3
"""
Module to copy a file from source to destination.
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

This module provides functionality to copy a file from source to destination.

Usage:
    To copy a file named "source.txt" to "destination.txt":
    ```bash
    python copy_file.py source.txt destination.txt
    ```
Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented functionality to copy files.

"""

import argparse
import shutil

def copy_file(source, destination):
    """Copy a file from source to destination.

    Args:
        source (str): Source file to copy.
        destination (str): Destination to copy the file.
    """
    try:
        shutil.copy(source, destination)
    except Exception as e:
        print(f"Error occurred while copying file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy a file")
    parser.add_argument("source", help="Source file to copy")
    parser.add_argument("destination", help="Destination to copy the file")
    args = parser.parse_args()

    copy_file(args.source, args.destination)
