#!/usr/bin/env python3
# lab5b.py

from lab5a import read_file_string, read_file_list, append_file_string, write_file_list, copy_file_add_line_numbers

def clear_file(file_name):
    """Clears the content of the file."""
    with open(file_name, 'w') as f:
        f.truncate(0)  # Clears the content of the file

def main():
    # Define the file names
    file1 = 'data.txt'
    file2 = 'data_copy.txt'
    file3 = 'data_with_line_numbers.txt'

    # Clear the file before appending new content
    clear_file(file1)

    # Append some new strings to file1
    string1 = "Hello World\nThis is the second line\nThird line\nLast line\n"
    append_file_string(file1, string1)

    # Read the updated file1 and print it
    print("After appending to file1:")
    print(read_file_string(file1))

    # Write a list to file2
    list1 = ['Line 1', 'Line 2', 'Line 3']
    write_file_list(file2, list1)

    # Read and print file2 contents
    print("\nReading file2:")
    print(read_file_list(file2))

    # Copy file1 content to file3, adding line numbers
    copy_file_add_line_numbers(file1, file3)

    # Read and print file3 contents
    print("\nReading file3 (with line numbers):")
    print(read_file_string(file3))

if __name__ == "__main__":
    main()
