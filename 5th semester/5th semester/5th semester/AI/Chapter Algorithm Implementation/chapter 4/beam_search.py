class Problem:
    def __init__(self):
        # Tree structure (Adjacency list)
        self.tree = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': [],
            'E': [],
            'F': [],
            'G': []
        }

        # Heuristic values
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


def local_beam_search(problem, initial_states, k=2):
    states = initial_states

    iteration = 0
    while True:
        iteration += 1

        print(f"\nIteration {iteration}")
        print("Current states:", states)

        # Goal check
        for state in states:
            if state == problem.goal:
                print("Goal Found:", state)
                return state

        # Generate all successors
        all_neighbors = []
        for state in states:
            neighbors = problem.get_neighbors(state)
            all_neighbors.extend(neighbors)

        # If no more neighbors → stop
        if not all_neighbors:
            print("No solution found")
            return None

        # Sort based on heuristic
        all_neighbors.sort(key=lambda x: problem.heuristic(x))

        # Select best k
        states = all_neighbors[:k]


# 🔹 Run Example
problem = Problem()

# Start from root A (beam width k=2)
result = local_beam_search(problem, initial_states=['A'], k=2)

print("\nFinal Result:", result)