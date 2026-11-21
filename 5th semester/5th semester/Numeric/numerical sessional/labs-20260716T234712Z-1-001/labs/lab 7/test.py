import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Read data from CSV ----
data = pd.read_csv("rui_fish_dataset.csv")   # <-- put your CSV filename here
x = data["Age"].values
y = data["Length_mm"].values

# ---- Fit polynomial (change deg=1 to deg=2, deg=3 etc as needed) ----
deg = 3
coeffs = np.polyfit(x, y, deg=deg)
print("Coefficients:", coeffs)

p = np.poly1d(coeffs)
print("Polynomial:", p)

# ---- Predict for a new x value ----
x_new = 6
y_pred = p(x_new)
print(f"Predicted y at x={x_new}: {y_pred:.2f}")

# ---- Plot ----
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