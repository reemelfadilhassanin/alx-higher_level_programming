#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some of basic info about Python lists.
 * @p: python list object.
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		 PyObject *item = PyList_GetItem(p, i);
        const char *type_name = item->ob_type->tp_name;
        printf("Element %d: %s\n", i, type_name);
	}
}
