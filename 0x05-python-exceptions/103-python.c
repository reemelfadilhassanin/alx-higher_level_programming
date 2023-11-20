#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
/**
 * print_python_bytes - function that display python float objects
 * @p: pointer to Python oject 
 */
void print_python_bytes(PyObject *p)
{
	size_t byte, i;
	char *s;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)(p));
    byte = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", byte, s);
	byte >= 10 ? byte = 10 : byte++;
	printf("  first %ld bytes: ", byte);
	for (i = 0; i < byte - 1; i++)
		printf("%02hhx ", s[i]);
	printf("%02hhx\n", s[i]);
}
/**
 * print_python_float - function to display python objects list
 * @p: pointer point to python object
 */
void print_python_float(PyObject *p)
{
	char *s;
	double float;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	float = (PyFloatObject *)(p);
	s = PyOS_double_to_string(float, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}
/**
 * print_python_list - function to print python objects
 * @p: pointer point to PyObject
 */
void print_python_list(PyObject *p)
{
	PyFloatObject *obj;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    obj = (PyFloatObject *)p;
    printf("  value: %f\n", obj->ob_fval);
}
