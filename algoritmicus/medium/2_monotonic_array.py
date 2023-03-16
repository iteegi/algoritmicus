"""Monotonic array algorithm."""

from typing import List


def is_monotonic(array: List[int]) -> bool:
    """Сheck if the array is monotonous.

    O(n) time | O(1) space

    :param array: Array of values.
    :type array: List[int]
    :return: Is the array monotonic?
    :rtype: bool
    """
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False

    return is_non_decreasing or is_non_increasing


if __name__ == '__main__':
    arrs = [[1, 2, 9],
            [1, 2, -1],
            [-11, -2, -1],
            [-1, -5, -100]]

    for arr in arrs:
        print(is_monotonic(arr))
