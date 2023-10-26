#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    A function that surveys for
    utf-8 code
    """
    bytes_count = 0

    for w in data:
        if bytes_count == 0:
            if w >> 5 == 0b110 or w >> 5 == 0b1110:
                bytes_count = 1
            elif w >> 4 == 0b1110:
                bytes_count = 2
            elif w >> 3 == 0b11110:
                bytes_count = 3
            elif w >> 7 == 0b1:
                return False
        else:
            if w >> 6 != 0b10:
                return False
            bytes_count -= 1
    return bytes_count == 0
