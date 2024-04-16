#!/usr/bin/python3
"""Module with the method lookup."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
