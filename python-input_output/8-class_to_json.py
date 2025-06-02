#!/usr/bin/python3
"""Returns the dictionary representation of an object."""


def class_to_json(obj):
    """Return the dictionary description of obj."""
    return obj.__dict__
