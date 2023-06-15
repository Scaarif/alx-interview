#!/usr/bin/python3
""" Calculates the number of coins that satisfy a certain total given """


def makeChange(coins, total):
    """ returns the number of coins calculated,
        0 if total is 0 and -1 if the total cannot be satisfied
        by the available denominations `coins` where:
        Args:
            coins - an array of coin denominations available
            total - the amount to be satisfied by the coins
    """
    # make a copy of the coins
    count = 0
    c_coin = max(coins) if len(coins) else total
    new = coins[:]
    # print('coin: ', c_coin, ' -> ', coins)
    while len(new) or c_coin <= total > 0 and len(new):
        count += total // c_coin
        total = total % c_coin
        idx = new.index(c_coin)
        new = new[:idx] + new[idx + 1:]
        c_coin = max(new) if len(new) else total
        # print('new: ', new, ' and max: ', c_coin, ' total left ', total)
    return count if total == 0 else -1
