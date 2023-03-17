"""Move element to end algorithm."""

from typing import List


Array = List[int]


def move_element_to_end(array: Array, to_move: int) -> Array:
    """Move the given number to the end of the array.

    :param array: Array of integers.
    :type array: Array
    :param to_move: The number to be moved to the end of the array.
    :type to_move: int
    :return: An array of integers with the given element moved to the end.
    :rtype: Array
    """
    i = 0
    j = len(array) - 1

    while i < j:
        while i < j and array[j] == to_move:
            j -= 1
        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]
        i += 1

    return array


if __name__ == '__main__':
    arr = [1, 3, 2, 4, 2, 2, 2, 7]
    move_element_to_end(arr, 2)
    print(arr)
