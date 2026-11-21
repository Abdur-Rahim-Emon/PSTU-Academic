import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ---------- Sample dataset (replaces reading from CSV) ----------
# Temperature (X) vs Pressure (y) - made up sample data
data_dict = {
    "Temperature": [1, 2, 3, 4, 5, 6],
    "Pressure":    [0.15, 0.25, 0.25, 0.15, 0.12, 0.08]
}

#[1, 2, 3, 4, 5, 6], size=78, p=[0.15, 0.25, 0.25, 0.15, 0.12, 0.08]
datas = pd.DataFrame(data_dict)
datas

"""
datas = pd.read_csv('/content/data.csv')
datas
"""

X = datas.iloc[:, 0:1].values   # Temperature column as 2 d array
y = datas.iloc[:, 1].values     # Pressure column 1 d array

lin = LinearRegression()
lin.fit(X, y)

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)

# ---------- Plot: Linear Regression ----------
plt.scatter(X, y, color='blue')
plt.plot(X, lin.predict(X), color='red')
plt.title('Linear Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.show()

# ---------- Plot: Polynomial Regression ----------
plt.scatter(X, y, color='blue')
plt.plot(X, lin2.predict(poly.fit_transform(X)), color='red')
plt.title('Polynomial Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.show()

# ---------- Predictions for a new Temperature value ----------
pred = 5.5
predarray = np.array([[pred]])
print("Linear Regression prediction:", lin.predict(predarray))

pred2 = 5.5
pred2array = np.array([[pred2]])
print("Polynomial Regression prediction:", lin2.predict(poly.fit_transform(pred2array)))