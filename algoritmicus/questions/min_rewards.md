## Min Rewards

#### Problem Statement


Imagine that you're a teacher who's just graded the nal exam in a class. You have a list of student scores on the nal exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: rst, all students must receive at least one reward; second, any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score. Assume that all students have different scores; in other words, the scores are all unique. Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students, all the while satisfying the two rules.


#### Complexity Analysis

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**


#### For example:

```python
Input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
Output: 25
```

or

```python
Input: [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```


#### Solution

Check this [Python](../medium/array_of_products.py) code.

