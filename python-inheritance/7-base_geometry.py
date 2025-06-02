#!/usr/bin/python3
"""BaseGeometry with validation."""


class BaseGeometry:
    """Geometry base class."""

    def area(self):
        """Raise not implemented error."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is a positive int."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
