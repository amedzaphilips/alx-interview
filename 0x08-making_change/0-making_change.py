#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to the meet total
        If total is 0 or less, then return 0
        If total cannot be met by any number of coins you have, then return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    Change = 0

    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            Change += 1
        if (total == 0):
            return Change
    return -1
