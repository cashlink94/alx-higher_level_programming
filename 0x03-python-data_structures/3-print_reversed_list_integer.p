#!/usr/bin/python3
# 3-print_reversed_list_integer_rewritten.py

def print_reversed_list_integer(my_list=[]):
        """Print integers from a list in reverse order."""
                if isinstance(my_list, list):
                        reversed_list = my_list[::-1]
                        for num in reversed_list:
                        print("{:d}".format(num))

