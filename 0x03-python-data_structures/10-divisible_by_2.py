def divisible_by_2(my_list=[]):
	"""Identify if elements in a list are divisible by 2."""
		divisibility_flags = [num % 2 == 0 for num in my_list]
		return divisibility_flags

