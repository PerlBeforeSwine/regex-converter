import os
import requests
from flask import redirect, render_template
from functools import wraps

''' Display an apology to the user '''
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def convert1(text):
    """Convert to regex - first letter case insensitive"""

    # Sanitize input to ensure it's alphanumeric + spaces
    text = list(text)
    for index in range(len(text)):
        if not text[index].isalpha():
            if not text[index] == " " and not text[index] == "'":
                text[index] = '*'

    text[0] = '[' + text[0].upper() + text[0].lower() + ']'

    output = ""

    for char in text:
        if char != "*":
            output += char

    return output


def convert2(text):
    """Convert to regex - first letter in each word case insensitive"""

    # Sanitize input to ensure it's alphanumeric + spaces
    text = list(text)
    for index in range(len(text)):
        if not text[index].isalpha():
            if not text[index] == " " and not text[index] == "'":
                text[index] = '*'

    output = ""

    for char in text:
        if char != "*":
            output += char

    output = output.split()

    for index in range(len(output)):
        output[index] = list(output[index])
        output[index][0] = '[' + output[index][0].upper() + output[index][0].lower() + ']'
        output[index] = ''.join(output[index])

    output = ' '.join(output)

    return output


def convert3(text):
    """All letters case insensitive, retain spaces"""
    # Sanitize input to ensure it's alphanumeric + spaces
    text = list(text)
    for index in range(len(text)):
        if not text[index].isalpha():
            if not text[index] == " " and not text[index] == "'":
                text[index] = '*'

    output = ""

    for char in text:
        if char != "*":
            if char.isalpha():
                output += "[" + char.upper() + char.lower() + "]"
            else:
                output += char

    return output


def convert4(text):
    """First of each word case insensitive, all words as OR"""
    # Sanitize input to ensure it's alphanumeric + spaces
    text = list(text)
    for index in range(len(text)):
        if not text[index].isalpha():
            if not text[index] == " " and not text[index] == "'":
                text[index] = '*'

    output = ""

    for char in text:
        if char != "*":
            output += char

    output = output.split()

    for index in range(len(output)):
        output[index] = list(output[index])
        output[index][0] = '[' + output[index][0].upper() + output[index][0].lower() + ']'
        output[index] = ''.join(output[index])

    output = '|'.join(output)

    return output


def convert5(text):
    """All case insensitive, all ORs"""
    # Sanitize input to ensure it's alphanumeric + spaces
    text = list(text)
    for index in range(len(text)):
        if not text[index].isalpha():
            if not text[index] == " " and not text[index] == "'":
                text[index] = '*'

    output = ""

    for char in text:
        if char != "*":
            if char.isalpha():
                output += "[" + char.upper() + char.lower() + "]"
            else:
                output += char

    output = output.split()

    output = '|'.join(output)

    return output
