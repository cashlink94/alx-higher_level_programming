def delete_at(my_list=[], idx=0):
	"""Remove an element at a specified index from a list."""
		if 0 <= idx < len(my_list):
			del my_list[idx]
			return my_list

