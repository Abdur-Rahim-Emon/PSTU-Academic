import torch
import torch.nn as nn
import torch.optim as optim

# XOR Data
X = torch.tensor([[0.,0.],
                  [0.,1.],
                  [1.,0.],
                  [1.,1.]])

y = torch.tensor([[0.],
                  [1.],
                  [1.],
                  [0.]])

# Model
model = nn.Sequential(
    nn.Linear(2,2),
    nn.Sigmoid(),
    nn.Linear(2,1),
    nn.Sigmoid()
)

# Loss + Optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.5)

# Train
for epoch in range(10000):

    output = model(X)

    loss = criterion(output, y)

    optimizer.zero_grad()
    loss.backward()   # automatic backpropagation
    optimizer.step()

# Output
print(model(X).detach())