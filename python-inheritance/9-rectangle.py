#!/usr/bin/python3
"""Rectangle with area and str."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with width and height."""

    def __init__(self, width, height):
        """Set dimensions."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def __str__(self):
        """Return string form."""
        return f"[Rectangle] {self.__width}/{self.__height}"
