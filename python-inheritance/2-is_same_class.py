#!/usr/bin/python3
"""A function that sees if object is exactly same as class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly a_class; else False."""
    return type(obj) is a_class
