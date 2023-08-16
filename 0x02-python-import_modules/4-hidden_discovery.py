#!/usr/bin/python3

"""
Script: Hidden Module Names
Description: This script prints the names defined by the 'hidden_4' module, excluding names starting with '__'.
"""

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)

