"""Max Path Sum In Binary Tree algorithm."""


from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def max_path_sum(tree: Node) -> int:
    """Return max path sum.

    O(n) time | O(log(n)) space.

    :param tree: Binary tree.
    :type tree: Node
    :return: Max path sum.
    :rtype: int
    """
    _, maxSum = _find_max_sum(tree)
    return maxSum


def _find_max_sum(tree):
    if tree is None:
        return (0, 0)

    left_max_sum_as_branch, leftMaxPathSum = _find_max_sum(tree.left)
    right_max_sum_as_branch, rightMaxPathSum = _find_max_sum(tree.right)
    max_child_sum_as_branch = max(left_max_sum_as_branch,
                                  right_max_sum_as_branch)

    value = tree.value
    max_sum_as_branch = max(max_child_sum_as_branch + value, value)
    max_sum_as_root_node = max(left_max_sum_as_branch +
                               value +
                               right_max_sum_as_branch,
                               max_sum_as_branch)
    max_path_sum = max(leftMaxPathSum, rightMaxPathSum, max_sum_as_root_node)

    return (max_sum_as_branch, max_path_sum)


if __name__ == '__main__':
    tree = Node(10)
    tree.left = Node(2)
    tree.right = Node(10)
    tree.left.left = Node(20)
    tree.left.right = Node(1)
    tree.right.right = Node(-25)
    tree.right.right.left = Node(3)
    tree.right.right.right = Node(4)

    print(f'Max path sum is {max_path_sum(tree)}')
