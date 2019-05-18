# -*- coding: utf8 -*-

__author__ = "polarbear08"
__date__ = "19 May 2019"


def gauss_jordan(matrix):
    """Return Gauss Jordan standard form of the input matrix

    Args:
        matrix: 2 dimension matrix

    Returns:
        matrix: Gauss Jordan standard form of input matrix

    """
    row, col = matrix.shape
    for ri in range(row):
        if not contain_nonzero(ri):
            break

        matrix = normalize_matrix(matrix)
        pivot_row_idx = choose_pivot(matrix, ri)
        matrix = exchange_rows(matrix, ri, pivot_row_idx)
        matrix = make_othercol_zero(matrix, ri)

    return matrix