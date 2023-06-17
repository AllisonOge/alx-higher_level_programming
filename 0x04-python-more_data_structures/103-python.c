#include <Python.h>

/**
 * print_python_list - 
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	/* get size and allocated field of the list */
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - 
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *byteObj;
	Py_ssize_t size, i;
	char *data;

	printf("[*] bytes object info\n");
	/* 
	 * print a max of 10 bytes for the first X bytes
	 * if p is not a valid PyBytesObject, print the error
	 * message [ERROR] Invalid Bytes Object
	 */
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	byteObj = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", byteObj->ob_sval);

	if (size > 10)
		size = 10;
	data = byteObj->ob_sval;
	printf("  first %zd bytes:", size);
	for (i = 0; i < size; ++i)
		printf("  %02x", (unsigned char)data[i]);
	printf("\n");
}
