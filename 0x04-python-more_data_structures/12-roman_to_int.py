#!/usr/bin/python3

def to_subtract(list_num):
    total = 0
    max_num = max(list_num)

    for num in list_num:
        if max_num > num:
            total += num

    return max_num - total


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(rom_n.keys())

    num = 0
    last_num = 0
    num_list = [0]

    for ch in roman_string:
        for r_num in keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_num:
                    num += to_subtract(num_list)
                    num_list = [rom_n.get(ch)]
                else:
                    num_list.append(rom_n.get(ch))

                last_num = rom_n.get(ch)

    num += to_subtract(num_list)

    return num

