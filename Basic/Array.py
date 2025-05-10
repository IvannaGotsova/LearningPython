import numpy as np

arrayExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(len(arrayExample))
print(type(arrayExample))

print(arrayExample[3])

arrayExampleToAdd = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arrayExampleAdded = np.append(arrayExample, arrayExampleToAdd)
print(arrayExampleAdded)
