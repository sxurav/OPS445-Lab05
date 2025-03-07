#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    try:
        # Attempt to convert both inputs to integers
        number1 = int(number1)
        number2 = int(number2)
        result = number1 + number2
        return result
    except (TypeError, ValueError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    # Test cases
    print(add(10, 5))                          # works
    print(add('10', 5))                        # works
    print(add('abc', 5))                       # exception
    print(add('5', '5'))                       # works after fixing
    print(read_file('seneca2.txt'))           # works
    print(read_file('file10000.txt'))         # exception
