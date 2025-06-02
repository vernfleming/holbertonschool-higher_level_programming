#!/usr/bin/python3
"""Serialize and deserialize dictionary with XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Save dictionary to XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load dictionary from XML file."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
