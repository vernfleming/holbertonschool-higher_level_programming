#!/usr/bin/python3
"""BaseGeometry with area method."""


class BaseGeometry:
    """Geometry base class."""

    def area(self):
        """Raise not implemented error."""
        raise Exception("area() is not implemented")
