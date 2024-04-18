import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**2 - 2*x + 1

# Create a range of x values
x = np.linspace(-5, 5, 100)

# Plot the function
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 2x + 1')
plt.show()