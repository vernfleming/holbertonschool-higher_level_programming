#!/usr/bin/python3
"""Square class from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square using size."""

    def __init__(self, size):
        """Validate and set size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area."""
        return self.__size * self.__size
