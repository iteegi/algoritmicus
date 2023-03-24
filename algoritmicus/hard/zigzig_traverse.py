"""ZigZag Traverse algorithm."""

from collections.abc import Sequence


def zigzag_traverse(array: Sequence[Sequence[int]]) -> Sequence[int]:
    """Return a one-dimensional array of all the array's elements in zigzag
    order.

    O(n) time | O(n) space.

    :param array: A two-dimensional array.
    :type array: Sequence[Sequence[int]]
    :return: A one-dimensional array of all the array's elements in zigzag
    order.
    :rtype: Sequence[int]
    """
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    going_down = True

    while not _is_out_of_bounds(row, col, height, width):
        result.append(array[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def _is_out_of_bounds(row: int, col: int, height: int, width: int) -> bool:
    return row < 0 or row > height or col < 0 or col > width


if __name__ == '__main__':
    arr = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],
    ]
    print(zigzag_traverse(arr))
