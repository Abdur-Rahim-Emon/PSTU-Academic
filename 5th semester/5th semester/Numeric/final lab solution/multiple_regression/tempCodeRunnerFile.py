import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Dataset
# -----------------------------
X = np.array([
    [1000,2,1],
    [1200,3,2],
    [1500,3,3],
    [1700,4,3],
    [850,2,1],
    [1400,3,2],
    [2000,5,3]
], dtype=float)

y = np.array([30,45,65,75,25,55,95], dtype=float)

# -----------------------------
# Train Model
# -----------------------------
X_bias = np.hstack((np.ones((X.shape[0],1)), X))
beta = np.linalg.inv(X_bias.T @ X_bias) @ X_bias.T @ y

print("\nRegression Coefficients:")
print(beta)

print("\nFinal Model")
print(f"Price = {beta[0]:.4f} + ({beta[1]:.4f})*Area + ({beta[2]:.4f})*Rooms + ({beta[3]:.4f})*Location")

# -----------------------------
# Prediction
# -----------------------------
y_pred = X_bias @ beta

# -----------------------------
# User Input
# -----------------------------
print("\nEnter New House Information")

area = float(input("Area: "))
rooms = float(input("Rooms: "))
location = float(input("Location (1/2/3): "))

sample = np.array([1, area, rooms, location])

price = sample @ beta

print(f"\nPredicted House Price = {price:.2f} Lakh BDT")

# -----------------------------
# Graph 1
# -----------------------------
plt.figure(figsize=(6,5))
plt.scatter(y, y_pred, s=80)

mn = min(y.min(), y_pred.min())
mx = max(y.max(), y_pred.max())

plt.plot([mn,mx],[mn,mx],'r--')
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.grid(True)
plt.show()

# -----------------------------
# Graph 2
# -----------------------------
error = y - y_pred

plt.figure(figsize=(7,4))
plt.bar(range(len(error)), error)
plt.xlabel("House")
plt.ylabel("Error")
plt.title("Prediction Error")
plt.grid(True)
plt.show()

# -----------------------------
# Graph 3
# -----------------------------
plt.figure(figsize=(6,5))
plt.scatter(X[:,0], y, s=80, label="Actual")
plt.scatter(X[:,0], y_pred, marker='x', s=80, label="Predicted")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.legend()
plt.grid(True)
plt.show()