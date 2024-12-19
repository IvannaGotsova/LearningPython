import pandas as pd

array_one_dimension = [1, 2, 3, 4, 5, 6, 7, 8, 9]

array_one_dimension = pd.Series(array_one_dimension, index = ["one", "two", "three", "four", "five",
                                                              "six", "seven", "eight", "nine"])

print(array_one_dimension)
print("three")

array_two_dimension = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8,
            "nine" : 9}

array_two_dimension = pd.Series(array_two_dimension)

print(array_two_dimension)
print("three")





