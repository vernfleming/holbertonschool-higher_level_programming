#!/usr/bin/python3
"""Module for basic JSON serialization and deserialization."""

import json


def serialize_and_save_to_file(data, filename):
    """Save a dictionary as JSON to a file."""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a dictionary from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
