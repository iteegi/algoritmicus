"""Array of products algorithm."""


from typing import List


def array_of_products(array: List[int]) -> List[int]:
    """Return an array A such that A[i] is equl to the product of all the
    elements of B exept B[i].

    O(N) time | O(N) space

    :param array: Array of integers.
    :type array: List[int]
    :return: List of multiplied numbers.
    :rtype: List[int]
    """
    products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(array_of_products(arr))

    arr = [-1, 1, 0, -3, 3]
    print(array_of_products(arr))
