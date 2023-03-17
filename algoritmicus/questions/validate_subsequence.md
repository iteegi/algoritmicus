## Validate subsequence

#### Problem Statement


Two arrays with positive numbers are given.
It is required to determine whether one array is a subsequence of the second one.
A subsequence of an array is a set of numbers that are not necessarily adjacent
in the array but that are in the same order as they appear in the array.

For instance, the numbers `[1,3,4]` form a subsequence of the array `[1,2,3,4]`,
and so do the numbers `[2,4]`. Note that a single number in an array and the array
itself are both valid subsequences of the array. `[1],[2],[3],[4]` and `[1,2,3,4]` are
all valid subsequences of `[1,2,3,4]`


#### Complexity Analysis

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**


#### For example:

```
array: [3, 1, 7, 5, 10, 2];
sequence: [1, 5, 2];
Output: true
```


#### Solution

Check this [Python](../easy/validate_subsequence.py) code.

