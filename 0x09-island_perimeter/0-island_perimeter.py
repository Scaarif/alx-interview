#!/usr/bin/python3
""" Calculates the perimeter of an island described in a grid """


def island_perimeter(grid):
    """ returns the calculated perimeter """
    perimeter = 0
    # grid can't have a length larger than 100
    if len(grid) <= 100:
        # loop through each row and column except first and last
        for index, row in enumerate(grid):
            # for each col, check adjacent cols (top, bottom, left and right)
            if 1 <= index <= len(grid) - 2:
                for idx, col in enumerate(row):
                    # only add 1 if the adjacent is 0 and the current, 1
                    if 1 <= idx <= len(row) - 2 and col:
                        # left and right respectively (same row)
                        perimeter += 1 if not row[idx - 1] else 0
                        perimeter += 1 if not row[idx + 1] else 0
                        # top and bottom respectively (same col)
                        perimeter += 1 if not grid[index - 1][idx] else 0
                        perimeter += 1 if not grid[index + 1][idx] else 0

    return perimeter
