"""Subarray Sort algorithm."""


from collections.abc import Sequence


def subarray_sort(array: Sequence[int]) -> list[int]:
    """Return an array of the starting and ending indices of the subarray.

    The function should return an array of the starting and ending indices
    of the smallest subarray in the input array that needs to be sorted in
    place in order for the entire input array to be sorted. If the input
    array is already sorted, the function should return [-1, -1].

    O(N) time | O(1) space

    :param array: An array of integers.
    :type array: Sequence[int]
    :return: Positions where you need to sort the array.
    :rtype: list[int]
    """
    min_out_of_order = float('inf')
    max_out_of_order = float('-inf')

    for i in range(len(array)):
        num = array[i]
        if _is_out_of_order(i, num, array):
            min_out_of_order = min(num, min_out_of_order)
            max_out_of_order = max(num, max_out_of_order)

    if min_out_of_order == float('inf'):
        return [-1, -1]

    sub_array_left_idx = 0
    sub_array_right_idx = len(array) - 1

    while min_out_of_order >= array[sub_array_left_idx]:
        sub_array_left_idx += 1

    while max_out_of_order <= array[sub_array_right_idx]:
        sub_array_right_idx -= 1

    return [sub_array_left_idx, sub_array_right_idx]


def _is_out_of_order(i: int, num: int, array: Sequence[int]) -> bool:
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


if __name__ == '__main__':
    arrs = [
        [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19],
        [1, 2, 3, 4, 5],
        [1, 2, 8, 4, 5]
    ]

    for k, arr in enumerate(arrs):
        res = subarray_sort(arr)
        print(f'\n{k + 1:*^52}')
        print(f'Array: {arr}')
        print(f'Result: {res}')
        print(f'*' * 52)
