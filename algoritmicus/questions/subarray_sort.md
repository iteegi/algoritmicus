## Subarray Sort

#### Problem Statement


Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should return `[-1, -1]`.


#### Complexity Analysis

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**


#### For example:

```python
Input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Output: [3, 9]
```

or

```python
Input: [1, 2, 3, 4, 5]
Output: [-1, -1]
```

or

```python
Input: [1, 2, 8, 4, 5]
Output: [2, 4]
```


#### Solution

Check this [Python](../hard/subarray_sort.pys) code.

