from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self):
        start_time = {}
        finish_time = {}
        time = 1

        # Function to perform DFS traversal
        def DFS_visit(node):
            nonlocal time
            start_time[node] = time
            time += 1

            # Explore adjacent nodes
            for neighbor in self.graph[node]:
                if neighbor not in start_time:
                    DFS_visit(neighbor)

            finish_time[node] = time
            time += 1

        # Iterate over all nodes in the graph
        for node in self.graph:
            if node not in start_time:
                DFS_visit(node)

        return start_time, finish_time

g = Graph()
g.add_edge('u', 'v')
g.add_edge('u', 'x')
g.add_edge('x', 'v')
g.add_edge('v', 'y')
g.add_edge('y', 'x')
g.add_edge('w', 'y')
g.add_edge('w', 'z')
g.add_edge('z', 'z')

start_times, finish_times = g.DFS()
print("Start Times:", start_times)
print("Finish Times:", finish_times)
