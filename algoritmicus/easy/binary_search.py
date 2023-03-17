"""Binary Search."""


from typing import List, Union


def binary_searcher(array: List[int], target: int) -> Union[int, bool]:
    """Binary search for a number in a sorted array

    O(log(n)) time | O(1) space

    :param array: Array of sorted numbers.
    :type array: List[int]
    :param target: The number to be found.
    :type target: int
    :return: The position of the number in the array, or False if the number
    is not found.
    :rtype: Union[int, bool]

    """

    left = 0
    right = len(array) - 1
    while left <= right:
        middel = (left + right) // 2
        potentialMatch = array[middel]
        if target == potentialMatch:
            return middel
        elif target < potentialMatch:
            right = middel - 1
        else:
            left = middel + 1
    return False


def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 89, 99, 100]
    t = 0
    print(binary_searcher(a, t))


if __name__ == "__main__":
    main()
