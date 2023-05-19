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
    print(f'data: {data}')
    # if len(data) < 2 and binary starts with anything other than 0,
    # return false
    if len(data) < 2:
        print('single integer in data')
        return True if data[0] <= 128 else False
    # otherwise, check that the bytes most significant bits rules hold
    i = 0
    while i < len(data):
        # get number of bytes and if 1 and starts with 1 return false
        bits = bin(data[i])
        if bits[2:].find('0') == -1 and len(bits) - 2 == 8:
            print('No zeros in str: ', bits)
            return False
        bNum = bits[2:].find('0') + 2 - bits.find('1') if len(bits) - 2 > 7 else 1
        print(f'{bits}: {bNum}')
        if bNum > 4 or (bNum == 1 and len(bits) - 2 == 8):
            print('more than 4bytes or invalid 1 byte character')
            return False
        # depending on number of bytes, check rules hold
        # check that each following byte starts with `10`
        x = 1
        while x < bNum:
            if x + i >= len(data) or not (len(bin(data[i + x])) - 2 == 8 and
                    (bin(data[i + x])[2:4] == '10')):
                # print(f'next byte check failed - {data[i + x]} -> {bin(data[i + x])}')
                print(f'next byte check failed')
                return False
            print(f'x is {x}')
            x += 1
        # skip to next character (how?)
        # print(f'dealt with {data[i]} at idx {i} and {bNum} bytes. We move on to {data[i + bNum]} at idx {i + bNum - 1}')
        i += bNum

    return True
