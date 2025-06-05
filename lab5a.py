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

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
