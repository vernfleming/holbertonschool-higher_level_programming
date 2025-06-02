#!/usr/bin/python3
"""Reads and prints the contents of a UTF8 text file."""


def read_file(filename=""):
    """Print the content of a text file to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
