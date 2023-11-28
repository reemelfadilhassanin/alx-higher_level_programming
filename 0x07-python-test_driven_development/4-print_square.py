#!/usr/bin/python3
"""Print_squarewith # module."""


def print_square(size):
    """Function for printing a square with #.

    Args:
        size (int): Int size of the square.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for x in range(size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
