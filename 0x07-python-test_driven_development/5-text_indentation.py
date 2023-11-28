#!/usr/bin/python3
"""Module text_indentation method."""


def text_indentation(text):
    """Method for print with adding 2 new lines after '.','?',':' chars.

    Args:
        text (str): The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for st in ".?:":
        text = (st + "\n\n").join(
            [line.strip(" ") for line in text.split(st)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
