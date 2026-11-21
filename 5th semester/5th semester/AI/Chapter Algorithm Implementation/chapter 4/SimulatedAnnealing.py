import random
import math

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

        self.h = {
            'A': 6,
            'B': 4,
            'C': 5,
            'D': 2,
            'E': 3,
            'F': 1,
            'G': 0
        }

        self.goal = 'G'

    def get_neighbors(self, node):
        return self.tree[node]

    def heuristic(self, node):
        return self.h[node]


def simulated_annealing(problem, start, T=10, cooling_rate=0.95):
    current = start

    while T > 0.1:
        print(f"Current: {current}, T={T:.2f}")

        if current == problem.goal:
            print("Goal Found:", current)
            return current

        neighbors = problem.get_neighbors(current)
        if not neighbors:
            return current

        # Pick random neighbor
        next_node = random.choice(neighbors)

        delta = problem.heuristic(next_node) - problem.heuristic(current)

        # If better → accept
        if delta < 0:
            current = next_node
        else:
            # Accept worse with probability
            probability = math.exp(-delta / T)
            if random.random() < probability:
                current = next_node

        # Decrease temperature
        T *= cooling_rate

    return current


# 🔹 Run
problem = Problem()
result = simulated_annealing(problem, 'A')

print("Final Result:", result)