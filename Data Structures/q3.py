"""
detect_tricycle: this method detects a tricycle in the graph. It iterates through each node and its neighbors, checs if any 
two neighbors are also connected. If such a set of three vertices is found, it returns the vertices making the tricycle.
The worst-case running time is O(V * E). This is because for each vertex, it checks all pairs of its neighbors.
The space utilization is O(V + E), for storing the adjacenc list and the set of neighbors.
"""
"""
Execution:    python graph.py graph.txt
Data files:   graph.txt

A graph, implemented using an array of sorted lists.
The sort is unnecessary but can aid debugging.
"""

class Graph:
    def __init__(self, v=None, filename=None):
        if filename is None:
            self.V = v
            self.E = 0
            self.adj = [list() for i in range(self.V)]
        else:
            infile = open(filename, "r")
            self.V = int(infile.readline())
            self.E = 0

            self.adj = [list() for i in range(self.V)]
            E = int(infile.readline())
            for _ in range(E):
                v, w = infile.readline().split()
                self.add_edge(v, w)
            infile.close()
            self.sort_adj()

    def sort_adj(self):
        for adj in self.adj:
            adj.sort()

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join(
            "%d: %s" % (v, " ".join(str(w) for w in self.adj[v]))
            for v in range(self.V)
        )
        return s

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adjacent(self, v):
        return self.adj[v]

    def edges(self):
        result = set()
        for u in range(self.V):
            for v in self.adj[u]:
                if (v, u) not in result:
                    result.add((u, v))
        return result

    def detect_tricycle(self): 
        for node in range(self.V):
            nbrs = set(self.adj[node])
            for nbr1 in self.adj[node]:
                for nbr2 in self.adj[nbr1]:
                    if nbr2 in nbrs and nbr2 != node and nbr1 != node:
                        return [node, nbr1, nbr2]
        return []

if __name__ == '__main__':
    import os

    g = Graph(9)
    edges = [
        (0, 1), (3, 8), (1, 2), (1, 5), (3, 7),
        (0, 3), (1, 4), (6, 7), (0, 2), (4, 5), (3, 6)
    ]
    for v, w in edges:
        g.add_edge(v, w)
    g.sort_adj()
    print(g)

    current_file_path = os.path.dirname(__file__)
    try:
        g1 = Graph(filename=current_file_path + "/" + "graph.txt")
        print(g1)
    except FileNotFoundError:
        print("File 'graph.txt' not found.")