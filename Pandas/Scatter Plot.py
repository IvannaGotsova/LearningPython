import pandas as pd
import matplotlib.pyplot as plt

data = {
  "first_column": [1, 2, 3, 4, 5],
  "second_column": [10, 20, 30, 40, 50],
  "third_column": [100, 200, 300, 400, 500]
}

dataFrame = pd.DataFrame(data, index = ["first_row", "second_row", "third_row", "fourth_row", "fifth_row"])

dataFrame.plot(kind = 'scatter', x = 'first_column', y = 'second_column')

plt.show()

dataFrame.plot(kind = 'scatter', x = 'first_column', y = 'third_column')

plt.show()

dataFrame.plot(kind = 'scatter', x = 'second_column', y = 'third_column')

plt.show()