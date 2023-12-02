#!/usr/bin/python3
"""Prints text with 2 newlines after characters '.', '?' and ':'

Prototype: def text_indentation(text):
- text must be a string, otherwise raise a TypeError 
  exception with the message text must be a string
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module
"""

def text_indentation(text):
    """Print text with 2 newlines after '.', '?', and ':'

    Args:
        text: string to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    lines = [line.strip() for line in text.split("\n")]
    print("\n\n".join(lines), end="")
