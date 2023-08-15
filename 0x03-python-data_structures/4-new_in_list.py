#!/usr/bin/python3
# 4-new_in_list_rewritten.py

def new_in_list(my_list, idx, element):
	"""Replace an element in a copied list at a specified position."""
		if idx < 0 or idx >= len(my_list):
			return my_list

			copied_list = my_list.copy()
	copied_list[idx] = element
	return copied_list

