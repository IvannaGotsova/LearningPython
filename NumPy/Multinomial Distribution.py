import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

array_example = random.multinomial(n=10, pvals=[1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10])

print(array_example)