#!/usr/bin/python3
"""Check if obj inherits from a_class (not the same class)."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
