"""Validate subsequence

Complexity Analysis
    Time Complexity: O(N), where N is the length of the array.
    Space Complexity: O(1).

Two arrays with positive numbers are given.
It is required to determine whether one array is a subsequence of the second one.
A subsequence of an array is a set of numbers that are not necessarily adjacent
in the array but that are in the same order as they appear in the array.
For instance, the numbers [1,3,4] form a subsequence of the array [1,2,3,4],
and so do the numbers [2,4]. Note that a single number in an array and the array
itself are both valid subsequences of the array.( [1],[2],[3],[4] and [1,2,3,4] are
all valid subsequences of [1,2,3,4] )

"""


from typing import List


def validate_subsequence(array: List[int], sequence: List[int]) -> bool:
    """Return True if the sequence is a subsequence of the array

    :param array: an array of integers
    :type array: List[int]
    :param sequence: a sequence of integers
    :type sequence: List[int]
    :return: is the passed sequence a subsequence of the array?
    :rtype: bool
    """

    seqInd = 0
    for value in array:
        if seqInd == len(sequence):
            break
        if sequence[seqInd] == value:
            seqInd += 1
    return seqInd == len(sequence)


def main():
    array = [3, 1, 7, 5, 10, 2]
    sequence = [1, 5, 2]

    print(validate_subsequence(array, sequence))


if __name__ == "__main__":
    main()
