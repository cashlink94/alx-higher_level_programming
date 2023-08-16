#include <stdio.h>
#include <Python.h>

void print_python_bytes_info(PyObject *object) {
	char *data;
	long int size, i, limit;

	printf("[.] bytes object information\n");
	if (!PyBytes_Check(object)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(object))->ob_size;
	data = ((PyBytesObject *)object)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  attempting string: %s\n", data);

	limit = (size >= 10) ? 10 : size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++) {
		if (data[i] >= 0) {
			printf(" %02x", data[i]);
		} else {
			printf(" %02x", 256 + data[i]);
		}
	}

	printf("\n");
}

void print_python_list_info(PyObject *object) {
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = ((PyVarObject *)(object))->ob_size;
	list = (PyListObject *)object;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++) {
		item = ((PyListObject *)object)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item)) {
			print_python_bytes_info(item);
		}
	}
}

