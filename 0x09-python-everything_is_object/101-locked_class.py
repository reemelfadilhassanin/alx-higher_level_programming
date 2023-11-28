#!/usr/bin/python3
"""locked class modules."""


class LockedClass:
    """
    This class prevent user from dynamically creating new instance attributes,
    except attribute is called first_name.
    """

    __slots__ = ["first_name"]
