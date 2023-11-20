#include <Python.h>

/**
 * print_python_bytes - prints information about Python bytes objects
 * @p: PyObject pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    unsigned long i, size;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %lu\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; i++)
    {
        printf(" %02x", str[i] & 0xFF);
    }
    printf("\n");
}

/**
 * print_python_list - prints information about Python list objects
 * @p: PyObject pointer to a Python object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    unsigned long i, size;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %lu\n", size);
    printf("[*] Allocated = %lu\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %lu: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (PyBytes_Check(PyList_GetItem(p, i)))
            print_python_bytes(PyList_GetItem(p, i));
    }
}

/**
 * print_python_float - prints information about Python float objects
 * @p: PyObject pointer to a Python object
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *float_obj;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    float_obj = (PyFloatObject *)p;
    printf("  value: %f\n", float_obj->ob_fval);
}
