
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y - 0.5*np.exp(x/2)*np.sin(5*x) + 5*np.exp(x/2)*np.cos(5*x)

def exact_solution(x):
    return np.exp(x/2) * np.sin(5*x)

def euler_method(f, x0, y0, h=0.1, n=100):
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    return np.array(x_values), np.array(y_values)

def solve_and_plot(x0, y0, h, t_end):
    n = int(round((t_end - x0) / h))   # auto-calculate number of steps
    x_values, y_values = euler_method(f, x0, y0, h, n)
    exact_values = exact_solution(x_values)
    error = np.abs(exact_values - y_values)
    percent_error = np.where(exact_values != 0, (error / np.abs(exact_values)) * 100, 0)

    print(f"{'n':<3}{'x_n':<8}{'y_n (Euler)':<15}{'Exact':<15}{'Error':<12}{'% Error':<10}")
    print("-" * 65)
    for i in range(len(x_values)):
        print(f"{i:<3}{x_values[i]:<8.2f}{y_values[i]:<15.6f}"
              f"{exact_values[i]:<15.6f}{error[i]:<12.6f}{percent_error[i]:<10.2f}")

    print()
    x_fine = np.linspace(x0, x_values[-1], 500)
    y_fine_exact = exact_solution(x_fine)

    plt.figure(figsize=(9, 6))
    plt.plot(x_values, y_values, 'o--', label="Euler's Method", color='blue')
    plt.plot(x_fine, y_fine_exact, label="Exact Solution", color='red')
    plt.title(f"Euler's Method (x0={x0}, y0={y0}, h={h}, t_end={t_end})")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

    return x_values, y_values, exact_values, error, percent_error

solve_and_plot (0,0,0.1,1)
solve_and_plot (0,0,0.01,1)
