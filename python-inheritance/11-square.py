#!/usr/bin/python3
"""Square with custom str."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square using size."""

    def __init__(self, size):
        """Set and validate size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area."""
        return self.__size * self.__size

    def __str__(self):
        """Return string form."""
        return f"[Square] {self.__size}/{self.__size}"
