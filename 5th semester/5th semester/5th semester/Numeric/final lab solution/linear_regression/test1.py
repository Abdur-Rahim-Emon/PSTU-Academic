import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_data.csv")

data = pd.read_csv(csv_path)

x = data["x"].values.reshape(-1, 1)
y = data["y"].values.reshape(-1, 1)
def gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=10000):
    n = len(y)#coutn the trainning samples
    for epoch in range(epochs):
        # Predict y
        y_pred = m * x + b

        # Calculate gradients
        dm = (-2 / n) * np.sum(x * (y - y_pred))
        db = (-2 / n) * np.sum(y - y_pred)

        m = m - learning_rate * dm
        b = b - learning_rate * db
    return m, b

m, b = gradient_descent(x, y)
#output 

print("\n========== MODEL TRAINED ==========")
print(f"Slope (m)      : {m:.4f}")
print(f"Intercept (b)  : {b:.4f}")
print(f"Model Equation : y = {m:.4f}x + {b:.4f}")
#sample test

x_input = float(input("\nEnter the value of X: "))

y_prediction = m * x_input + b

print("----------------------------------")
print(f"For X = {x_input}")
print(f"Predicted Y = {y_prediction:.4f}")
print("----------------------------------")

y_pred = m * x + b

#plot
plt.figure(figsize=(8, 5))#sset height , weight

plt.scatter(x, y, color="blue", label="Training Data")## plot input 
#plot the output
plt.plot(x, y_pred, color="red", linewidth=0.9, label="Regression Line")

# Show the user's prediction
plt.scatter(x_input, y_prediction, color="green", s=120,
            label=f"Prediction ({x_input}, {y_prediction:.2f})")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression using Gradient Descent")
plt.legend()
plt.grid(True)

plt.show()