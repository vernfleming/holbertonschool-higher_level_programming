#!/usr/bin/python3
"""Rectangle class from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with width and height."""

    def __init__(self, width, height):
        """Validate and set dimensions."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
