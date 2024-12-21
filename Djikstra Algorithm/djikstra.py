def dijkstra(graph, start, end):
    unvisited = {node: float('inf') for node in graph}
    unvisited[start] = 0
    visited = {}
    previous_nodes = {node: None for node in graph}

    while unvisited:
        current_node = min(unvisited, key=unvisited.get)
        current_distance = unvisited[current_node]

        if current_node == end:
            visited[current_node] = current_distance
            break

        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < unvisited[neighbor]:
                    unvisited[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node

        visited[current_node] = current_distance
        unvisited.pop(current_node)

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, visited[end] if end in visited else float('inf')

graph = {
    1: [(2, 5), (4, 6), (5, 10), (3,3)],
    2: [(6, 9), (5, 7)],
    3: [(5, 2), (6, 4), (8, 6)],
    4: [(6, 3), (7, 8)],
    5: [(7, 5), (8, 3)],
    6: [(7, 11), (8, 7)],
    7: [(8, 4)],
    8: []
}

for end_node in graph:
    path, cost = dijkstra(graph, 1, end_node)
    if path:
        path_str = " -> ".join(map(str, path))
        print(f"Jarak terpendek dari 1 ke {end_node}: {cost}")
        print(f"Path: {path_str}\n")
    else:
        print(f"Jarak terpendek dari 1 ke {end_node}: Tidak Tersedia\n")

print(f"Jalur tercepat: {path}")
print(f"Jarak total: {cost}")
