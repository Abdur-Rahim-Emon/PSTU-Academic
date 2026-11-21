import random
import math

# Multi-peak objective function
def f(x):
    return x * math.sin(x)

# Generate neighbors with some randomness
def get_neighbors(x):
    # Neighbors are ±1, ±2
    return [x - 2, x - 1, x + 1, x + 2]

# -------------------------
# 1. Simple Hill Climbing
# -------------------------
def hill_climbing(start):
    current = start
    while True:
        neighbors = get_neighbors(current)
        next_state = max(neighbors, key=f)
        if f(next_state) <= f(current):
            return current
        current = next_state

# -------------------------
# 2. First-Choice Hill Climbing
# -------------------------
def first_choice_hill_climbing(start, max_attempts=100):
    current = start
    while True:
        improved = False
        for _ in range(max_attempts):
            neighbor = random.choice(get_neighbors(current))
            if f(neighbor) > f(current):
                current = neighbor
                improved = True
                break
        if not improved:
            return current

# -------------------------
# 3. Stochastic Hill Climbing
# -------------------------
def stochastic_hill_climbing(start):
    current = start
    while True:
        neighbors = get_neighbors(current)
        better_neighbors = [n for n in neighbors if f(n) > f(current)]
        if not better_neighbors:
            return current
        current = random.choice(better_neighbors)

# -------------------------
# 4. Random-Restart Hill Climbing
# -------------------------
def random_restart_hill_climbing(restarts=5):
    best_solution = None
    best_value = float('-inf')
    for _ in range(restarts):
        start = random.randint(-10, 10)
        result = hill_climbing(start)
        if f(result) > best_value:
            best_solution = result
            best_value = f(result)
    return best_solution, best_value

# -------------------------
# Run experiments
# -------------------------
start = random.randint(-10, 10)
print("Start:", start)
print("Simple HC result:", hill_climbing(start), "Value:", f(hill_climbing(start)))
print("First-Choice HC result:", first_choice_hill_climbing(start), "Value:", f(first_choice_hill_climbing(start)))
print("Stochastic HC result:", stochastic_hill_climbing(start), "Value:", f(stochastic_hill_climbing(start)))
solution, value = random_restart_hill_climbing(10)
print("Random-Restart HC best x:", solution, "Maximum value:", value)
input("Press Enter to exit...")
