#!/usr/bin/python3
""" Determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ Determines if all n boxes (sequential) can be unlocked.
        Args: boxes - a list of lists (lists being the keys in a
                    given box)
    """
    # all closed boxes
    closed = {x: x for x in range(1, len(boxes))}
    valid_keys = [0]  # box already open... no need for checking that key
    locked = len(boxes) - 1  # since the first box is unlocked
    # loop through boxes getting keys (valid) and deleting unlockables
    for index, box in enumerate(boxes):
        # print(f'box: {index} -> {box} with keys: ')
        for key in box:
            # check key is valid, there're locked boxes still & not in own box
            # print(f'{key}, ')
            valid = key not in valid_keys and key < len(boxes)
            if valid and locked and key != index:
                valid_keys.append(key)
                del closed[key]
                locked -= 1
    if not locked:
        return True  # all locks unlocked (locked = 0)
    else:
        return False
