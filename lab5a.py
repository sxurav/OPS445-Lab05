#!/usr/bin/env python3
# Author ID: Sourav1

def read_file_string(file_name):
    """Reads the file and returns its contents as a single string."""
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

def read_file_list(file_name):
    """Reads the file and returns its contents as a list of lines without new-line characters."""
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def append_file_string(file_name, string_of_lines):
    """Appends the string to the file."""
    try:
        with open(file_name, 'a') as f:
            f.write(string_of_lines)
    except FileNotFoundError:
        return "File not found"

def write_file_list(file_name, list_of_lines):
    """Writes the list of lines to the file."""
    try:
        with open(file_name, 'w') as f:
            for line in list_of_lines:
                f.write(line + '\n')
    except FileNotFoundError:
        return "File not found"

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Copies data from one file to another, adding line numbers to each line."""
    try:
        with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
            line_number = 1
            for line in f_read:
                f_write.write(f"{line_number}:{line}")
                line_number += 1
    except FileNotFoundError:
        return "File not found"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))  # Print the file contents as a string
    print(read_file_list(file_name))    # Print the file contents as a list
