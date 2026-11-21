# =========================================================
# POLYNOMIAL REGRESSION - BEGINNER FRIENDLY VERSION
# =========================================================
# This program teaches a computer to find a curved line
# (a polynomial) that best fits some data points.
# Then it lets you type a new x value and predicts y for it.

# ---------- STEP 1: Import the tools we need ----------
import numpy as np                                    # for math and arrays
import pandas as pd                                    # for reading CSV files (used later)
import matplotlib.pyplot as plt                        # for drawing graphs
from sklearn.preprocessing import PolynomialFeatures    # turns x into x, x^2, x^3
from sklearn.linear_model import LinearRegression       # the model that learns the equation
from sklearn.metrics import r2_score, mean_squared_error  # to check how good the model is


# ---------- STEP 2: Get the data (x and y values) ----------

# OPTION 1: Use sample/fake data (this is ON right now)
# We make up 30 points that follow a curved pattern, plus some random noise.
np.random.seed(42)                          # keeps the "random" numbers the same every time we run it
x = np.linspace(1, 10, 30)                  # 30 numbers evenly spaced between 1 and 10
y = 0 + 10* x - 0.6 * x**2 + 0.08 * x**3 + np.random.normal(0, 3, size=x.shape)
x = x.reshape(-1, 1)                        # sklearn needs x to be a column, not a flat list

# OPTION 2: Use your own CSV file instead (this is OFF right now)
# To turn this on:
#   1. Put a "#" in front of the 4 lines above (Option 1)
#   2. Remove the "#" in front of the 5 lines below
#   3. Change "your_dataset.csv" and the column names to match your file
#
# data = pd.read_csv("your_dataset.csv")
# data = data.dropna()                      # removes empty/missing rows
# x = data["x_column_name"].values
# y = data["y_column_name"].values
# x = x.reshape(-1, 1)


# ---------- STEP 3: Turn x into x, x^2, x^3 ----------
# A straight-line model can only draw a straight line.
# To draw a curve, we also give the model x^2 and x^3 as extra inputs.
degree = 3
poly_maker = PolynomialFeatures(degree=degree, include_bias=False)
x_poly = poly_maker.fit_transform(x)


# ---------- STEP 4: Train (teach) the model ----------
model = LinearRegression()
model.fit(x_poly, y)   # this is where the "learning" happens


# ---------- STEP 5: Show the equation the model learned ----------
# The model gives us 4 numbers: a, b, c, d
a = model.intercept_
b = model.coef_[0]
c = model.coef_[1]
d = model.coef_[2]

print("=" * 55)
print("The equation the model learned:")
print("=" * 55)
print(f"y = {a:.4f} + ({b:.4f})x + ({c:.4f})x^2 + ({d:.4f})x^3")
print()


# ---------- STEP 6: Check how good the model is ----------
y_predicted_for_training_data = model.predict(x_poly)

r2 = r2_score(y, y_predicted_for_training_data)
mse = mean_squared_error(y, y_predicted_for_training_data)
rmse = np.sqrt(mse)

print("How good is the model?")
print("-" * 55)
print(f"R2 Score : {r2:.4f}   (1.0 = perfect fit)")
print(f"MSE      : {mse:.4f}   (lower is better)")
print(f"RMSE     : {rmse:.4f}   (lower is better)")
print()


# ---------- STEP 7: Ask the user for a new x and predict y ----------
try:
    x_new_text = input("Enter a new x value to predict y: ")
    x_new = float(x_new_text)

    # We must transform x_new the same way we transformed the training data
    x_new_as_array = np.array([[x_new]])
    x_new_poly = poly_maker.transform(x_new_as_array)

    # Ask the model to predict y
    y_predicted = model.predict(x_new_poly)[0]

    # Double check by using the equation directly (should give the same answer)
    y_from_equation = a + b * x_new + c * x_new**2 + d * x_new**3

    print()
    print("Prediction:")
    print("-" * 55)
    print(f"x = {x_new}")
    print(f"y predicted by the model  = {y_predicted:.4f}")
    print(f"y from the equation above = {y_from_equation:.4f}")
    print("(These two match, which shows the model follows its own equation.)")

except ValueError:
    print("That was not a valid number. Skipping the prediction step.")
    x_new = None
    y_predicted = None


# ---------- STEP 8: Draw a graph ----------
# Make a smooth curve by predicting y for many closely spaced x values
x_line = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
x_line_poly = poly_maker.transform(x_line)
y_line = model.predict(x_line_poly)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="blue", label="Original data points")
plt.plot(x_line, y_line, color="red", linewidth=2, label="Fitted curve")

if x_new is not None:
    plt.scatter([x_new], [y_predicted], color="green", s=120,
                marker="*", label="Your predicted point")

plt.title("Polynomial Regression (degree 3)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("polynomial_regression_plot.png", dpi=150)   # saves the graph as an image
plt.show()                                                # opens the graph on screen

print()
print("Graph saved as 'polynomial_regression_plot.png'")