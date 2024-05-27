from functools import reduce

numbers = [7, 8, 4, 9, 10, 2, 3, 5, 1, 6]

def sums(x, y):
     return x + y


result = reduce(sums, numbers)

print(result)