#!/usr/bin/env python3
"""Defines a text file reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
