import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Gradient Descent Function
def gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=10000):
    n = len(y)

    for _ in range(epochs):
        # Predict y
        y_pred = m * x + b

        # Calculate gradients
        dm = (-2 / n) * np.sum(x * (y - y_pred))
        db = (-2 / n) * np.sum(y - y_pred)

        # Update parameters
        m -= learning_rate * dm
        b -= learning_rate * db

    return m, b

# Plot the original data
plt.scatter(x, y, label="Data")

# Train the model
m, b = gradient_descent(x, y)

# Print the final values
print("Final Parameters")
print("----------------")
print(f"Slope (m)      = {m:.4f}")
print(f"Intercept (b)  = {b:.4f}")
print(f"Equation       = y = {m:.4f}x + {b:.4f}")

# Plot the regression line
plt.plot(x, m * x + b, color='red', linewidth=2, label="Regression Line")

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression using Gradient Descent")
plt.legend()

# Show the plot
plt.show()