def print_matrix_integer(matrix=[[]]):
	"""Print a matrix of integers."""
		for row in matrix:
		for col_index, col in enumerate(row):
			print("{:d}".format(col), end=" " if col_index != len(row) - 1 else "")
			print()

