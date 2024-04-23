class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        i = 0  # Index for sorted edges
        e = 0  # Index for result[]

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


g = Graph(9)
node_indices = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
g.add_edge(node_indices['a'], node_indices['b'], 4)  # a-b
g.add_edge(node_indices['a'], node_indices['h'], 8)  # a-h
g.add_edge(node_indices['b'], node_indices['h'], 11) # b-h
g.add_edge(node_indices['b'], node_indices['c'], 8)  # b-c
g.add_edge(node_indices['h'], node_indices['i'], 7)  # h-i
g.add_edge(node_indices['g'], node_indices['h'], 1)  # g-h
g.add_edge(node_indices['g'], node_indices['i'], 6)  # g-i
g.add_edge(node_indices['c'], node_indices['i'], 2)  # c-i
g.add_edge(node_indices['c'], node_indices['f'], 4)  # c-f
g.add_edge(node_indices['c'], node_indices['d'], 7)  # c-d
g.add_edge(node_indices['f'], node_indices['d'], 14) # f-d
g.add_edge(node_indices['f'], node_indices['e'], 10) # f-e
g.add_edge(node_indices['d'], node_indices['e'], 9)  # d-e

mst = g.kruskal()
print("Edges in the MST:")
for u, v, weight in mst:
    print(f"{chr(97 + u)} - {chr(97 + v)} : {weight}") 
