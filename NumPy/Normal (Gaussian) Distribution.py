import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

array_example = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

sns.distplot(random.normal(array_example), hist=False)

plt.show()