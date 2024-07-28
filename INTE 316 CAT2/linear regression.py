import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Define the data points
X = np.array([[0], [1], [2], [3], [4]])
y = np.array([0, 2, 4, 6, 8])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
X_pred = np.array([[5], [6]])
y_pred = model.predict(X_pred)

# Plot the data points and the linear regression line
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, model.predict(X), color='red', label='Linear Regression Line')
plt.scatter(X_pred, y_pred, color='green', label='Predictions')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()