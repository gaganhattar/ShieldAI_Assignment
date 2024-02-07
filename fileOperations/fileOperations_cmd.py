#!/usr/bin/env python3
"""
Main script for performing file operations.
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

This script provides functionality to perform various file operations such as create, copy, combine, or delete.

Usage:
    To perform file operations:
    ```bash
    python main.py create new_file.txt -t "optional text"
    python main.py copy source_file.txt destination_file.txt
    python main.py combine file1.txt file2.txt output.txt
    python main.py delete file_to_delete.txt
    ```

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented functionality to support all functionality of this package.

"""

import argparse
import create_file
import copy_file
import combine_files
import delete_file

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="File Operations")
    subparsers = parser.add_subparsers(dest="command")

    # Sub-parser for create file
    parser_create = subparsers.add_parser("create", help="Create a file")
    parser_create.add_argument("filename", help="Name of the file to create")
    parser_create.add_argument("-t", "--text", help="Optional text to write into the file")

    # Sub-parser for copy file
    parser_copy = subparsers.add_parser("copy", help="Copy a file")
    parser_copy.add_argument("source", help="Source file to copy")
    parser_copy.add_argument("destination", help="Destination to copy the file")

    # Sub-parser for combine files
    parser_combine = subparsers.add_parser("combine", help="Combine two files into a third")
    parser_combine.add_argument("inputfile1", help="First filename to combine")
    parser_combine.add_argument("inputfile2", help="Second filename to combine")
    parser_combine.add_argument("outputfile", help="Output filename after combining")

    # Sub-parser for delete file
    parser_delete = subparsers.add_parser("delete", help="Delete a file")
    parser_delete.add_argument("filename", help="Name of the file to delete")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    try:
        if args.command == "create":
            create_file.create_file(args.filename, args.text)
        elif args.command == "copy":
            copy_file.copy_file(args.source, args.destination)
        elif args.command == "combine":
            combine_files.combine_files(args.inputfile1, args.inputfile2, args.outputfile)
        elif args.command == "delete":
            delete_file.delete_file(args.filename)
        else:
            raise ("invalid option try again")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
