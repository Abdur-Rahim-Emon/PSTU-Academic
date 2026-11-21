import random

class Problem:
    def __init__(self):
        self.tree = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': [],
            'E': [],
            'F': [],
            'G': []
        }
        self.goal = 'G'

    def get_neighbors(self, node):
        return self.tree[node]

def stochastic_search(problem, start, max_steps=20):
    current = start
    path = [current]

    for step in range(max_steps):
        print(f"Step {step+1}: Current Node = {current}")

        # Check goal
        if current == problem.goal:
            print("Goal Found!")
            return path

        neighbors = problem.get_neighbors(current)
        if not neighbors:
            print("No neighbors to move, stopping.")
            break

        # Pick random neighbor
        current = random.choice(neighbors)
        path.append(current)

    print("Max steps reached, stopping.")
    return path

# 🔹 Run
problem = Problem()
result_path = stochastic_search(problem, 'A')
print("Path taken:", " -> ".join(result_path))