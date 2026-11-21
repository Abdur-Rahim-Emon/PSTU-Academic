import matplotlib.pyplot as plt
import numpy as np

def bisection_method(f, a, b, tol=1e-5, max_iter=50):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    print(f"{'Iter':<5}{'a':<10}{'b':<10}{'f(a)':<12}{'f(b)':<12}{'c':<10}{'f(c)':<12}{'Abs Error':<12}")
    print("-" * 83)

    c_old = None  # Stores previous midpoint for error calculation

    for i in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        c = (a + b) / 2
        fc = f(c)

        # Absolute error = |current c - previous c|
        if c_old is None:
            abs_error = float('nan')
        else:
            abs_error = abs(c - c_old)

        print(f"{i:<5}{a:<10.6f}{b:<10.6f}{fa:<12.6f}{fb:<12.6f}{c:<10.6f}{fc:<12.6f}{abs_error:<12.6f}")

        # Stop if function value is close enough to zero
        if abs(fc) < tol:
            return c

        # Update interval
        if fa * fc < 0:
            b = c
        else:
            a = c

        c_old = c

    return c

# Function
def f(x):
    return ((668.061 / x) * (1 - np.exp(-0.1468 * x))) - 40

# Find root
root = bisection_method(f, 14, 16)
print(f"\nApproximate root: {root:.6f}")

# Plot
x = np.arange(10, 20, 0.1)
plt.plot(x, f(x), label='f(x)')
plt.axvline(root, color='red', linestyle='--', label=f'Root ≈ {root:.5f}')
plt.axhline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()
plt.show()