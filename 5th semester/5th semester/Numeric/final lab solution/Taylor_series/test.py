import matplotlib.pyplot as plt

# ---------------------------------------
# Differential Equation
# dy/dx = y - x^3
# ---------------------------------------

def f(x, y):
    return y - x**3


# ---------------------------------------
# Taylor Series Derivatives
# ---------------------------------------

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

    x_values = [x0]
    y_values = [y0]

    print("\nTaylor Series")
    print("-"*30)
    print("x\t\t y")
    print("-"*30)
    print(f"{x0:.1f}\t\t{y0:.6f}")

    x = x0
    y = y0

    for i in range(steps):

        y = (y
             + h*y1(x, y)
             + (h**2/2)*y2(x, y)
             + (h**3/6)*y3(x, y)
             + (h**4/24)*y4(x, y))

        x += h

        x_values.append(x)
        y_values.append(y)

        print(f"{x:.1f}\t\t{y:.6f}")

    return x_values, y_values


# ---------------------------------------
# Milne Predictor-Corrector
# ---------------------------------------

def milne_method(x, y, h):

    f0 = f(x[0], y[0])
    f1 = f(x[1], y[1])
    f2 = f(x[2], y[2])
    f3 = f(x[3], y[3])

    print("\nDerivative Table")
    print("-"*40)
    print("x\t\t y\t\t f(x,y)")
    print("-"*40)

    for i in range(4):
        print(f"{x[i]:.1f}\t\t{y[i]:.6f}\t{f(x[i],y[i]):.6f}")

    # Predictor
    yp = y[0] + (4*h/3)*(2*f1 - f2 + 2*f3)

    x4 = x[3] + h
    fp = f(x4, yp)

    # Corrector
    yc = y[2] + (h/3)*(f2 + 4*f3 + fp)

    print("\nMilne Predictor")
    print("------------------------")
    print(f"y({x4:.1f}) = {yp:.6f}")

    print("\nMilne Corrector")
    print("------------------------")
    print(f"y({x4:.1f}) = {yc:.6f}")

    return x4, yc


# ---------------------------------------
# Main Program
# ---------------------------------------

h = 0.1

# Taylor gives y(0.1), y(0.2), y(0.3)
x, y = taylor_method(0, 1, h, 3)

# Milne finds y(0.4)
x4, y4 = milne_method(x, y, h)

# Store new point
x.append(x4)
y.append(y4)

# ---------------------------------------
# Plot
# ---------------------------------------

plt.figure(figsize=(7,5))

plt.plot(x, y, marker='o', linewidth=2)

plt.title("Taylor Series + Milne Predictor-Corrector")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()