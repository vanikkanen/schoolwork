from collections import defaultdict
import sys


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def APUtil(self, u, visited, ap, parent, low, disc):

        children = 0
        visited[u] = True
        self.Time += 1

        disc[u] = self.Time
        low[u] = self.Time

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def AP(self):
        # Mark all the vertices as not visited
        visited = {node: False for node in self.graph}
        disc = {node: float("Inf") for node in self.graph}
        low = {node: float("Inf") for node in self.graph}
        parent = {node: -1 for node in self.graph}
        ap = {node: False for node in self.graph}

        for node in self.graph:
            if visited[node] == False:
                self.APUtil(node, visited, ap, parent, low, disc)

        art_nodes = []
        for node, value in ap.items():
            if value == True:
                art_nodes.append(node)
        print(f"Found {len(art_nodes)} articulation nodes:", end="")
        for node in sorted(art_nodes):
            print(" " + node, end="")

    def bridgeUtil(self, u, visited, parent, low, disc, bridges):
        visited[u] = True
        self.Time += 1

        disc[u] = self.Time
        low[u] = self.Time

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc, bridges)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = {node: False for node in self.graph}
        disc = {node: float("Inf") for node in self.graph}
        low = {node: float("Inf") for node in self.graph}
        parent = {node: -1 for node in self.graph}
        bridges = []
        for node in self.graph:
            if visited[node] == False:
                self.bridgeUtil(node, visited, parent, low, disc, bridges)
        print(f"Found {len(bridges)} bridges:", end="")
        for bridge in bridges:
            print(f" {sorted(bridge)[0]}-{sorted(bridge)[1]}", end="")
        print()


def main():

    input = open(sys.argv[1])
    #input = open("../input2_3.txt")
    g = Graph()
    for line in input:
        param = line.split()
        g.add_edge(param[0], param[1])
    g.AP()
    print()
    g.bridge()



if __name__ == "__main__":
    main()