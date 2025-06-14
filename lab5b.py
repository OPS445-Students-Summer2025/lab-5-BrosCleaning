#!/usr/bin/env python3
# Author ID: sbashyal

def read_file_string(file_name):
    """
    Takes file_name as string for a file name,
    returns its entire contents as a single string.
    """
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """
    Takes file_name as string for a file name,
    returns its entire contents as a list of lines without newline characters.
    """
    with open(file_name, 'r') as f:
        return [line.rstrip('\n') for line in f]

def append_file_string(file_name, string_of_lines):
    """
    Takes two strings, appends the string_of_lines to the end of the file.
    """
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """
    Takes a file name and a list,
    writes all items from list_of_lines to file, each item as one line.
    """
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Reads data from file_name_read, writes to file_name_write
    adding line numbers at the start of each line in the format: "1:Line text".
    """
    with open(file_name_read, 'r') as fin, open(file_name_write, 'w') as fout:
        for i, line in enumerate(fin, start=1):
            fout.write(f"{i}:{line.rstrip()}\n")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'

    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
