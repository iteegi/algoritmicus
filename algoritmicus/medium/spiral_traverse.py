"""Spiral traverse algorithm."""

from typing import List


Numbers_encountered = List[int]
Matrix = List[List[int]]


def spiral_traverse(matrix: Matrix) -> Numbers_encountered:
    """Return the sequence of encountered numbers.

    The matrix is traversed in a spiral.

    O(n) time | O(n) space.

    The Spiral Matrix problem takes a 2-Dimensional array of N-rows and
    M-columns as an input, and prints the elements of this matrix in
    spiral order.

    The spiral begins at the top left corner of the input matrix, and prints
    the elements it encounters, while looping towards the center of this
    matrix, in a clockwise manner.

    :param matrix: Matrix of numbers.
    :type matrix: Matrix
    :return: sequence of encountered numbers.
    :rtype: Numbers_encountered
    """
    result: Numbers_encountered = []
    _spiral_fill(matrix,
                 0,
                 len(matrix) - 1,
                 0,
                 len(matrix[0]) - 1,
                 result)
    return result


def _spiral_fill(matrix: Matrix,
                 start_row: int,
                 end_row: int,
                 start_col: int,
                 end_col: int,
                 result: Numbers_encountered) -> None:
    """Append the encountered numbers to the sequence."""

    if start_row > end_row or start_col > end_col:
        return

    for col in range(start_col, end_col + 1):
        result.append(matrix[start_row][col])

    for row in range(start_row + 1, end_row + 1):
        result.append(matrix[row][end_col])

    for col in reversed(range(start_col, end_col)):
        result.append(matrix[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
        result.append(matrix[row][start_col])

    _spiral_fill(matrix, start_row + 1, end_row - 1,
                 start_col + 1, end_col - 1, result)


if __name__ == '__main__':
    array = [[1, 2, 3, 4],
             [12, 13, 14, 5],
             [11, 16, 15, 6],
             [10, 9, 8, 7]]

    res = spiral_traverse(array)

    print(res)
