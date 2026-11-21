import heapq

# 🔹 Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3)],
    'C': [('D', 1)],
    'D': []  # Goal node exists
}

# 🔹 Heuristic
h = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0  # Goal heuristic = 0
}

def a_star(graph, heuristic, start, goal):
    frontier = []
    # (f, g, node, path)
    heapq.heappush(frontier, (heuristic[start], 0, start, [start]))

    # Best g(n) cost for each node
    best_graph = {start: 0}

    while frontier:
        f, g_cost, node, path_list = heapq.heappop(frontier)

        print("Expanding:", node)

        if node == goal:
            return g_cost, path_list

        for neighbor, neighbor_cost in graph[node]:
            new_g = g_cost + neighbor_cost

            # If neighbor not visited OR found better path
            if neighbor not in best_graph or new_g < best_graph[neighbor]:
                best_graph[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(frontier, (new_f, new_g, neighbor, path_list + [neighbor]))

    return None, []

# 🔹 Run A* from A to D
cost, path = a_star(graph, h, 'A', 'D')

print("Path :", " -> ".join(path))
print("Cost :", cost)