#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	char *typeName;
	/* get size and allocated field of the list*/
	Py_ssize_t size = PyList_Size(p), i;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}
