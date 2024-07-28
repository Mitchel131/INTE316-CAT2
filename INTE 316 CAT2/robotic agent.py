import numpy as np

# Given coordinates
x_coords = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_coords = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# The x value we want to interpolate at
x_target = 4.0

# Find the interval for x_target
for i in range(len(x_coords) - 1):
    if x_coords[i] <= x_target <= x_coords[i + 1]:
        x1, y1 = x_coords[i], y_coords[i]
        x2, y2 = x_coords[i + 1], y_coords[i + 1]
        break

# Calculate the interpolated y value
y_target = y1 + ((y2 - y1) / (x2 - x1)) * (x_target - x1)

# Print the result
print(f'The value of y at x = {x_target} is approximately: {y_target:.2f}')