import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# f(theta) = theta*cos(theta) - 0.2
def f(theta):
    return theta * np.cos(theta) - 0.2

# f'(theta) = cos(theta) - theta*sin(theta)
def f_prime(theta):
    return np.cos(theta) - theta * np.sin(theta)

def newton_raphson(f, f_prime, theta0, iterations=2):
    print(f"{'Iter':<5}{'theta':<12}{'f(theta)':<14}{'fprime(theta)':<16}{'theta_new':<12}{'Abs Error':<12}")
    print("-" * 71)

    theta_old = theta0
    theta_history = [theta0]   # store every theta for plotting the points

    for i in range(1, iterations + 1):
        f_val = f(theta_old)
        fprime_val = f_prime(theta_old)

        theta_new = theta_old - (f_val / fprime_val)
        abs_error = abs(theta_new - theta_old)

        print(f"{i:<5}{theta_old:<12.6f}{f_val:<14.6f}{fprime_val:<16.6f}{theta_new:<12.6f}{abs_error:<12.6f}")

        theta_history.append(theta_new)
        theta_old = theta_new

    return theta_old, theta_history

theta0 = 0.5
root, theta_history = newton_raphson(f, f_prime, theta0, iterations=2)

print(f"\ntheta after 2 iterations = {root:.3f} rad")

# Plot
theta_plot = np.linspace(-0.5, 1.5, 300)
plt.plot(theta_plot, f(theta_plot), label="y = f(theta)")
plt.axvline(root, color='red', linestyle='--', label=f'theta ≈ {root:.3f}')
plt.axhline(0, color='black', linewidth=5)

# mark each iteration's theta point on the curve
for i, t in enumerate(theta_history):
    plt.scatter(t, f(t), color='green', zorder=5)
    plt.annotate(f"θ{i}", (t, f(t)), textcoords="offset points", xytext=(5,8), fontsize=8)

plt.xlabel("theta (rad)")
plt.ylabel("f(theta)")
plt.title("Newton-Raphson: f(theta) = theta*cos(theta) - 0.2")
plt.grid()
plt.legend()
plt.show()