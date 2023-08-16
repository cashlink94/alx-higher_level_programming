#!/usr/bin/python3

"""
This script calculates and prints the sum of 1 and 2 using the 'add' function from the 'add_0' module.
"""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

