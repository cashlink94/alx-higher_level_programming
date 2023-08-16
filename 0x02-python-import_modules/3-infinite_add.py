#!/usr/bin/python3

"""
Script: Sum of Command-line Arguments
Description: This script calculates and prints the sum of all provided command-line arguments.
"""

if __name__ == "__main__":
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))

