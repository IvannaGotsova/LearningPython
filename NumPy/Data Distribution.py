from numpy import random

array_example = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                              p=[0.0, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0, 0.2],
                              size=(20))

print(array_example)

array_example = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                              p=[0.0, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0, 0.2],
                              size=(3, 7, 1))

print(array_example)