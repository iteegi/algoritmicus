"""Largest Range algorithm."""


def largest_range(array: list[int]) -> list[int]:
    """Return an array representing the largest range of numbers in the array.

    O(n) time | O(n) space

    :param array: An array of integers.
    :type array: list[int]
    :return: An array of length 2 representing the largest range of numbers
    contained in that array.
    :rtype: list[int]
    """
    best_range = []
    longest_length = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        current_lenght = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            current_lenght += 1
            left -= 1
        while right in nums:
            nums[right] = False
            current_lenght += 1
            right += 1
        if current_lenght > longest_length:
            longest_length = current_lenght
            best_range = [left + 1, right - 1]
    return best_range


if __name__ == '__main__':
    arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print(largest_range(arr))
