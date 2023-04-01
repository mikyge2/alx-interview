#!/usr/bin/python3
""" Checks to see if all 'boxes' in the array can be 'unlocked' """


def canUnlockAll(boxes):
    """ Algorithm """
    if not boxes:
        return False
    if type(boxes) is not list:
        return False

    open = [0]
    for n in open:
        for key in boxes[n]:
            if key not in open and key < len(boxes):
                open.append(key)
    if len(open) == len(boxes):
        return True

    return False
