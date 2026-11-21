
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_data.csv")

# Read the CSV
data = pd.read_csv(csv_path)
x = data["x"].values
y = data["y"].values

# ---- Fit polynomial ----
deg =  int(input("Enter polynomial degree: "))
coeffs = np.polyfit(x, y, deg=deg)
print("Coefficients:", coeffs)

p = np.poly1d(coeffs)
print("Polynomial:", p)

x_new = int(input("enter input data point: "))
y_pred = p(x_new)
print(f"Predicted y at x={x_new}: {y_pred:.2f}")
y_fit = p(x)

mse = np.mean((y - y_fit) ** 2)
rmse = np.sqrt(mse)

ss_total = np.sum((y - np.mean(y)) ** 2)
ss_res = np.sum((y - y_fit) ** 2)
r2 = 1 - ss_res / ss_total

print(f"MSE  = {mse:.3f}")
print(f"RMSE = {rmse:.3f}")
print(f"R²   = {r2:.4f}")
x_smooth = np.linspace(min(x)-0.5, max(x)+1.5, 200)
y_smooth = p(x_smooth)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Original data points (from CSV)')
plt.plot(x_smooth, y_smooth, color='blue', label=f'Degree {deg} fit')
plt.scatter([x_new], [y_pred], color='green', marker='*', s=150, label=f'Prediction at x={x_new}')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Polynomial Regression (Degree {deg}) from CSV Data')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()