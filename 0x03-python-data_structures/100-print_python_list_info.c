#include <Python.h>

/**
 * analyze_python_list - Provides essential insights about Python lists.
 * @list_object: A PyObject representing a list.
 */
void analyze_python_list(PyObject *list_object)
{
	int list_size, allocation_size, index;
	PyObject *list_item;

	list_size = Py_SIZE(list_object);
	allocation_size = ((PyListObject *)list_object)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", allocation_size);

	for (index = 0; index < list_size; index++)
	{
		printf("Element %d: ", index);

		list_item = PyList_GetItem(list_object, index);
		printf("%s\n", Py_TYPE(list_item)->tp_name);
	}
}

