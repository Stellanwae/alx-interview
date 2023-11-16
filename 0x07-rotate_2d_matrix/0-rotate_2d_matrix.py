#!/usr/bin/python3

"""Func rotates matrix to 90 deg"""


def rotate_2d_matrix(matrix):
    """gives 90 deg matrix"""

    edited_matrix = matrix.copy()
    matrix.clear()

    edited_matrix.reverse()

    for i in range(len(edited_matrix)):
        matr_row = [element[i] for element in edited_matrix]
        matrix.append(matr_row)