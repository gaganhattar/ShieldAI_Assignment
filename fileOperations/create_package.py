#!/usr/bin/env python3
"""
Module to create Python executable and Debian package.
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

This module provides functionality to create a Python executable and Debian package from the generated Python files.

Usage:
    To create a Python executable:
    ```bash
    python create_package.py -e
    ```

    To create a Debian package:
    ```bash
    python create_package.py -d
    ```

    To create a Debian test package:
    ```bash
    python create_package.py -t
    ```

Author: Gagan J Singh
Email: gagan_hattar@yahoo.com
Change History:
02/06/24    Gagan J Singh   Implemented script to generate python executable and .deb package.

"""
import argparse
import os
import shutil
import subprocess
from io import StringIO
import sys

def create_python_executable():
    """Create Python executable using pyinstaller."""
    try:
        subprocess.run(["pyinstaller", "--onefile", "fileOperations_cmd.py"], check=True)
        #os.rename("dist/main", "../fileOperations_cmd.py")
        print("build/ and dist/ folders created, needed for creating debian package !!")
        print("fileOperations_cmd executable generated in dist/ folder, try executing it!!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating Python executable: {e}")
        raise

def create_deb_package():
    """Create deb package using dpkg-deb."""
    try:
        if os.path.exists("dist/fileOperations_cmd"):
            package_name = "shieldai.assignment"
            version = "1.0"
            output_dir = "dist"
            deb_name = f"{package_name}_{version}_all.deb"
                        
            # Create the DEBIAN directory structure
            debian_dir = os.path.join(output_dir, "DEBIAN")
            os.makedirs(debian_dir, exist_ok=True)

            # Write control file
            control_content = ""
            for line in [f"Package: {package_name}", f"Version: {version}", "Architecture: all", 
                         "Maintainer: Gagan J Singh <gagan_hattar@yahoo.com>", 
                         f"Description: package for {package_name}"]:
                control_content += line + "\n"

            control_file = os.path.join(debian_dir, "control")
            with open(control_file, "w") as f:
                f.write(control_content)
            os.chmod(debian_dir, 0o775)
            # Copy test files to package directory
            package_dir = os.path.join(output_dir, "usr/bin")
            os.makedirs(package_dir, exist_ok=True)

            # Build the package
            subprocess.run(["dpkg-deb", "--build", output_dir, deb_name], check=True)
            print("shieldai_assignment.1.0_all.deb created")
        else:
            print("Generate executable first using '-e' option ")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating Debian package: {e}")
        raise

def create_deb_test_package():
    """Create deb test package including all test files located in ./tests folder."""
    try:
        package_name = "ShieldAI_Assignment-tests"
        version = "1.0"
        output_dir = "dist_tests"
        deb_name = f"{package_name}_{version}_all.deb"

        # Create the DEBIAN directory structure
        debian_dir = os.path.join(output_dir, "DEBIAN")
        os.makedirs(debian_dir, exist_ok=True)

        # Write control file
        control_content = ""
        for line in [f"Package: {package_name}", f"Version: {version}", "Architecture: all", 
                        "Maintainer: Gagan J Singh <gagan_hattar@yahoo.com>", 
                        f"Description: Test package for {package_name}"]:
            control_content += line + "\n"
        control_file = os.path.join(debian_dir, "control")
        with open(control_file, "w") as f:
            f.write(control_content)

        # Copy test files to package directory
        package_dir = os.path.join(output_dir, "usr/bin/")
        os.makedirs(package_dir, exist_ok=True)

        tests_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ShieldAI_Assignment_tests")
        for root, _, filenames in os.walk(tests_folder):
            for filename in filenames:
                shutil.copy(os.path.join(root, filename), package_dir)

        # Build the package
        subprocess.run(["dpkg-deb", "--build", output_dir, deb_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating test Debian package: {e}")
        raise

def copy_python_files_to_dist():
    """Move all Python files to dist folder."""
    try:
        if not os.path.exists("dist"):
            os.makedirs("dist")

        for filename in os.listdir("."):
            if filename.endswith(".py"):
                shutil.copy(filename, os.path.join("dist", filename))
    except Exception as e:
        print(f"Error occurred while moving Python files to dist folder: {e}")
        raise

def copy_python_files_to_dist_test():
    """Move all Python files to dist folder."""
    try:
        if not os.path.exists("dist_tests"):
            os.makedirs("dist_tests")

        for filename in os.listdir("."):
            if filename.endswith(".py"):
                shutil.copy(filename, os.path.join("dist_tests", filename))
    except Exception as e:
        print(f"Error occurred while moving Python files to dist_test folder: {e}")
        raise

def copy_readme_to_share_doc():
    """Copy Readme.md to share/doc/ShieldAI_Assignment directory."""
    try:
        if not os.path.exists("dist/usr/share/doc/ShieldAI_Assignment"):
            os.makedirs("dist/usr/share/doc/ShieldAI_Assignment")

        shutil.copy("../Readme.md", "dist/usr/share/doc/ShieldAI_Assignment")
    except Exception as e:
        print(f"Error occurred while copying README.md to share/doc/ShieldAI_Assignment directory: {e}")
        raise

def copy_readme_to_share_doc_dist_test():
    """Copy Readme.md to share/doc/ShieldAI_Assignment directory."""
    try:
        if not os.path.exists("dist_test/usr/share/doc/ShieldAI_Assignment"):
            os.makedirs("dist_test/usr/share/doc/ShieldAI_Assignment")

        shutil.copy("../Readme.md", "dist_test/usr/share/doc/ShieldAI_Assignment")
    except Exception as e:
        print(f"Error occurred while copying README.md to share/doc/ShieldAI_Assignment directory: {e}")
        raise

def create():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Create Python executable and Debian package",
        epilog="If no option is provided, the script will not perform any action."
    )
    parser.add_argument("-e", "--executable", action="store_true", help="Create Python executable")
    parser.add_argument("-d", "--deb", action="store_true", help="Create Debian package")
    parser.add_argument("-t", "--test-deb", action="store_true", help="Create test Debian package with test files")
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error("Please specify at least one option: -e/--executable, -d/--deb, -t/--test-deb")

    if args.executable:
        copy_python_files_to_dist()
        create_python_executable()
    
    if args.deb:
        copy_python_files_to_dist()
        copy_readme_to_share_doc()
        create_deb_package()

    if args.test_deb:
        copy_python_files_to_dist_test()
        copy_readme_to_share_doc_dist_test()
        create_deb_test_package()

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        parser = argparse.ArgumentParser(description="Usage:")
        parser.print_help()
        sys.exit(0)
    create()