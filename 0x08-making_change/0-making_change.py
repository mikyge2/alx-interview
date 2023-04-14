#!/usr/bin/python3
""" Making change in linear complexity"""


def makeChange(coins, total):
    """ Bottom up """
    temp = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp += total // coin
            total = total % coin

    return temp if total == 0 else -1
