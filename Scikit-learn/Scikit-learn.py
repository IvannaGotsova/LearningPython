import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X_features = np.array([1, 2, 3, 3, 7, 6, 7, 8, 9, 10]).reshape(-1, 1)
Y_target = np.array([2, 4, 5, 7, 10, 12, 15, 19, 20, 22])

training_model = LinearRegression()
training_model.fit(X_features, Y_target)

Y_target_prediction = training_model.predict(X_features)

plt.scatter(X_features, Y_target, label="Actual")
plt.plot(X_features, Y_target_prediction, color="blue", label="Predicted")
plt.legend()
plt.show()
