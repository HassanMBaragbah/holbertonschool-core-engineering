#!/usr/bin/env python3
"""Defines a function for writing text to a file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns character count.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string content to write into the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
