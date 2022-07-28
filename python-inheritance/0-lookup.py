#!/usr/binpython3
"""Defines an object's characteristic lookup function."""


def lookup(obj):
    """Return a list of the object's available Characteristic."""
    return (dir(obj))
