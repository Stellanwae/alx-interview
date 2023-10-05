#!/usr/bin/python3
"""Script to unlock list of lists"""

def canUnlockAll(boxes):
    """This function will take a list of lists and unlock
    content
    """

    keys = [0]
    for key in keys:
        for boxOpener in boxes[key]:
            if boxOpener not in keys and boxOpener < len(boxes):
                keys.append(boxOpener)
    if len(keys) == len(boxes):
        return True
    return False
