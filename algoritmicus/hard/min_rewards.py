"""Min Rewards algorithm."""

import timeit

from collections.abc import Sequence
from typing import TypeAlias

Amount_awards: TypeAlias = int


def min_rewards_1(score: Sequence[int]) -> Amount_awards:
    """Return the minimum number of rewards you must give away.

    Solution #1

    O(n^2) time | O(n) space

    :param score: List of student grades.
    :type score: Sequence[int]
    :return: The minimum number of rewards.
    :rtype: Amount_awards
    """
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        j = i - 1
        if score[i] > score[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and score[j] > score[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)


def min_rewards_2(scores: Sequence[int]) -> Amount_awards:
    """Return the minimum number of rewards you must give away.

    Solution #2

    O(n) time | O(n) space

    :param score: List of student grades.
    :type score: Sequence[int]
    :return: The minimum number of rewards.
    :rtype: Amount_awards
    """
    rewards = [1 for _ in scores]
    local_min_idxs = _get_local_min_idxs(scores)
    for local_min_idx in local_min_idxs:
        _expand_from_local_min_idx(local_min_idx, scores, rewards)
    return sum(rewards)


def _get_local_min_idxs(array):
    if len(array) == 1:
        return [0]
    local_min_idxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            local_min_idxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:
            local_min_idxs.append(i)
        if i == 0 or i == len(array) - 1:
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            local_min_idxs.append(i)
    return local_min_idxs


def _expand_from_local_min_idx(local_min_idx, scores, rewards):
    left_idx = local_min_idx - 1
    while left_idx >= 0 and scores[left_idx] > scores[left_idx + 1]:
        rewards[left_idx] = max(rewards[left_idx], rewards[left_idx + 1] + 1)
        left_idx -= 1
    right_idx = local_min_idx + 1
    while right_idx < len(scores) and \
            scores[right_idx] > scores[right_idx - 1]:
        rewards[right_idx] = rewards[right_idx - 1] + 1
        right_idx += 1


def min_rewards_3(score: Sequence[int]) -> Amount_awards:
    """Return the minimum number of rewards you must give away.

    Solution #3

    O(n) time | O(n) space

    :param score: List of student grades.
    :type score: Sequence[int]
    :return: The minimum number of rewards.
    :rtype: Amount_awards
    """
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        if score[i] > score[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed((range(len(score) - 1))):
        if score[i] > score[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)


if __name__ == '__main__':
    arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]

    list_algo = [min_rewards_1,
                 min_rewards_2,
                 min_rewards_3,]

    for i in range(0, 3):
        code_to_test = f"""a = min_rewards_{i+1}(arr)"""
        elapsed_time = timeit.timeit(code_to_test,
                                     globals=globals(),
                                     number=100)
        res = list_algo[i](arr)
        print(f'min_rewards_{i}: lapsed_time = {elapsed_time:.5}, Sum = {res}')
