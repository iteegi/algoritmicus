"""Binary Search."""


from typing import List, Union


# O(log(n)) time | O(1) space
def binary_searcher(array: List[int], target: int) -> Union[int, bool]:
    """Binary search for a number in a sorted array

    :param array: array of sorted numbers
    :type array: List[int]
    :param target: the number to be found
    :type target: int
    :return: the position of the number in the array, or False if the number is not found
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
