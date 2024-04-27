def floyd_warshall(graph):
    distance = {u: {v: float('inf') if u != v else 0 for v in graph} for u in graph}
    
    # Use of matrix
    for u in graph:
        for v in graph[u]:
            distance[u][v] = graph[u][v]

    #Shortest paths
    for k in graph:
        for i in graph:
            for j in graph:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# Example Figure 25.1 from Page 690:
graph = {
    '1': {'2': 3, '3':8, '5':-4},
    '2': {'5': 7, '4':1},
    '3': {'2':4},
    '4': {'3':-5, '1':2},
    '5': {'4':6}
}

all_pairs_shortest_paths = floyd_warshall(graph)
for u in graph:
    for v in graph:
        print(f"Shortest path from {u} => {v}: {all_pairs_shortest_paths[u][v]}")
    print()
