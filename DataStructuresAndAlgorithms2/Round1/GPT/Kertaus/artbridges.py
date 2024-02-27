import sys


class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.connected_nodes = []
        self.prev = ""
        self.next_nodes = []
        self.articulation = False
        self.own = 0
        self.earliest = 0

    def add_connected(self, name):
        self.connected_nodes.append(name)


def DFSart(G, node, prev, counter):
    G[node].visited = True
    G[node].own = counter
    G[node].earliest = counter
    counter += 1
    G[node].prev = prev
    for next_node in G[node].connected_nodes:
        if not G[next_node].visited:
            G[node].next_nodes.append(next_node)
            counter = DFSart(G, next_node, node, counter)
            if G[node].own <= G[next_node].earliest:
                G[node].articulation = True
            else:
                G[node].earliest = G[next_node].earliest
        elif G[node].earliest > G[next_node].earliest and next_node != \
                G[node].prev:
            G[node].earliest = G[next_node].earliest
    return counter


def findBridges(G, nodes, bridges):
    for node in nodes:
        for next_node in G[node].connected_nodes:
            if G[node].own < G[next_node].earliest:
                bridges.append((node, next_node))


def main():
    #args = sys.argv
    #filename = args[1]
    filename = "input1_2.txt"
    input = open(filename)
    node_dict = {}
    for line in input:
        params = line.split()
        node1 = params[0]
        node2 = params[1]
        if node1 not in node_dict:
            new_node1 = Node(node1)
            node_dict[node1] = new_node1
        if node2 not in node_dict:
            new_node2 = Node(node2)
            node_dict[node2] = new_node2
        node_dict[node1].connected_nodes.append(node2)
        node_dict[node2].connected_nodes.append(node1)

    start_node = sorted(node_dict.keys())[0]
    counter = 0
    DFSart(node_dict, start_node, start_node, counter)

    if len(node_dict[start_node].next_nodes) < 2:
        node_dict[start_node].articulation = False
    else:
        node_dict[start_node].articulation = True

    art_nodes = []
    for node in node_dict:
        if node_dict[node].articulation:
            art_nodes.append(node)

    print(f"Found {len(art_nodes)} articulation nodes: ", end="")
    print(*art_nodes, sep=" ")

    bridges = []
    findBridges(node_dict, art_nodes, bridges)

    print(f"Found {len(bridges)} bridges:", end="")
    for bridge in bridges:
        print(f" {sorted(bridge)[0]}-{sorted(bridge)[1]}", end="")
    print()


if __name__ == "__main__":
    main()
