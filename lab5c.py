#!/usr/bin/env python3
# Author ID: sbashyal

def add(number1, number2):
    """
    Add two numbers together, return the result.
    If inputs are strings representing numbers, convert them.
    If error, return 'error: could not add numbers'.
    """
    try:
        n1 = int(number1)
        n2 = int(number2)
        return n1 + n2
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    """
    Read a file, return a list of all lines.
    If error, return string 'error: could not read file'.
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works, expect 15
    print(add('10', 5))                      # works, expect 15
    print(add('abc', 5))                     # exception, expect error message
    print(read_file('seneca2.txt'))          # works if file exists
    print(read_file('file10000.txt'))        # exception, expect error message

