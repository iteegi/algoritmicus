## Largest Range

#### Problem Statement


Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The rst number in the output array should be the rst number in the range while the second number should be the last number in the range. A range of numbers is dened as a set of numbers that come right after each other in the set of real integers. For instance, the output array `[2, 6]` represents the range `{2, 3, 4, 5, 6}`, which is a range of length `5`. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.


#### Complexity Analysis

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**


#### For example:

```python
Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Output: [0, 7]
```


#### Solution

Check this [Python](../hard/largest_range.py) code.

