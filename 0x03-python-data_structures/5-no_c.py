#!/usr/bin/python3
# 5-no_c_rewritten.py

def no_c(my_string):
	"""Remove all occurrences of characters 'c' and 'C' from a string."""
		filtered_chars = [char for char in my_string if char.lower() not in ('c', 'C')]
		return "".join(filtered_chars)

