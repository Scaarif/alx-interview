#!/usr/bin/python3
""" Checks that a data set is a valid utf-8 encoding """


def validUTF8(data):
    """ returns true if data reps a valid utf-8 encoding
        and false otherwise.
        Args:
            data - an array of integers
        Of Note (borrowed from leetCode):
            A character in UTF8 can be 1 to 4 bytes long, subject
            to the following rules;
            - for a 1-byte character, the first bit is a `0`,
            followed by its unicode code
            - for an n-bytes character, the first n bits are
            all `1`s, the n+1 bit is `0` followed by (n - 1)
            bytes with most significant 2 bits being `10`.
        Constraints:
            - 1 <= data.length <= 2 * 10**4
            - 0 <= data[i] <= 255
    """
    # if len(data) < 2 and binary starts with anything other than 0,
    # return false
    if data is None:
        return True
    if len(data) < 2:
        return True if len(data) == 0 or data[0] < 128 else False
    # otherwise, check that the bytes most significant bits rules hold
    i = 0
    while i < len(data):
        # get number of bytes and if 1 and starts with 1 return false
        bits = bin(data[i])
        # if a character is all `1`s
        if bits[2:].find('0') == -1 and len(bits) - 2 == 8:
            return False
        bNum = bits[2:].find('0') + 2 - \
            bits.find('1') if len(bits) - 2 > 7 else 1
        if bNum > 4 or (bNum == 1 and len(bits) - 2 == 8):
            return False
        # depending on number of bytes, check rules hold
        # check that each following byte starts with `10`
        x = 1
        while x < bNum:
            if not (len(bin(data[i + x])) - 2 == 8 and
                    (bin(data[i + x])[2:4] == '10')):
                return False
            x += 1
        # skip to next character (how?)
        i += bNum

    return True