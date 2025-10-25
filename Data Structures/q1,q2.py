"""
1.	validTopologicalOrder: This checks if the given sequence is a topological order of graph G. It maps each node to 
its position in sequence, then verifies if for every directed edge (v, w), v appears before w in the order. The time complexity
is O(V + E), here V is the number of vertices and E is the number of edges. The space complexity is O(V), for storing the node
position mapping.
2.	topological: This method finds a valid topological order for the graph. It calculates the in-degree of each vertex, 
then uses a queue to process vertices with zero in-degree, then adds them to the topological order and updates the in-degree
of their neighbors. It repeats until all vertices are processed. The time complexity is O(V + E), where V is the number of vertices
and E is the number of edges. The space complexity is O(V), for the in-degree array and the queue.
"""
import os

class Digraph:
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

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].append(w)
        self.E += 1

    def sort_adj(self):
        for adj in self.adj:
            adj.sort()

    def reverse(self):
        R = Digraph(self.V)
        v = 0
        while v < self.V:
            for w in self.adj[v]:
                R.add_edge(w, v)
            v += 1
        return R

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join(
            "%d: %s" % (v, " ".join(str(w) for w in self.adj[v]))
            for v in range(self.V)
        )
        return s

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_deg = 0
        for v in range(self.V):
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count

    # Question 1: Validate Topological Order
    def validTopologicalOrder(self, order):
        idx_map = {node: idx for idx, node in enumerate(order)}
        for node in range(self.V):
            for neighbor in self.adj[node]:
                if idx_map[node] > idx_map[neighbor]:
                    return False
        return True

    # Question 2: Find Topological Order
    def topological(self):
        in_deg = [0] * self.V
        for n in range(self.V):
            for nbr in self.adj[n]:
                in_deg[nbr] += 1

        zero_deg_q = [n for n in range(self.V) if in_deg[n] == 0]
        topo_ord = []

        while zero_deg_q:
            cur = zero_deg_q.pop(0)
            topo_ord.append(cur)
            for nbr in self.adj[cur]:
                in_deg[nbr] -= 1
                if in_deg[nbr] == 0:
                    zero_deg_q.append(nbr)

        if len(topo_ord) == self.V:
            return topo_ord
        else:
            return None


if __name__ == "__main__":
    filename = "tinyDG.txt"
    current_file_path = os.path.dirname(__file__)
    try:
        g = Digraph(filename=current_file_path + "/" + filename)
    except FileNotFoundError:
        print("File not found: " + filename)

    print(g)

    g = Digraph(9)
    edges = [
        (0, 1), (3, 8), (1, 2), (1, 5), (3, 7),
        (0, 3), (1, 4), (6, 7), (0, 2), (4, 5), (3, 6)
    ]
    for v, w in edges:
        g.add_edge(v, w)
    g.sort_adj()
    print(g)