#!/usr/bin/python3
""" Given a 2D Mtraix, rotates it (in place) 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """ rotates (mutates) the matrix through 90 degrees """
    looper = []
    # make a deep copy of the matrix
    for row in matrix:
        looper.append(row[:])
    row = len(matrix[0]) - 1
    # mutate matrix (column, reversed becomes the row)
    for col in range(len(matrix)):
        i = 0
        while row >= 0:
            # print(matrix[col][i], ' <- ', looper[row][col])
            matrix[col][i] = looper[row][col]
            i += 1
            row -= 1
        row = len(matrix) - 1
