# Introduction

This document provides the information of about the usage of each file o perform file operations, such as Create, Delete, Copy, Combine

# Modular Python3 Filesystem Structure:
File_Operation/
│
├── create_file.py
├── copy_file.py
├── combine_files.py
├── delete_file.py
├── create_package.py
├── main.py
├── tests/
│   ├── test_create_file.py
│   ├── test_copy_file.py
│   ├── test_combine_files.py
│   ├── test_delete_file.py
│   └── test_main.py
│
└── README.md


## File Structure

- **create_file.py**: Script to create a file with optional text.
- **copy_file.py**: Script to copy a file.
- **combine_files.py**: Script to combine two files into a third.
- **delete_file.py**: Script to delete a file.
- **main.py**: Main script with CLI options to call modules for file operations.
- **tests/**: Directory containing unit tests for each file operation.
- **create_package.py**: Script to create Python executable and Debian package.
- **README.md**: This file.

## How to 
python create_file.py new_file.txt -t "optional text"
python copy_file.py source_file.txt destination_file.txt
python combine_files.py file1.txt file2.txt output.txt
python delete_file.py file_to_delete.txt

python main.py --help
python create_file.py --help
python copy_file.py --help
python combine_files.py --help
python delete_file.py --help

## How to Use

1. **Running Main Script**:
   - Run `python main.py --help` to see available commands and options.
   - Example: `python main.py create new_file.txt -t "optional text"`

2. **Running Tests**:
   - Navigate to the `tests` directory.
   - Run `python -m unittest` to execute all unit tests.

3. **Creating Python Executable and Debian Package**:
   - Run `python create_package.py` to generate Python executable and Debian package.

## Create_package
Place it in the same directory as your generated Python files.
Run the script with -h or --help option to see available options and their descriptions.
Use -e or --executable option to create the Python executable.
Use -d or --deb option to create the deb package.
The script will create a dist folder if it doesn't exist and move all Python files into it before creating the executable or deb package.

Here are step-by-step instructions in Markdown format on how to install the Debian package `File_Operations_AIShield` on a Bash terminal and how to use `fileOperations_cmd` with all options:

### Installing Debian Package

1. **Download the Debian Package**: Ensure that you have the `File_Operations_AIShield.deb` Debian package downloaded to your system.

2. **Open Terminal**: Open a Bash terminal on your system.

3. **Navigate to Directory**: Navigate to the directory where the `File_Operations_AIShield.deb` package is located.

   ```bash
   cd /path/to/directory
   ```

4. **Install the Package**: Use the `dpkg` command to install the Debian package.

   ```bash
   sudo dpkg -i File_Operations_AIShield.deb
   ```

5. **Verify Installation**: After installation, you can verify that the package is installed by listing installed packages.

   ```bash
   dpkg -l | grep File_Operations_AIShield
   ```

6. **Expectations After Installation**: Upon successful installation, you should see confirmation messages indicating that the package has been installed. The package should now be available for use.

### Using `fileOperations_cmd` with Options

1. **Open Terminal**: Open a Bash terminal on your system.

2. **Navigate to Directory**: Navigate to the directory where `fileOperations_cmd` executable is located.

   ```bash
   cd /path/to/directory
   ```

3. **Run the Executable**: Execute the `fileOperations_cmd` executable with appropriate options.

   ```bash
   ./fileOperations_cmd --help
   ```

   This command will display the available options and their descriptions.

4. **Perform File Operations**: Use the `fileOperations_cmd` executable to perform desired file operations such as creating a file, copying a file, combining files, or deleting a file.

   ```bash
   ./fileOperations_cmd create new_file.txt -t "optional text"
   ./fileOperations_cmd copy source_file.txt destination_file.txt
   ./fileOperations_cmd combine file1.txt file2.txt output.txt
   ./fileOperations_cmd delete file_to_delete.txt
   ```

   Replace the arguments with appropriate filenames and options based on the desired operation.

5. **Expectations After Command Execution**: After executing each command, you should expect to see output indicating the success or failure of the operation. For example, when creating a file, you should expect to see a confirmation message indicating that the file has been created. Similarly, for other operations, you should expect to see relevant confirmation messages or error messages in case of failure.

Following these steps should allow you to install the Debian package `File_Operations_AIShield` and use the `fileOperations_cmd` executable with all available options on a Bash terminal.

After installing the `File_Operations_AIShield` Debian package, you can expect the following file structure:

```
/
└── usr
    ├── bin
    │   └── fileOperations_cmd
    └── share
        └── doc
            └── File_Operations_AIShield
                ├── create_file.py
                ├── copy_file.py
                ├── combine_files.py
                ├── delete_file.py
                ├── main.py
                └── create_package.py
```

Explanation of the file structure:
- **`/usr/bin/fileOperations_cmd`**: This is the executable file created from the `main.py` script. It's placed in the `/usr/bin` directory to make it globally accessible.
- **`/usr/share/doc/File_Operations_AIShield`**: This directory contains documentation related to the `File_Operations_AIShield` package.
  - **`create_file.py`**: Python script for creating a file.
  - **`copy_file.py`**: Python script for copying a file.
  - **`combine_files.py`**: Python script for combining two files into a third.
  - **`delete_file.py`**: Python script for deleting a file.
  - **`main.py`**: Main Python script that orchestrates the file operations.
  - **`create_package.py`**: Python script for creating a Python executable and deb package.

This file structure ensures that the `fileOperations_cmd` executable is available for use globally, while also providing documentation for the `File_Operations_AIShield` package in the `/usr/share/doc` directory.
