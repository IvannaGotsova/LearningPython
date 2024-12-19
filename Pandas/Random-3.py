import pandas as pd

data = {
  "first_column": [1, 2, 3, 4, 5],
  "second_column": [10, 20, 30, 40, 50],
  "third_column": [100, 200, 300, 400, 500]
}

dataFrame = pd.DataFrame(data, index = ["first_row", "second_row", "third_row", "fourth_row", "fifth_row"])

print(dataFrame)

print(dataFrame.mean())
print(dataFrame.median())
print(dataFrame.mode())
print(dataFrame.min())
print(dataFrame.max())
print(dataFrame.nunique())
print(dataFrame.pct_change())
print(dataFrame.prod())
print(dataFrame.sem())