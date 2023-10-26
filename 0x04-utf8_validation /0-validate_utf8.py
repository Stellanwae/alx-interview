#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Surveys for utf-8 code
    """
    byte_count = 0

    bin_1 = 1 << 7
    bin_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if byte_count == 0:

            while mask_byte & i:
                byte_count += 1
                mask_byte = mask_byte >> 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False

        else:
            if not (i & bin_1 and not (i & bin_2)):
                return False

        byte_count -= 1

    if byte_count == 0:
        return True

    return False
