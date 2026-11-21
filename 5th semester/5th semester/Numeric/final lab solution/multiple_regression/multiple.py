import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([
    [1000, 2, 1],
    [1200, 3, 2],
    [1500, 3, 3],
    [1700, 4, 3],
    [850,  2, 1],
    [1400, 3, 2],
    [2000, 5, 3]
])

# Price (Lakh BDT)
y = np.array([30, 45, 65, 75, 25, 55, 95])

model = LinearRegression()
model.fit(X, y)

# Get Equation intercept

intercept = model.intercept_
# Get Equation coefficient
coef = model.coef_

print("Final Equation:\n")
print(f"Price = {intercept:.2f}"
      f" + ({coef[0]:.4f} × Area)"
      f" + ({coef[1]:.4f} × Rooms)"
      f" + ({coef[2]:.4f} × LocationCode)")


# Take User Input

print("\nEnter House Information")

area = float(input("Area (sq ft): "))
rooms = float(input("Number of Rooms: "))
location = int(input("Location (1=Rural, 2=Suburban, 3=Urban): "))

new_house = np.array([[area, rooms, location]])

predicted_price = model.predict(new_house)

print(f"\nPredicted House Price = {predicted_price[0]:.2f} Lakh BDT")

#plot 
y_pred = model.predict(X)

plt.figure(figsize=(6,6))
plt.scatter(y, y_pred, color="blue", s=80)

min_val = min(y.min(), y_pred.min())
max_val = max(y.max(), y_pred.max())

plt.plot([min_val, max_val],
         [min_val, max_val],
         "r--")

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Price")
plt.grid(True)
plt.show()