import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPyList.so')

# Set argument types for the function
lib.print_python_list_info.argtypes = [ctypes.py_object]

# Create a Python list
python_list = ['hello', 'World']

# Display information about the list
lib.print_python_list_info(python_list)

# Modify the list
	del python_list[1]
lib.print_python_list_info(python_list)

	python_list = python_list + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(python_list)

	python_list = []

# Display information about an empty list
lib.print_python_list_info(python_list)

# Append elements to the list
	python_list.append(0)
	lib.print_python_list_info(python_list)
	python_list.append(1)
	python_list.append(2)
	python_list.append(3)
python_list.append(4)

# Display information after appending elements
lib.print_python_list_info(python_list)

# Remove the last element from the list
	python_list.pop()
lib.print_python_list_info(python_list)

