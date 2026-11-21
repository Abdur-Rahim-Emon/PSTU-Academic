import numpy as np
import matplotlib.pyplot as plt

# Third approximation
def Y3(x):
    return (
        1
        + (x)
        + pow(x, 3) / 3
        + pow(x, 4) / 4
        + pow(x, 6) / 18
        + pow(x, 7) / 28
        + pow(x, 9) / 162
    )

def picard_method(f, x0, h=0.1, n=10, iterations=3):
    x_values = np.arange(x0, x0 + n * h, h)
    y_values = np.array([f(i) for i in x_values])

    return x_values, y_values

x_values, y_values = picard_method(f=Y3, x0=0, h=0.1)

# --- show the results ---
print(f"{'x':<8}{'y (3rd approximation)':<25}")
print("-" * 33)
for xi, yi in zip(x_values, y_values):
    print(f"{xi:<8.1f}{yi:<25.6f}")

plt.plot(x_values, y_values)
plt.scatter(x_values[1], y_values[1], label=f'Point at x={x_values[1]:.1f}')
plt.scatter(x_values[2], y_values[2], label=f'Point at x={x_values[2]:.1f}')
plt.legend()
plt.show()