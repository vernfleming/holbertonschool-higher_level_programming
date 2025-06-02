#!/usr/bin/python3
"""Writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a file and return number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
