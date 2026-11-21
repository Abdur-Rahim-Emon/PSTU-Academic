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


def hill_climbing(problem, start):
    current = start

    while True:
        print("Current:", current)

        # Goal check
        if current == problem.goal:
            print("Goal Found:", current)
            return current

        neighbors = problem.get_neighbors(current)

        # If no neighbors → stop
        if not neighbors:
            print("Reached local optimum:", current)
            return current

        # Choose best neighbor (minimum heuristic)
        next_node = min(neighbors, key=lambda x: problem.heuristic(x))

        # If no improvement → stop
        if problem.heuristic(next_node) >= problem.heuristic(current):
            print("Reached local optimum:", current)
            return current

        current = next_node


# 🔹 Run
problem = Problem()
result = hill_climbing(problem, 'A')

print("Final Result:", result)