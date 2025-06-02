#!/usr/bin/python3
"""Defines a class MyList that is inherited from list"""


class MyList(list):
    """Prints list elements in ascending order"""

    def print_sorted(self):
        """Print list elements without changing original list"""
        print(sorted(self))
