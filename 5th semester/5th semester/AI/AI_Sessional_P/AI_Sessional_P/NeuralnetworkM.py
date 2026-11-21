import math
import random

# Activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative
def sigmoid_derivative(output):
    return output * (1 - output)

# XOR dataset
data = [
    ([0,0], 0),
    ([0,1], 1),
    ([1,0], 1),
    ([1,1], 0)
]

random.seed(1)

# Weights Input -> Hidden
w1 = random.uniform(-1,1)
w2 = random.uniform(-1,1)
w3 = random.uniform(-1,1)
w4 = random.uniform(-1,1)

# Weights Hidden -> Output
w5 = random.uniform(-1,1)
w6 = random.uniform(-1,1)

# Biases
b1 = random.uniform(-1,1)
b2 = random.uniform(-1,1)
b3 = random.uniform(-1,1)

lr = 0.5
epochs = 10000

for epoch in range(epochs):

    for x, target in data:

        x1 = x[0]
        x2 = x[1]

        # ---------- Forward Pass ----------
        h1 = sigmoid(x1*w1 + x2*w2 + b1)
        h2 = sigmoid(x1*w3 + x2*w4 + b2)

        output = sigmoid(h1*w5 + h2*w6 + b3)

        # ---------- Error ----------
        error = target - output

        # ---------- Backpropagation ----------
        delta_output = error * sigmoid_derivative(output)

        delta_h1 = delta_output * w5 * sigmoid_derivative(h1)
        delta_h2 = delta_output * w6 * sigmoid_derivative(h2)

        # Update weights Hidden -> Output
        w5 += lr * delta_output * h1
        w6 += lr * delta_output * h2

        # Update weights Input -> Hidden
        w1 += lr * delta_h1 * x1
        w2 += lr * delta_h1 * x2
        w3 += lr * delta_h2 * x1
        w4 += lr * delta_h2 * x2

        # Update biases
        b1 += lr * delta_h1
        b2 += lr * delta_h2
        b3 += lr * delta_output

# Final Result
print("Predictions:")
for x, target in data:
    x1 = x[0]
    x2 = x[1]

    h1 = sigmoid(x1*w1 + x2*w2 + b1)
    h2 = sigmoid(x1*w3 + x2*w4 + b2)

    output = sigmoid(h1*w5 + h2*w6 + b3)

    print(x, "=>", round(output,3))