#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
/**
 * print_python_bytes - function to print python list object
 * @p: pointer to point to PyObject 
 */
void print_python_bytes(PyObject *p)
{
	size_t byte, i;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)(p))->ob_sval, byte = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", byte, s);
	byte >= 10 ? byte = 10 : byte++;
	printf("  first %ld bytes: ", byte);
	for (i = 0; i < byte - 1; i++)
		printf("%02hhx ", s[i]);
	printf("%02hhx\n", s[i]);
}
/**
 * print_python_float - function to print python objects
 * @p: pointer to point toPyObject p
 */
void print_python_float(PyObject *p)
{
	char *str;
	double f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_list - function that print python object list
 * @p: pointer to point to  PyObject 
 */
void print_python_list(PyObject *p)
{
	size_t a, size, i;
	const char *t;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	a = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, a);
	for (i = 0; i < size; i++)
	{
		t = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, t);
		!strcmp(t, "bytes") ? print_python_bytes(list->ob_item[i]) : (void)t;
		!strcmp(t, "float") ? print_python_float(list->ob_item[i]) : (void)t;
	}
}
