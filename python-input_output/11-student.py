#!/usr/bin/python3
"""Student class with serialization and reload."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict representation based on attrs filter."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes using json dict."""
        for key, value in json.items():
            setattr(self, key, value)
