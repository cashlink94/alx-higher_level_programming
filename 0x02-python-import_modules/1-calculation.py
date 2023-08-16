#!/usr/bin/python3

"""
Script: Arithmetic Operations
Description: This script performs arithmetic operations on 10 and 5 using functions from the 'calculator_1' module.
"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

