import numpy as np

array_example = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for y, x in np.ndenumerate(array_example):
  print(y, x)