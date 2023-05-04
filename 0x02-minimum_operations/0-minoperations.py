#!/usr/bin/python3
""" Calculates the fewest number of operations needed to result in exactly
    n 'H' characters in a file that starts off with only one 'H' and only
    two possible operations:
    1. Copy All
    2. Paste
"""


def minOperations(n):
    """ returns the calculated minimum number of operations.
        and 0 id n is impossible to achieve
    """
    # keep track current number of 'H' characters (starts at 1)
    count = 1
    ops = 0
    # check that n is valid & at least > 1
    if type(n) != int or n < 2:
        return ops  # 0
    # very first operation'll always be a copy followed by a paste
    count += 1  # count = 2 at this point
    ops += 2  # first copy and paste
    # track the current number of 'H'(s) we'd be pasting
    batch = 1
    # if n > 2, loop until count == n
    while count < n:
        # if n % count == 0, copy batch and paste else paste batch again
        if n % count == 0:
            batch = count  # copy current number of 'H'(s) - the batch
            count += batch  # paste
            ops += 2
        else:
            count += batch
            ops += 1
    return ops
