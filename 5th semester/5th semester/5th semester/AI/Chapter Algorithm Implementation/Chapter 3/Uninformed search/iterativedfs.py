# Tree definition
tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Depth-Limited DFS function
def dfs_limited(tree, node, limit, visited):
    if node not in visited and limit > 0:
        print(node, end=" ")
        visited.append(node)
        for neighbor in tree[node]:
            dfs_limited(tree, neighbor, limit-1, visited)

# Iterative Deepening DFS function
def iterative_deepening(tree, start, max_limit):
    for i in range(1, max_limit + 1):  # depth from 1 to max_limit
        print(f"Iteration {i} : ", end="")
        dfs_limited(tree, start, i, [])
        print()

# Run IDDFS with maximum depth 4
iterative_deepening(tree, 'A', 4)