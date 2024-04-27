def bellman_ford(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaxation step
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]

    #Negative cycles
    for u in graph:
        for v in graph[u]:
            if distances[u] + graph[u][v] < distances[v]:
                raise ValueError("Graph contains negative cycle")

    return distances

# Example Figure 24.4 from Page 652:
graph = {
    'S': {'T': 6, 'Y': 7},
    'T': {'X': 5, 'Y': 8, 'Z': -4},
    'X': {'T':-2},
    'Y': {'X': -3, 'Z': 9},
    'Z': {'S': 2, 'X':7}
}

start_node = 'S'
try:
    shortest_distances = bellman_ford(graph, start_node)
    print("Shortest distances from", start_node + ":")
    for node, distance in shortest_distances.items():
        print(node + ":", distance)
except ValueError as e:
    print(e)
