# A template for Ford Fulkerson algorithm and min cut

from graph import Graph
from copy import deepcopy as copy
from collections import deque
import sys


# from icecream import ic


## This code assumes flow is dictionary with keys (u,v) and values flow(u,v)
## Define the sum of two flows
def SumFlow(f1, f2):
    f = {}
    for (u, v) in set(f1.keys()) | set(f2.keys()):
        if not (u, v) in f1:
            f[(u, v)] = f2[(u, v)]
        elif not (u, v) in f2:
            f[(u, v)] = f1[(u, v)]
        else:
            f[(u, v)] = f1[(u, v)] + f2[(u, v)]
    return f


class FlowNetwork:
    def __init__(self, G) -> None:
        self.G = G
        self.s = None
        self.FindSource()
        self.t = None
        self.FindSink()

    # Find the source, it is the first vertex with a non-empty adjacency list:
    def FindSource(self):
        for u in range(self.G.n):
            if len(self.G.adj[u]) > 0:
                self.s = u
                return
                # Find the sink. It is the last vertex.

    def FindSink(self):
        self.t = self.G.n - 1

    # Define the value of a flow
    def FlowValue(self, f):
        return sum([f[(self.s, u)] for u in G.adj[self.s] if (self.s, u) in f])

    # Create a residual graph
    def MakeResidual(self, f):
        # Copy the graph:
        G = copy(self.G)
        for (u, v) in f:
            c = 0
            # Copy the weight
            if (u, v) in G.w:
                c = G.w[(u, v)]
            # calculate residual capasity
            cf = c - f[(u, v)]
            # It is an error if the residual capacity is negative
            if cf < 0:
                raise Exception("capacity violation in f")
            # Add the edge if the residual capacity is positive
            if not v in G.adj[u]:
                G.addEdge(u, v)
            G.w[(u, v)] = cf
        return G

    # DFS for finding augmenting paths
    def DFS(self, Gr, u, visited, path):
        visited[u] = True
        path.append(u)

        if u == self.t:
            return True

        for v in Gr.adj[u]:
            if not visited[v] and Gr.w[(u, v)] > 0:
                if self.DFS(Gr, v, visited, path):
                    return True

        path.pop()
        return False

    # BFS for finding all the edges that we can get to from start node to
    # determine the S set for MinCut
    def BFS(self, Gr):
        visited = set()
        queue = deque([self.s])

        while queue:
            u = queue.popleft()
            if u not in visited:
                visited.add(u)
                for v in Gr.adj[u]:
                    # Add to the queue if the next vertex is not visited and
                    # the edge weight is more than 0 so is not on the other
                    # side of the MinCut
                    if v not in visited and Gr.w[(u, v)] > 0:
                        queue.append(v)

        return visited

    # Augmenting path algorithm is a DFS
    def FindAugPath(self, Gr, s=None, t=None):
        if s is None:
            s = self.s

        # Now find the path.
        visited = [False] * Gr.n
        path = []

        if self.DFS(Gr, s, visited, path):
            return path
        else:
            return []

        # Make an augmenting flow from a path

    def MakeAugFlow(self, path, Gr=None):
        if Gr is None:
            Gr = self.G
        f = {}
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            if (u, v) not in Gr.w or Gr.w[(u, v)] == 0:
                raise Exception("Edge not in Gr or saturated")
            f[(u, v)] = 0
        cf = min([Gr.w[(u, v)] for (u, v) in f])
        for (u, v) in f:
            f[(u, v)] = cf
        return f

    def FordFulkerson(self):
        f = {}
        G = self.G
        Gr = self.MakeResidual(f)
        ap = self.FindAugPath(G)
        while ap != []:
            fp = self.MakeAugFlow(ap, Gr)
            f = SumFlow(f, fp)
            Gr = self.MakeResidual(f)
            ap = self.FindAugPath(Gr)
        return f

    def MinCutEdges(self):
        f = self.FordFulkerson()
        Gr = self.MakeResidual(f)
        # Find the cut (S,T) by finding the set S.
        S = self.BFS(Gr)

        # Return the edges that cross the cut
        # Find the edges that cross the cut (S,T), i.e., they start from S
        # and end in T.
        Edges = [(u, v) for u in S for v in G.adj[u] if v not in S]

        # Return these edges.
        return Edges


if __name__ == "__main__":
    G = Graph()
    inputgraph = sys.argv[1]
    # inputgraph = "testcase"
    G.readgraph(inputgraph)
    F = FlowNetwork(G)
    edges = F.MinCutEdges()
    # Print can be commented out but used for presenting the results
    print(edges)
