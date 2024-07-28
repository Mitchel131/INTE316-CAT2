import numpy as np

# Define the function to integrate
def f(x):
    return x**2

# Define the trapezoidal rule function
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)
    integral = h/2 * (np.sum(fx) - fx[0] - fx[-1])
    return integral

# Define the interval [a, b] and the number of subintervals n
a = 0
b = 1
n = 100

# Calculate the integral using the trapezoidal rule
result = trapezoidal_rule(a, b, n)
print("Approximate integral using the trapezoidal rule:", result)