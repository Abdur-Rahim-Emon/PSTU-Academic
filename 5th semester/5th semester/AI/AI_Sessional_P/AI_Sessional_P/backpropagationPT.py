import torch
import torch.nn as nn
import torch.optim as optim

# Data
X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float32)
y = torch.tensor([[0],[1],[1],[0]], dtype=torch.float32)

# Model
model = nn.Sequential(
    nn.Linear(2,2),
    nn.Sigmoid(),
    nn.Linear(2,1),
    nn.Sigmoid()
)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.5)

# Training
for epoch in range(10000):

    output = model(X)

    loss = criterion(output, y)

    optimizer.zero_grad()
    loss.backward()      # Automatic Backpropagation
    optimizer.step()

print(model(X).detach())