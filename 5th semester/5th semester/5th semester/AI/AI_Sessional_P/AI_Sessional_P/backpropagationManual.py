import random
import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(output):
    return output * (1 - output)

# XOR dataset
training_data = [
    ([0, 0], [0]),
    ([0, 1], [1]),
    ([1, 0], [1]),
    ([1, 1], [0])
]

# Random seed
random.seed(1)

# Input layer (2 neurons)
# Hidden layer (2 neurons)
# Output layer (1 neuron)

# Weights Input -> Hidden
w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()

# Weights Hidden -> Output
w5 = random.random()
w6 = random.random()

# Bias
b1 = random.random()
b2 = random.random()
b3 = random.random()

# Learning rate
lr = 0.5

# Training
epochs = 10000

for epoch in range(epochs):

    total_error = 0

    for inputs, target in training_data:

        x1 = inputs[0]
        x2 = inputs[1]
        y = target[0]

        # ---------- Forward Propagation ----------

        # Hidden layer
        h1_input = x1*w1 + x2*w2 + b1
        h1_output = sigmoid(h1_input)

        h2_input = x1*w3 + x2*w4 + b2
        h2_output = sigmoid(h2_input)

        # Output layer
        o1_input = h1_output*w5 + h2_output*w6 + b3
        o1_output = sigmoid(o1_input)

        # ---------- Error ----------
        error = y - o1_output
        total_error += error**2

        # ---------- Backpropagation ----------

        # Output neuron delta
        delta_output = error * sigmoid_derivative(o1_output)

        # Hidden neuron deltas
        delta_h1 = delta_output * w5 * sigmoid_derivative(h1_output)
        delta_h2 = delta_output * w6 * sigmoid_derivative(h2_output)

        # ---------- Update Weights ----------

        # Hidden -> Output
        w5 += lr * delta_output * h1_output
        w6 += lr * delta_output * h2_output

        # Input -> Hidden
        w1 += lr * delta_h1 * x1
        w2 += lr * delta_h1 * x2

        w3 += lr * delta_h2 * x1
        w4 += lr * delta_h2 * x2

        # Update Bias
        b3 += lr * delta_output
        b1 += lr * delta_h1
        b2 += lr * delta_h2

    # Print every 1000 epoch
    if epoch % 1000 == 0:
        print("Epoch:", epoch, "Error:", total_error)

# ---------- Final Output ----------
print("\nFinal Predictions:")

for inputs, target in training_data:

    x1 = inputs[0]
    x2 = inputs[1]

    h1 = sigmoid(x1*w1 + x2*w2 + b1)
    h2 = sigmoid(x1*w3 + x2*w4 + b2)

    output = sigmoid(h1*w5 + h2*w6 + b3)

    print(inputs, "=>", round(output, 3))