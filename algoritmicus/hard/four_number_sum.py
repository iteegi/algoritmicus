"""Four Number Sum algorithm."""


from collections.abc import Sequence
from typing import TypeAlias

Sum_of_numbers: TypeAlias = list[list[int]]
Target_sum: TypeAlias = list[list[int] | None]


def four_number_sum(array: Sequence[int], target_sum: int) -> Target_sum:
    """Find all quadruplets in the array that sum up to the target sum.

    Find all quadruplets in the array that sum up to the target sum and
    return a two-dimensional array of all these quadruplets in no particular
    order. If no four numbers sum up to the target sum, the function should
    return an empty array.

    Average:    O(n^2) time  | O(n^2) space
    Worst:      O(n^3) time  | O(n^2) space

    :param array: Array of integers.
    :type array: Sequence[int]
    :param target_sum: Target sum.
    :type target_sum: int
    :return: List of found numbers, or an empty list.
    :rtype: Target_sum
    """

    allPairSums: dict[int, Sum_of_numbers] = {}
    quadruplets: Target_sum = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = target_sum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])

        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])

    return quadruplets


if __name__ == '__main__':
    input = [7, 6, 4, -1, 1, 2]
    output = four_number_sum(input, 16)
    if output:
        print(f'Quadruplets: {output}')
    else:
        print(f'Quadruplet doesn\'t exist')
