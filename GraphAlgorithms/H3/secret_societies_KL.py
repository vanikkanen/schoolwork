"""""
MATH.APP.270-2023-2024-1 Graafialgoritmit / Algorithms for graphs

3. programming task
3. Salaseurat / Secret societies

Input: A graph, given as directed, but interpreted to be nondirected
Interpretation: The vertices are players of a clandestine game. Edges denote observed
interactions between players. Players have formed four secret societies. Players are more
likely to interact with players that are members of the same society, and less likely to
interact with outsiders (though these interactions may occur). Every player belongs to
one of the four secret societies. The societies try to form in such a way that they are
roughly the same size, though the sizes may in some cases differ.
Task: Based on the edges, formulate an estimate as to what are the four secret societies.
Return a list of four lists in such a way that every vertex belongs to exactly one list.
Order the lists internally from the smallest vertex number to the largest.

"""""

from graph import Graph
import sys


# Making an assumption that a node cannot have a secret society with itself but it needs to have a connection to
# at least one other node in the graph
def nondirect_graph(G):
    graph_dict = {}

    index = 0
    for adj_nodes in G.adj:
        for adj_node in adj_nodes:
            if index not in G.adj[adj_node]:
                G.addEdge(adj_node, index)
        graph_dict[index] = adj_nodes
        index += 1

    # Return a dict without any nodes without connections
    return {k: v for k, v in graph_dict.items() if v}


def FloydWarshall(graph):
    dist = [[float("inf") for _ in range(len(graph))] for _ in range(len(graph))]

    for node in graph:
        dist[node][node] = 0

    for node in graph:
        for neighbor in graph[node]:
            dist[node][neighbor] = 1
            dist[neighbor][node] = 1

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Kernighan-Lin algorithm modified k-partitioning.
# We are using the distances of the nodes from one another as the metric for determining if they are in the same secret
# society as we don not have any edge weights.
def detect_secret_societies(graph, k=4):
    # Initialize the partition to four random sets of nodes
    partitions = [list(graph)[i::k] for i in range(k)]
    # Get the shortest distances between nodes
    dist = FloydWarshall(graph)

    improvement = True

    while improvement:
        improvement = False
        best_improvement = 0
        best_move = None
        # Calculate the initial distances for each node in the partitions
        distances_in_partition = calculate_initial_distances(partitions, dist)

        # Iterate over all the pairs of partitions
        for i in range(k):
            for j in range(i + 1, k):
                # Iterate over the nodes in the partitions
                for nodeA in partitions[i]:
                    for nodeB in partitions[j]:
                        # Calculate the distance improvement for switching the partitions of nodeA and nodeB
                        distance_improvement = distances_in_partition[nodeA] + distances_in_partition[nodeB] \
                               - calculate_distance_when_moved(nodeA, nodeB, partitions[i][:], partitions[j][:], dist)
                        # If there was any improvement in the partitions and the improvement is the best we have
                        # found this iteration mark it down
                        if distance_improvement > best_improvement:
                            best_improvement = distance_improvement
                            best_move = (nodeA, nodeB, i, j)

        # If there was any improvement this iteration make the best improvement
        if best_improvement > 0:
            nodeA, nodeB, i, j = best_move
            partitions[i][partitions[i].index(nodeA)], partitions[j][partitions[j].index(nodeB)] = nodeB, nodeA
            improvement = True

    # Return the sorted best partitions
    return [sorted(partition) for partition in partitions]


# We calculate the initial values for all the nodes in the graph which we will use to compare improvement
def calculate_initial_distances(partitions, dist):
    gains = {node: 0 for node in range(len(dist))}
    for partition in partitions:
        for node in partition:
            # Calculate the sum of distances from the node to the other nodes in its partition.
            for other_node in partition:
                if other_node != node:
                    gains[node] += dist[node][other_node]
    return gains


# Calculate what the distances would be if the nodes switched partitions
def calculate_distance_when_moved(nodeA, nodeB, partitionA, partitionB, dist):
    partitionA[partitionA.index(nodeA)], partitionB[partitionB.index(nodeB)] = nodeB, nodeA

    distA, distB = 0, 0
    # Calculate the sum of distances from the nodes to the other nodes in their partitions.
    for node in partitionA:
        if node != nodeB:
            distA += dist[nodeB][node]
    for node in partitionB:
        if node != nodeA:
            distB += dist[nodeA][node]

    return distA + distB


if __name__ == '__main__':
    G = Graph()
    inputgraph = sys.argv[1]
    # inputgraph = "testcase"
    G.readgraph(inputgraph)
    graph_dict = nondirect_graph(G)
    secret_societies = detect_secret_societies(graph_dict)
    print(secret_societies)




