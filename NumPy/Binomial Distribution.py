import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=100), hist=True, kde=False)

plt.show()