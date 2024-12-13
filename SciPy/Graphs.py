import numpy as np
from scipy.sparse.csgraph import dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
from scipy.sparse import csr_matrix

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [0, 0, 0, 0]]

matrix_graphs = csr_matrix(matrix)

print(dijkstra(matrix_graphs, return_predecessors=True, indices=0))
print(floyd_warshall(matrix_graphs, return_predecessors=True))
print(bellman_ford(matrix_graphs, return_predecessors=True, indices=0))
print(depth_first_order(matrix_graphs, 1))
print(breadth_first_order(matrix_graphs, 1))