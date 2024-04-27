import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    #Implemented using a Priority Queue
    priority_queue = [(0, start)]

    previous = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

# Example 24.6 from Page 659:
graph = {
    'S': {'T': 10, 'Y': 5, 'Z':7},
    'T': {'X':1, 'Y':2},
    'X': {'Z': 4},
    'Y': {'Z': 2, 'T': 3, 'X': 9},
    'Z': {'S': 7, 'X': 6}
}

start_node = 'S'
distances, previous = dijkstra(graph, start_node)

print("Distances from", start_node + ":")
for node, distance in distances.items():
    print(node + ":", distance)

print("\nPrevious nodes:")
for node, prev_node in previous.items():
    print(node + ":", prev_node)
