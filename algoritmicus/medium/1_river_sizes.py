# The river sizes algorithm

# You are given a two-dimensional array of potentially unequal height and
# width. It contains only 0s and 1s. This array represents a map: 0s are land,
# and 1s are water. A "river" on this map consists of any number of contiguous,
# adjacent water squares, where "adjacent" means "above", "below", "to the
# left of", or "to the right of" (that is , diagonal squares are not adjacent).
# Write a function which returns an array of the sizes of all rivers
# represented in the input matrix. Note that these sizes do not need to be in
# any particular order.

# For example:
# matrix = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0]
# ]

# riverSizes(input); // returns [1, 2, 2, 2, 5]

# That is, in this input, there is one river of size 1, there are three rivers
# of size 2, and there is one river of size 5.


from typing import List


Matrix = List[List[int]]
River_sizes = List[int]
Visited_nodes = List[List[bool]]
List_neighbors = List[List[int]]


# O(wh) time | O(wh) space
def river_sizes(matrix: Matrix) -> River_sizes:
    """Calculate river sizes.

    :param matrix: You are given a two-dimensional array of potentially
    unequal height and width. It contains only 0s and 1s. This array
    represents a map: 0s are land, and 1s are water. A "river" on this map
    consists of any number of contiguous, adjacent water squares, where
    "adjacent" means "above", "below", "to the left of", or "to the right of"
    (that is, diagonal squares are not adjacent).
    :type matrix: Matrix
    :return: River sizes.
    :rtype: River_sizes
    """
    sizes: River_sizes = []
    visited: Visited_nodes = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            _travers_node(i, j, matrix, visited, sizes)

    return sizes


def _travers_node(i: int,
                  j: int,
                  matrix: Matrix,
                  visited: Visited_nodes,
                  sizes: River_sizes) -> None:
    """Calculating the size of the river."""

    current_river_size = 0
    nodes_to_explorer = [[i, j]]

    while len(nodes_to_explorer):
        current_node = nodes_to_explorer.pop()
        i = current_node[0]
        j = current_node[1]

        if visited[i][j]:
            continue
        visited[i][j] = True

        if matrix[i][j] == 0:
            continue

        current_river_size += 1

        unvisited_neighbors = _get_unvisited_neighbors(i, j, matrix, visited)

        for neighbor in unvisited_neighbors:
            nodes_to_explorer.append(neighbor)

    if current_river_size > 0:
        sizes.append(current_river_size)


def _get_unvisited_neighbors(i: int,
                             j: int,
                             matrix: Matrix,
                             visited: Visited_nodes) -> List_neighbors:
    """Get a list of neighbors.

    Returns whether parts of the river continue.
    """

    unvisited_neighbors: List_neighbors = []

    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbors.append([i, j + 1])

    return unvisited_neighbors


if __name__ == '__main__':

    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]

    result = river_sizes(matrix)

    print(sorted(result))
