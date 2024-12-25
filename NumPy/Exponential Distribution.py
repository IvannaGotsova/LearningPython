import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=100), hist=False)

plt.show()

