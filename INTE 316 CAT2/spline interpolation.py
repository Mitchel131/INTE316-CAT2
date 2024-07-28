import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Define the data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Perform cubic spline interpolation
cs = CubicSpline(x, y)

# Generate points for the interpolated curve
x_interp = np.linspace(0, 4, 100)
y_interp = cs(x_interp)

# Plot the original data points and the interpolated curve
plt.figure()
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_interp, y_interp, label='Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()