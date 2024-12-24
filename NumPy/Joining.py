import numpy as np

array_first = np.array([1, 2, 3])

array_second = np.array([4, 5, 6])

array_third = np.array([7, 8, 9])

array_example = np.concatenate((array_first, array_second, array_third))

print(array_example)

array_example = np.stack((array_first, array_second, array_third), axis=1)

print(array_example)

array_example = np.hstack((array_first, array_second, array_third))

print(array_example)

array_example = np.vstack((array_first, array_second, array_third))

print(array_example)

array_example = np.dstack((array_first, array_second, array_third))

print(array_example)