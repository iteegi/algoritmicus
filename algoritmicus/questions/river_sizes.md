## River Sizes

#### Problem Statement


You are given a two-dimensional array of potentially unequal height and
width. It contains only 0s and 1s. This array represents a map: 0s are land,
and 1s are water. A "river" on this map consists of any number of contiguous,
adjacent water squares, where "adjacent" means "above", "below", "to the
left of", or "to the right of" (that is , diagonal squares are not adjacent).
Write a function which returns an array of the sizes of all rivers
represented in the input matrix. Note that these sizes do not need to be in
any particular order.


#### Complexity Analysis

- Time Complexity: **O(wh)**
- Space Complexity: **O(wh)**


#### For example:
matrix = [
   [1, 0, 0, 1, 0],
   [1, 0, 1, 0, 0],
   [0, 0, 1, 0, 1],
   [1, 0, 1, 0, 1],
   [1, 0, 1, 1, 0]
 ]

riverSizes(input); // returns [1, 2, 2, 2, 5]

That is, in this input, there is one river of size 1, there are three rivers
of size 2, and there is one river of size 5.



#### Solution

Check this [Python](../medium/river_sizes.py) code.

