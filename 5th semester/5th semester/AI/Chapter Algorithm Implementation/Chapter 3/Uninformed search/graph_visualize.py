import matplotlib.pyplot as plt
import networkx as nx

tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

G = nx.DiGraph()

# add edges
for node in tree:
    for neighbor in tree[node]:
        G.add_edge(node, neighbor)

# manually define positions (TREE STRUCTURE)
pos = {
    'A': (0, 3),
    'B': (-1, 2),
    'E': (1, 2),
    'C': (-1.5, 1),
    'D': (-0.5, 1),
    'F': (-1.5, 0)
}

# draw
nx.draw(G, pos, with_labels=True)

plt.show()