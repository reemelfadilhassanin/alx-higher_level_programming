#!/usr/bin/python3
"""Add integres number."""


def add_integer(a, b=98):
    """Function to add two int/float num.

        Args:
                a (int, float): first int num
                b (int, float): seconed int number. Defaults to 98.

        Raises:
                TypeError: a must be an integer
                TypeError: b must be an integer

        Returns:
                int: int number z = a +b
        """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')
    else:
        z = int(a) + int(b)
        return z


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
