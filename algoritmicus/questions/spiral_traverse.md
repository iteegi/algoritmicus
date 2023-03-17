## Smallest Difference

#### Problem Statement


The Spiral Matrix problem takes a 2-Dimensional array of N-rows and
M-columns as an input, and prints the elements of this matrix in
spiral order.

The spiral begins at the top left corner of the input matrix, and prints
the elements it encounters, while looping towards the center of this
matrix, in a clockwise manner.
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]


#### Complexity Analysis

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**


#### How does the spiral matrix algorithm work?


- First, four variables containing the indices for the corner points of the array are initialized.
- The algorithm starts from the top left corner of the array, and traverses the first row from left to right. Once it traverses the whole row it does not need to revisit it, thus, it increments the top corner index.
- Once complete, it traverses the rightmost column top to bottom. Again, once this completes, there is no need to revisit the rightmost column, thus, it decrements the right corner index.
- Next, the algorithm traverses the bottommost row and decrements the bottom corner index afterward.
- Lastly, the algorithm traverses the leftmost column, incrementing the left corner index once it’s done.

This continues until the left index is greater than the right index, and the top index is greater than the bottom index.


#### Solution

Check this [Python](../medium/spiral_traverse.py) code.

