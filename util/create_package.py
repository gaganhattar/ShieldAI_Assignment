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

# This is for py not to generate __pycache__, so that the files can be uninstalled properly
sys.dont_write_bytecode = True 

def create_python_executable():
    """Create Python executable using pyinstaller."""
    try:
        subprocess.run(["pyinstaller", "--onefile", "../fileOperations/fileOperations_cmd.py"], check=True)
        dist_bin_path = "dist/usr/local/bin"
        if not os.path.exists(dist_bin_path):
            os.makedirs(dist_bin_path)
            shutil.copy("dist/fileOperations_cmd", "../bin")
            shutil.move("dist/fileOperations_cmd", dist_bin_path)

            print("build/ and dist/ folders created, needed for creating debian package !!")
            print("fileOperations_cmd executable generated in dist/ and bin/ folder, try executing it!!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating Python executable: {e}")
        raise

def create_deb_package():
    """Create deb package using dpkg-deb."""
    try:
        dist_bin_path = "dist/usr/local/bin/fileOperations_cmd"
        if not os.path.exists(dist_bin_path):
            create_python_executable()
        
        package_name = "shieldai.assignment"
        version      = "1.0"
        output_dir   = "dist"
        deb_name     = f"{package_name}_{version}_all.deb"
                    
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
                
        # Build the package
        subprocess.run(["dpkg-deb", "--build", output_dir, deb_name], check=True)
        print("shieldai_assignment.1.0_all.deb created")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating Debian package: {e}")
        raise

def create_deb_test_package():
    """Create deb test package including all test files located in ./unit_tests folder."""
    try:
        
        package_name = "shieldai.assignment.tests"
        version = "1.0"
        output_dir = "dist"
        deb_name = f"{package_name}_{version}_all.deb"

        dist_bin_path = "dist/usr/local/bin/fileOperations_cmd"
        if not os.path.exists(dist_bin_path):
            create_python_executable()

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


        # Build the package
        subprocess.run(["dpkg-deb", "--build", output_dir, deb_name], check=True)
        print(f"{deb_name} is created")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating test Debian package: {e}")
        raise

def copy_python_files_to_dist():
    """Move all Python files to dist folder."""
    try:
        dist_lib_path = "dist/opt/shieldai_assignment/lib"
        if not os.path.exists(dist_lib_path):
            os.makedirs(dist_lib_path)

        for filename in os.listdir("../fileOperations"):
            if filename.endswith(".py") and filename != "__init__.py":
                file_path = os.path.join("../fileOperations", filename)
                shutil.copy(file_path, dist_lib_path)
    except Exception as e:
        print(f"Error occurred while moving Python files to dist folder: {e}")
        raise

def copy_python_files_to_dist_test():
    """Move all test Python files to dist folder."""
    try:
        dist_test_folder = "dist/opt/shieldai_assignment/tests";
        if not os.path.exists(dist_test_folder):
            os.makedirs(dist_test_folder)

        for filename in os.listdir("../unit_tests"):
            if filename.endswith(".py") and filename != "__init__.py":
                test_file_path = os.path.join("../unit_tests", filename)
                shutil.copy(test_file_path, os.path.join(dist_test_folder, filename))

        for filename in os.listdir("./functional_tests"):
            if filename.endswith(".py")  and \
               filename != "__init__.py" and \
               filename != "test_pkg_install_uninstall.py":
                test_file_path = os.path.join("./functional_tests", filename)
                shutil.copy(test_file_path, os.path.join(dist_test_folder, filename))
        unit_test_script = "../unit_tests/run_all_unit_tests.sh";
        os.chmod(unit_test_script, 0o777)
        shutil.copy(unit_test_script, dist_test_folder)
                
    except Exception as e:
        print(f"Error occurred while moving Python files to dist_test folder: {e}")
        raise

def copy_readme_to_share_doc():
    """Copy Readme.md to share/doc/shieldai_assignment directory."""
    try:
        dist_doc_folder = "dist/opt/shieldai_assignment/doc";
        if not os.path.exists(dist_doc_folder):
            os.makedirs(dist_doc_folder)

        shutil.copy("../Readme.md", dist_doc_folder)
    except Exception as e:
        print(f"Error occurred while copying README.md to share/doc/shieldai_assignment directory: {e}")
        raise

def cleanup_build():
    """ Delete any prev build contents"""
    if os.path.exists("dist"):
        shutil.rmtree("dist")

    if os.path.exists("build"):
        shutil.rmtree("build")

    if os.path.exists("fileOperations_cmd.spec"):
        os.remove("fileOperations_cmd.spec")

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
        #copy_python_files_to_dist()
        create_python_executable()
    
    if args.deb:
        cleanup_build();
        copy_python_files_to_dist()
        copy_readme_to_share_doc()
        create_deb_package()
        cleanup_build();

    if args.test_deb:
        cleanup_build();
        copy_python_files_to_dist()
        copy_python_files_to_dist_test()
        copy_readme_to_share_doc()
        create_deb_test_package()
        cleanup_build();

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        parser = argparse.ArgumentParser(description="Usage:")
        parser.print_help()
        sys.exit(0)
    create()