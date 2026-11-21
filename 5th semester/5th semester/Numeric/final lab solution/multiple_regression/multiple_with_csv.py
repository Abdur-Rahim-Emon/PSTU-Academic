import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# CSV file path
csv_path = os.path.join(script_dir, "house_data.csv")

# Read CSV
data = pd.read_csv(csv_path)

# ---------------------------------
# Select Features (X) and Target (y)
# ---------------------------------

X = data[["Area", "Rooms", "Location"]].values
y = data["Price"].values

# Train Model
model = LinearRegression()
model.fit(X, y)
# Get Equation
intercept = model.intercept_
coef = model.coef_

print("\nFinal Equation:\n")

print(f"Price = {intercept:.2f}"
      f" + ({coef[0]:.4f} × Area)"
      f" + ({coef[1]:.4f} × Rooms)"
      f" + ({coef[2]:.4f} × Location)")

# ---------------------------------
# User Input
print("\nEnter House Information")

area = float(input("Area (sq ft): "))
rooms = float(input("Number of Rooms: "))
location = int(input("Location (1=Rural, 2=Suburban, 3=Urban): "))

new_house = np.array([[area, rooms, location]])

predicted_price = model.predict(new_house)

print(f"\nPredicted House Price = {predicted_price[0]:.2f} Lakh BDT")
# Predict Training Data

y_pred = model.predict(X)
# Plot
plt.figure(figsize=(6,6))
plt.scatter(y, y_pred, color="blue", s=80)

min_val = min(y.min(), y_pred.min())
max_val = max(y.max(), y_pred.max())

plt.plot([min_val, max_val],
         [min_val, max_val],
         "r--",
         linewidth=2)

plt.xlabel("Actual Price (Lakh BDT)")
plt.ylabel("Predicted Price (Lakh BDT)")
plt.title("Actual vs Predicted House Price")
plt.grid(True)

plt.show()