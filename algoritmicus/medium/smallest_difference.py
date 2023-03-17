"""Smallest Difference algorithm."""


from typing import List, Tuple

Number_from_1_array = int
Number_from_2_array = int

Result = Tuple[Number_from_1_array, Number_from_2_array]


def smallest_difference(array_one: List[int], array_two: List[int]) -> Result:
    """Return a pair of numbers whose absolute difference is close to zero.

    O(nlog(n) + mlon(m)) time | O(1) space

    :param array_one: First non-empty array of integers.
    :type array_one: Number_from_1_array
    :param array_two: Second non-empty array of integers
    :type array_two: Number_from_2_array
    :return: A pair of numbers whose absolute difference is close to zero.
    :rtype: Result
    """
    array_one.sort()
    array_two.sort()
    index_one = 0
    index_two = 0
    smallest = float("inf")
    current = float("inf")

    while index_one < len(array_one) and index_two < len(array_two):
        first_num = array_one[index_one]
        second_num = array_two[index_two]
        if first_num < second_num:
            current = second_num - first_num
            index_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            index_two += 1
        else:
            return (first_num, second_num)

        if smallest > current:
            smallest = current
            result_pair = (first_num, second_num)
    return result_pair


if __name__ == '__main__':
    arr_1 = [-1, 5, 10, 20, 28, 3]
    arr_2 = [26, 134, 135, 15, 17]

    res = smallest_difference(arr_1, arr_2)

    print(f'{res}')
