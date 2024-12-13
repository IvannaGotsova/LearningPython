from scipy.sparse import csc_matrix

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [0, 0, 0, 0]]

print(csc_matrix(matrix))
