"""Three Number Sum algorithm."""

from typing import List, Tuple


Array = List[int]
Sample_sum = int
Term_1 = int
Term_2 = int
Triplates = List[Tuple[Sample_sum, Term_1, Term_2]]


def three_number_sum(array: Array, targetSum: int) -> Triplates:
    """Find all triplets in the array that sum up to a given target value.

    O(n^2) time | O(n) space

    :param array: Sample input array.
    :type array: Array
    :param targetSum: Sample sum.
    :type targetSum: int
    :return: A tuple containing the sum to be found and two terms that give
    this sum.
    :rtype: Triplates
    """
    array.sort()
    triplates = []
    for i in range(len(array) - 2):
        left_index = i + 1
        right_index = len(array) - 1
        while left_index < right_index:
            sum = array[i] + array[left_index] + array[right_index]
            if sum == targetSum:
                triplates.append(
                    (array[i],
                     array[left_index],
                     array[right_index])
                )
                left_index += 1
                right_index -= 1
            elif sum < targetSum:
                left_index += 1
            elif sum > targetSum:
                right_index -= 1
    return triplates


if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    sample_sum = 0
    result = three_number_sum(array, sample_sum)
    print(f"The sets of triplates are: {result}")
