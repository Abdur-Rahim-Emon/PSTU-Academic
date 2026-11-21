import numpy as np

import matplotlib.pyplot as plt

def y1(x, y):
    return y - x**3

def y2(x, y):
    return y - x**3 - 3*x**2

def y3(x, y):
    return y - x**3 - 3*x**2 - 6*x

def y4(x, y):
    return y - x**3 - 3*x**2 - 6*x - 6


# ---------------------------------------
# Taylor Series Method
# ---------------------------------------

def taylor_method(x0, y0, h, steps):

    x = x0
    y = y0

    print("x\t\t y")
    print("----------------------")
    print(f"{x:.1f}\t\t{y:.6f}")

    for i in range(steps):

        dy1 = y1(x, y)
        dy2 = y2(x, y)
        dy3 = y3(x, y)
        dy4 = y4(x, y)

        y = (y
             + h*dy1
             + (h**2/2)*dy2
             + (h**3/6)*dy3
             + (h**4/24)*dy4)

        x = x + h

        print(f"{x:.1f}\t\t{y:.6f}")


x0 = 0
y0 = 1
h = 0.1
steps = 3

taylor_method(x0, y0, h, steps)


def fun_avg(x, y):
    return (x + y) * 0.5

def milnes_method(f, x0, x1, x2, x3, y0, y1, y2, y3, x4):
    x = [x0, x1, x2, x3, x4]
    y = [y0, y1, y2, y3, None]
    h = x[1] - x[0]

    # derivatives dy/dx at x1, x2, x3
    y1_value = f(x[1], y[1])
    y2_value = f(x[2], y[2])
    y3_value = f(x[3], y[3])

    # --- table of x, y, dy/dx ---
    print(f"{'x':<8}{'y':<10}{'dy/dx':<10}")
    print("-" * 26)
    print(f"{x0:<8}{y0:<10}{'-':<10}")
    print(f"{x1:<8}{y1:<10}{y1_value:<10.4f}")
    print(f"{x2:<8}{y2:<10}{y2_value:<10.4f}")
    print(f"{x3:<8}{y3:<10}{y3_value:<10.4f}")

    # --- predictor ---
    y4_predictor = y[0] + (4 * h / 3) * (2 * y1_value - y2_value + 2 * y3_value)
    print(f"\nPredictor: y4 = {y4_predictor:.4f}")

    # --- corrector ---
    y4_value = f(x[4], y4_predictor)
    y4_corrector = y[2] + (h / 3) * (y2_value + 4 * y3_value + y4_value)
    print(f"Corrector: y4 = {y4_corrector:.4f}")

    return y4_corrector


x0, x1, x2, x3 = 0, 0.5, 1.0, 1.5
y0, y1, y2, y3 = 2, 2.636, 3.595, 4.968

final_y = milnes_method(fun_avg, x0, x1, x2, x3, y0, y1, y2, y3, x4=2)

# --- plot ---
plt.plot([x0, x1, x2, x3, 2], [y0, y1, y2, y3, final_y], marker='o', label="Milne's Method", color='green')
plt.title("Milne's Method for Solving ODE")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
plt.show()