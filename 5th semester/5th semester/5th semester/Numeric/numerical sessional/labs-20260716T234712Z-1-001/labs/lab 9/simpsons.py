import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def fun(x):
    return  (200*np.log(140000/(140000-2100*x)))-9.8*x

def simpsons_1_3_rule(fun, a, b):
    x0, x1, x2 = a, (a + b) / 2, b
    y0, y1, y2 = fun(x0), fun(x1), fun(x2)
    h = (b - a) / 2
    result = (h / 3) * (y0 + 4*y1 + y2)

    # Table
    print("\nSimpson's 1/3 Rule")
    print(f"{'i':<3}{'x_i':<10}{'f(x_i)':<12}{'Weight':<8}{'Weight*f(x_i)':<15}")
    print("-" * 48)
    labels = ['x0', 'x1', 'x2']
    xs = [x0, x1, x2]
    ys = [y0, y1, y2]
    weights = [1, 4, 1]
    for i in range(3):
        print(f"{labels[i]:<3}{xs[i]:<10.4f}{ys[i]:<12.6f}{weights[i]:<8}{weights[i]*ys[i]:<15.6f}")
    print("-" * 48)
    print(f"Result = (h/3) * Σ(weight*f) = ({h:.4f}/3) * {sum(w*y for w,y in zip(weights, ys)):.6f} = {result:.6f}\n")

    return result, xs, ys


def simpsons_3_8_rule(fun, a, b):
    a, b = min(a, b), max(a, b)
    h = (b - a) / 3
    x0, x1, x2, x3 = a, a+h, a+2*h, b
    y0, y1, y2, y3 = fun(x0), fun(x1), fun(x2), fun(x3)
    result = (3*h/8) * (y0 + 3*y1 + 3*y2 + y3)

    # Table
    print("\nSimpson's 3/8 Rule")
    print(f"{'i':<3}{'x_i':<10}{'f(x_i)':<12}{'Weight':<8}{'Weight*f(x_i)':<15}")
    print("-" * 48)
    labels = ['x0', 'x1', 'x2', 'x3']
    xs = [x0, x1, x2, x3]
    ys = [y0, y1, y2, y3]
    weights = [1, 3, 3, 1]
    for i in range(4):
        print(f"{labels[i]:<3}{xs[i]:<10.4f}{ys[i]:<12.6f}{weights[i]:<8}{weights[i]*ys[i]:<15.6f}")
    print("-" * 48)
    print(f"Result = (3h/8) * Σ(weight*f) = (3*{h:.4f}/8) * {sum(w*y for w,y in zip(weights, ys)):.6f} = {result:.6f}\n")

    return result, xs, ys




result_13, xs_13, ys_13 = simpsons_1_3_rule(fun, 8,15.33)
print("Simpson's 1/3 Rule Final Value:", result_13)

result_38, xs_38, ys_38 = simpsons_3_8_rule(fun, 15.33, 30)
print("Simpson's 3/8 Rule Final Value:", result_38)

# --- Run both methods ---
array = np.arange(8, 30, 1)

# --- Plotting ---
plt.plot(array, fun(array), label="f(x)")

plt.scatter(xs_13, ys_13, color='green') ## making individuals dots of x1 x2 x3
plt.plot(array, CubicSpline(xs_13, ys_13)(array), '--', color='red', label='Simpson 1/3 Rule')
plt.fill_between(array, CubicSpline(xs_13, ys_13)(array), color='red', alpha=0.3)
## simpsons 3/8 rule 
plt.scatter(xs_38, ys_38, color='green')# for point in the grapgh
plt.plot(array, CubicSpline(xs_38, ys_38)(array), '--', label="Simpson 3/8 Rule")
plt.fill_between(array, CubicSpline(xs_38, ys_38)(array), alpha=0.3)

plt.legend()
plt.title("Simpson's 1/3 Rule vs Simpson's 3/8 Rule")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.show()