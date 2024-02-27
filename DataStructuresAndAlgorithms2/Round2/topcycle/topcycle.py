import sys


class Node:

    def __init__(self, name):
        self.name = name
        self.next = set()
        self.prev = set()
        self.visited = False

    def add_next_node(self, node):
        self.next.add(node)

    def add_prev_node(self, node):
        self.prev.add(node)


def topoc_sort(G):

    ord = []
    src_nodes = []
    remaining = []

    # Find source nodes
    for n in G:
        node = G[n]
        remaining.append(n)
        if not node.prev:
            src_nodes.append(n)

    while src_nodes:
        u = sorted(src_nodes)[0]
        ord.append(u)
        for next in G[u].next:
            G[next].prev.remove(u)
            if not G[next].prev:
                src_nodes.append(next)
        src_nodes.remove(u)
        remaining.remove(u)

        if not src_nodes and remaining:
            print_topoc_loop(G, remaining)
            return

    print_topoc_order(ord)


def print_topoc_order(list):
    print("Found a topological order: ", end="")
    print(*list, sep=" ")


def print_topoc_loop(G, remaining):

    u = G[sorted(remaining)[0]]
    u.visited = True
    not_found = True
    current_node = u

    while not_found:
        current_node = G[sorted(current_node.prev)[0]]
        if current_node.visited:
            not_found = False
            continue
        current_node.visited = True

    loop_nodes = []
    start_node = current_node.name
    loop_nodes.append(start_node)
    looping = True
    while looping:
        current_node = G[sorted(current_node.prev)[0]]
        loop_nodes.append(current_node.name)
        if current_node.name == start_node:
            looping = False
            continue
    loop_nodes.reverse()

    print("The graph is not acyclic, found a cycle: ", end="")
    print(*loop_nodes, sep=" ")


def main(argv):

    input = open(sys.argv[1])
    #input = open("input2.txt")
    node_dict = {}

    for line in input:
        params = line.split()
        if int(params[0]) not in node_dict:
            new_node = Node(int(params[0]))
            node_dict[int(params[0])] = new_node
            new_node.add_next_node(int(params[1]))
        else:
            node_dict[int(params[0])].add_next_node(int(params[1]))

        if int(params[1]) not in node_dict:
            new_node = Node(int(params[1]))
            new_node.add_prev_node(int(params[0]))
            node_dict[int(params[1])] = new_node
        else:
            node_dict[int(params[1])].add_prev_node(int(params[0]))

    topoc_sort(node_dict)




if __name__ == "__main__":
    main(sys.argv)
