# Introduction

File Operations Package is a Python package that provides functionality to perform various file operations such as create, copy, combine, and delete files. The package also contain various unit tests and functional tests to validate code and functionality on the target system. The package was implemented as part of an **interview stage with ShieldAI**.

# How to get code (github)

- **git clone command** : Run command below to create workspace for this code on your computer.
   Run `git clone https://github.com/gaganhattar/ShieldAI_Assignment.git` 
- **Code download**: Download zip file from the "Code" button dropdown at https://github.com/gaganhattar/ShieldAI_Assignment

# Modular Python3 Filesystem Structure:

```
ShieldAI_Assignment
│──File_Operation/
│  │
│  ├── __init__.py
│  ├── create_file.py
│  ├── copy_file.py
│  ├── combine_files.py
│  ├── delete_file.py
│  ├── create_package.py
│  └── fileOperations_cmd.py
│ 
├── unit_tests/
│  ├── __init__.py
│  ├── test_create_file.py
│  ├── test_copy_file.py
│  ├── test_combine_files.py
│  ├── test_delete_file.py
│  ├── test_fileOperations_cmd.py
│  └── run_all_unit_tests.sh
│
├── util/
│  ├── functional_tests
│  │    ├── test_fileOperations_cmd_exe.py
│  │    └── test_pkg_install_uninstall.py
│  │
│  ├── create_package.py
│ 
├── .gtignore
│
└── README.md
```


## File Structure

1. **file_operation**: contains various module files as described below:
- **create_file.py**: Module to create a file with optional text.
- **copy_file.py**: Module to copy a file.
- **combine_files.py**: Module to combine two files into a third.
- **delete_file.py**: Module to delete a file.
- **fileOperations_cmd.py**: Main Module to access CLI options to perform create, copy, delete and combine files operations.
2. **unit_tests**: contains the unit tests for all the modules in **file_operation**
3. **util**: contains scripts to generate the the production and test Debian packages.
- **function_tests/**: 
   - **test_fileOperations_cmd_exe.py**: unit tests to verify **fileOperations_cmd** executable after installation.
   - **test_pkg_install_uninstall.py**: unit tests to verify installation and un-installation of both production and test Debian packages.
- **create_package.py**: Script to create Python executable and Debian package.
4. **.gitignore**: specify certain build or py auto-generated like __pycache__ to not tracked by git and remain untracked for commits.
5. **README.md**: this file, describing the file structure and various utilities build, generate and use the **fileOperations_cmd** executable on commandline.

## Dependancies 

- **python 3.8 or newer**
- **pyinstaller**: This package is needed for generating the executable **fileOperations_cmd**
- **dpkg and dpkg-deb**: Package manager to install and un-install .deb packages, as well building .deb package.

## Installing the production package

- Latest build is available in **util** folder
   - Run `sudo dpkg -i shieldai.assignment_1.0_all.deb`: this will install **fileOperations_cmd** executable in **/usr/local/bin**. The command is readily usable on new terminal launch after the installation. Use `fileOperations_cmd -h`
- Useful commads are:
  `fileOperation_cmd create new_file.txt -t "optional text"`
  `fileOperation_cmd copy source_file.txt destination_file.txt`
  `fileOperation_cmd combine file1.txt file2.txt output.txt`
  `fileOperation_cmd delete file_to_delete.txt ` 
- Installed files:
   - **fileOperations_cmd** in **/usr/local/bin**
   - All modules in **File_Operation** at **/opt/shieldai_assignment/lib**
   - **Readme.md** in **/opt/shieldai_assignment/doc**

## Generating or Building production package

- Although the package is avaialable in **util** folder, it's advisable to build the package at your system. The command to generate package are
   - Change directory to utils `cd utils`
   - Run `python3 create_package.py -d` to generate **shieldai.assignment_1.0_all.deb**

## Installing the test package

- The purpose of this package is running the unit tests and funstional tests on target production environment. The pre-built package is available at **utils** folder.
   - Run `sudo dpkg -i shieldai.assignment.tests_1.0_all.deb`
   - Installed files are:
      - **fileOperations_cmd** in **/usr/local/bin**
      - All modules in **file_Operation** at **/opt/shieldai_assignment/lib**
      - All unit and functional scripts in **unit_tests** and **utils/functiona_tests** at **/opt/shieldai_assignment/tests**
      - **Readme.md** in **/opt/shieldai_assignment/doc**

## Generating or Building test package

- Although the package is avaialable in **util** folder, it's advisable to build the package at your system. The command to generate package are
   - Change directory to utils `cd utils`
   - Run `python3 create_package.py -t` to generate **shieldai.assignment.tests_1.0_all.deb**

## Uninstallation Procedure

1. To uninstall the package, use the following command:                                  
 - `sudo dpkg -r shieldai.assignment` for production package
 - `sudo dpkg -r shieldai.assignment.tests` for test package

## How to Use

1. **Running fileOperations_cmd Script**:
   - Run `python fileOperations_cmd.py --help` to see available commands and options.
   - Example: `python fileOperations_cmd.py create new_file.txt -t "optional text"`
   - see the **fileOperations_cmd.py** file for more commands.

2. **Running `fileOperations_cmd` with Options**:
   - **Navigate to Directory**: Navigate to the directory where `fileOperations_cmd` executable is located, it's in **bin** folder in dev env. After install it should be auto detected on bash terminal.
   - **Run the Executable**: Execute the `fileOperations_cmd` executable with appropriate options. In dev env. prefix fileOperations_cmd with "./". e.g.:
   `./fileOperations_cmd --help`.
   This command will display the available options and their descriptions.

   - **Perform File Operations**: Use the `fileOperations_cmd` executable to perform desired file operations such as creating a file, copying a file, combining files, or deleting a file. In dev. env. commands are:
   
   ```
   ./fileOperations_cmd create new_file.txt -t "optional text"
   ./fileOperations_cmd copy source_file.txt destination_file.txt
   ./fileOperations_cmd combine file1.txt file2.txt output.txt
   ./fileOperations_cmd delete file_to_delete.txt
   ```

   Replace the arguments with appropriate filenames and options based on the desired operation.

3. **Running unit Tests**:
   - Navigate to the `/opt/shieldai.assignment/tests` directory after installing test package or `unit_test` in the development env.
   - Run `run_all_unit_tests.sh` to execute all unit tests.

4. **Running Functional Tests**
   - Navigate to the `/opt/shieldai.assignment/tests` directory after installing test package
   - Run `python3 -m unittest test_fileOperations_cmd_exe.py` to test **fileOperations_cmd** executable
   - To test install and un-install for test and production package. Navigate to `util/functional_tests' and 
   - Run `python3 -m unittest test_pkg_install_uninstall.py`


