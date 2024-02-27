import sys


class Node:

    def __init__(self, label):
        self.label = label
        self.connected_nodes = []
        self.earliest = 0
        self.own = 0
        self.visited = False
        self.prev = ""
        self.next = []
        self.articulation = False


class Counter:

    def __init__(self, ival):
        self.val = ival


def DFSart(node, prev, i):

    node.visited = True
    node.own = i.val
    node.earliest = i.val
    i.val += 1
    node.prev = prev
    for next_node in node.connected_nodes:
        if not next_node.visited and next_node != node.prev:
            node.next.append(next_node.label)
            DFSart(next_node, node, i)
            if node.own <= next_node.earliest:
                node.articulation = True
            else:
                node.earliest = next_node.earliest
        else:
            if node.earliest > next_node.earliest and next_node != \
                    node.prev:
                node.earliest = next_node.earliest


def findBridges(nodes, node_dict, bridges):
    for node in nodes:
        node = node_dict[node]
        node.visited = True
        for next_node in node.connected_nodes:
            if next_node.earliest > node.own and next_node.earliest != \
                    node.own:
                bridges.append((next_node.label, node.label))


def main(argv):

    #input = open(sys.argv[1])
    input = open("input2_2.txt")
    node_dict = {}
    for line in input:
        param = line.split()
        node1 = param[0]
        node2 = param[1]
        if node1 not in node_dict:
            new_node1 = Node(node1)
            node_dict[node1] = new_node1
        if node2 not in node_dict:
            new_node2 = Node(node2)
            node_dict[node2] = new_node2
        node_dict[node1].connected_nodes.append(node_dict[node2])
        node_dict[node2].connected_nodes.append(node_dict[node1])

    start_node = node_dict[list(node_dict)[0]]
    i = Counter(0)
    DFSart(start_node, start_node, i)

    if len(start_node.next) < 2:
        start_node.articulation = False
    else:
        start_node.articulation = True

    art_nodes = []
    for node in node_dict:
        if node_dict[node].articulation:
            art_nodes.append(node)
        node_dict[node].visited = False
    print(f"Found {len(art_nodes)} articulation nodes:", end=" ")
    print(*sorted(art_nodes), sep=" ")

    bridges = []
    findBridges(art_nodes, node_dict, bridges)

    print(f"Found {len(bridges)} bridges:", end="")
    for bridge in bridges:
        print(f" {sorted(bridge)[0]}-{sorted(bridge)[1]}", end="")
    print()


if __name__ == "__main__":
    main(sys.argv)
