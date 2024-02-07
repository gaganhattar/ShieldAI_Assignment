#!/bin/bash

# Unit tests for combine_files.py module.
# Copyright (C) 2024 Gagan J Singh

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This module contains unit tests for the combine_files.py module.

# The combine_files module provides functionality to combine content of two files into a third file.

# Usage:
#     To run the unit tests, use the following command:
#     ```./run_all_unit_tests.sh
#     ```

# For testing purposes, this module contains tests for the `combine_files` function.

# Author: Gagan J Singh
# Email: gagan_hattar@yahoo.com
# Change History:
# 02/06/24    Gagan J Singh   Implemented to unit test combine files functionality.


python3 -m unittest test_combine_files.py
python3 -m unittest test_create_file.py
python3 -m unittest test_copy_file.py
python3 -m unittest test_delete_file.py



