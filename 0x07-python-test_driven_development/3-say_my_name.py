#!/usr/bin/python3
"""Say_my_name module."""


def say_my_name(first_name, last_name=""):
    """This function display first and last name.

    Args:
            first_name (str): first name.
            last_name (str): last name.

    Raises:
            TypeError: If first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
