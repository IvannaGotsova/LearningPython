import pandas as pd

data = {
  "first_column": [1, 2, 3, 4, 5],
  "second_column": [10, 20, 30, 40, 50],
  "third_column": [100, 200, 300, 400, 500]
}

dataFrame = pd.DataFrame(data, index = ["first_row", "second_row", "third_row", "fourth_row", "fifth_row"])

print(dataFrame)

print(dataFrame.loc[["first_row", "third_row"]])



