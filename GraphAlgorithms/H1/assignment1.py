### Read in a graph, a set of vertices, and a pair of vertices.

import graph

import heapq
import sys


# Implement your algorithm here:


def algorithm(g, B, v, w):
    queue = [(0, (v, [v], set() if v not in B else {v}))]  # priority, (node, path, set)
    visited_nodes = set()

    while queue:
        current_priority, (
        current_node, current_path, current_set) = heapq.heappop(queue)

        if current_node == w:
            return len(current_set)

        for next_node in g.adj[current_node]:
            if next_node not in visited_nodes:
                next_node_path = current_path + [next_node]
                next_node_set = current_set.copy()
                if next_node in B:
                    next_node_set.add(next_node)
                priority = (len(next_node_path), -len(
                    next_node_set))  # prioritize fewer nodes from set B if
                # lengths are equal
                heapq.heappush(queue, (priority, (next_node, next_node_path, next_node_set)))
                visited_nodes.add(next_node)

        visited_nodes.add(current_node)

    # If the loop completes without finding the destination, there is no path
    return -1



### Read in a set of vertices from a file. These are just numbers separated
# by whitespace.
def readset(filename):
    f = open(filename, 'r')
    s = set()
    for line in f:
        for v in line.split():
            s.add(int(v))
    return s


## Read the pair, again, just two integers separated by whitespace.
def readpair(filename):
    f = open(filename, 'r')
    for line in f:
        (v, w) = line.split()
        return int(v), int(w)


### If ran from the command line:
if __name__ == "__main__":
    # Graph is the first command line argument:
    g = graph.Graph()

    g.readgraph(sys.argv[1])
    # Vertices are the second command line argument:
    B = readset(sys.argv[2])
    # Pair is the third command line argument:
    (v,w) = readpair(sys.argv[3])
    """""
    
    # Used for testing while coding and debugging
    g.readgraph("testgraph_10")
    # Vertices are the second command line argument:
    B = readset("testset_10")
    # Pair is the third command line argument:
    (v, w) = readpair("testpair_10")
    """""
    ### Call your algorithm:

    n = algorithm(g, B, v, w)

    # Print the result:
    print(n)
