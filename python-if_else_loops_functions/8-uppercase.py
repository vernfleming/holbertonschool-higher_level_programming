#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line"""
    for c in str:
        if 'a' <= c <= 'z':
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
