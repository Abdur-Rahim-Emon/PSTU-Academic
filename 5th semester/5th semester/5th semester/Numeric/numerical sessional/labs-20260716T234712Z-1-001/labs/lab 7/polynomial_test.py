"""
Polynomial Regression: Fish Length vs. Age
--------------------------------------------
Response (y): length of fish (mm)
Predictor (x): age of fish (years)

This script:
1. Tries to download the real bluegill fish dataset (n=78) from Penn State.
2. If that fails (e.g. no internet), lets you paste in your own data.
3. Fits linear, quadratic, and cubic polynomial models and compares them.
4. Plots the data with each fitted curve.
5. Lets you predict the length of a fish at any given age.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# ---------------------------------------------------------
# Step 1: Load the data
# ---------------------------------------------------------
def load_data():
    url = "https://online.stat.psu.edu/onlinecourses/sites/stat501/files/data/bluegills.txt"
    try:
        df = pd.read_csv(url, sep="\t")
        df.columns = [c.strip().lower() for c in df.columns]
        print(f"Loaded {len(df)} rows from the online dataset.\n")
        return df["age"].values, df["length"].values
    except Exception as e:
        print("Could not download the dataset automatically "
              f"({e}).")
        print("Paste your own age/length data below instead.\n")
        # --- REPLACE THIS with your real dataset if download fails ---
        age = np.array([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11])
        length = np.array([67, 87, 82, 105, 108, 128, 122, 155, 149, 170,
                            165, 187, 178, 195, 190, 205, 199, 210, 206, 214])
        return age, length


age, length = load_data()


# ---------------------------------------------------------
# Step 2: Fit polynomial models of different degrees
# ---------------------------------------------------------
def fit_polynomial(x, y, degree):
    x = x.reshape(-1, 1)
    poly = PolynomialFeatures(degree)
    x_poly = poly.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)

    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)

    return model, poly, r2


results = {}
for degree in [1, 2, 3]:
    model, poly, r2 = fit_polynomial(age, length, degree)
    results[degree] = (model, poly, r2)
    print(f"Degree {degree} model -> R-squared = {r2:.4f}")

# pick the best-performing degree (highest R^2) as the "chosen" model
best_degree = max(results, key=lambda d: results[d][2])
best_model, best_poly, best_r2 = results[best_degree]
print(f"\nBest fit: degree {best_degree} polynomial (R-squared = {best_r2:.4f})")


# ---------------------------------------------------------
# Step 3: Plot the data with each fitted curve
# ---------------------------------------------------------
x_line = np.linspace(age.min(), age.max(), 200).reshape(-1, 1)

plt.figure(figsize=(8, 6))
plt.scatter(age, length, color="black", label="Observed data")

colors = {1: "green", 2: "red", 3: "blue"}
for degree, (model, poly, r2) in results.items():
    y_line = model.predict(poly.transform(x_line))
    plt.plot(x_line, y_line, color=colors[degree],
              label=f"Degree {degree} fit (R2={r2:.3f})")

plt.xlabel("Age (years)")
plt.ylabel("Length (mm)")
plt.title("Fish Length vs. Age - Polynomial Regression")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("fish_length_vs_age.png", dpi=150)
print("\nPlot saved to fish_length_vs_age.png")


# ---------------------------------------------------------
# Step 4: Predict length for a new age using the best model
# ---------------------------------------------------------
def predict_length(new_age, model=best_model, poly=best_poly):
    new_age_poly = poly.transform(np.array([[new_age]]))
    return model.predict(new_age_poly)[0]


print("\n--- Try a prediction ---")
while True:
    user_input = input("Enter a fish age to predict its length (or 'exit'): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    try:
        new_age = float(user_input)
        pred = predict_length(new_age)
        print(f"Predicted length at age {new_age} = {pred:.2f} mm\n")
    except ValueError:
        print("Please enter a valid number, or 'exit' to quit.\n")