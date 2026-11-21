import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 1. Recreate the dataset environment (n = 78 Rui Fish from PSTU Pond)
np.random.seed(2023)
age = np.random.choice([1, 2, 3, 4, 5, 6], size=78, p=[0.15, 0.25, 0.25, 0.15, 0.12, 0.08])
length = 150 + 110 * age - 9 * (age ** 2) + np.random.normal(0, 25, size=78)

X = age.reshape(-1, 1)
y = length

# 2. Train the Polynomial Regression Model (Degree = 2)
degree = 2
poly_features = PolynomialFeatures(degree=degree, include_bias=False)
X_poly = poly_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Extract final mathematical parameters
intercept = model.intercept_
w1, w2 = model.coef_

print("--- MODEL TRAINING COMPLETE ---")
print(f"Predicted Function: Length = {intercept:.2f} + ({w1:.2f} * Age) + ({w2:.2f} * Age^2)\n")

# 3. Interactive Prediction Loop for Random Values
print("--------------------------------------------------")
print("RUI FISH LENGTH PREDICTOR (Type 'exit' to quit)")
print("--------------------------------------------------")

while True:
    user_input = input("Enter a random fish age in years (e.g., 3.5): ").strip()
    
    if user_input.lower() == 'exit':
        print("Exiting predictor. Goodbye!")
        break
        
    try:
        # Convert input to float
        random_age = float(user_input)
        
        if random_age < 0:
            print("Age cannot be negative. Please try again.")
            continue
            
        # Format input for the model [[age]]
        input_array = np.array([[random_age]])
        
        # Crucial step: transform the custom age into [age, age^2]
        input_poly = poly_features.transform(input_array)
        
        # Run prediction through the trained function
        predicted_length = model.predict(input_poly)[0]
        
        print(f"-> Predicted Length for a {random_age}-year-old fish: {predicted_length:.2f} mm\n")
        
    except ValueError:
        print("Invalid input! Please enter a valid number or type 'exit'.\n")