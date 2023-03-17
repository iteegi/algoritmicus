"""Longest Peak algorithm."""


from typing import List


Longest_peak_length = int


def longest_peak(array: List[int]) -> Longest_peak_length:
    """Returns the length of the longest peak in the array.

    O(N) time | O(1) space

    Function that takes in an array of integers and returns the length of the
    longest peak in the array.

    A peak is defined as adjacent integers in the array that are strictly
    increasing until they reach a tip (the highest value in the peak), at
    which point they become strictly decreasing. At least three integers are
    required to form a peak.

    :param array: Array of integers.
    :type array: List[int]
    :return:  The length of the longest peak in the array.
    :rtype: Longest_peak_length
    """
    longest_peak_length = 0
    i = 0

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        left_idx = i - 2

        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1

        right_idx = i + 2

        while right_idx < len(array) and \
                array[right_idx] < array[right_idx - 1]:
            right_idx += 1

        current_peak_length = right_idx - left_idx - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)
        i = right_idx

    return longest_peak_length


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longest_peak(arr))
