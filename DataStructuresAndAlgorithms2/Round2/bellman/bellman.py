import sys


class Node:

    def __init__(self, name):
        self.name = name
        self.next = {}
        self.dist = float('inf')
        self.prev = ""
        self.visited = False

    def add_next_node(self, node, cost):
        self.next[node] = cost


def bellman(G, s):

    G[s].dist = 0
    improved = []
    improved.append(s)
    for i in range(1, len(G)+1):
        next_improved = {}
        for u in sorted(improved):
            node = G[u]
            for next in node.next:
                next_node = G[next]
                if node.next[next] + node.dist < next_node.dist:
                    next_node.dist = node.next[next] + node.dist
                    next_improved[next] = ""
                    next_node.prev = node.name
        improved = next_improved.keys()

        if improved:
            print("Improvements in iteration", i, end=": ")
            for node in sorted(improved):
                print(f"d({node}) = {G[node].dist}",
                      end="" if node == sorted(improved)[len(improved)-1]
                            else ", ")
            print()
            if i == len(G):
                u = sorted(improved)[0]
                negative_loop(G, u)
        else:
            print("No improvements in iteration", i)
            if i == len(G):
                print(f"Distances from {s}:", end=" ")
                for node in sorted(G):
                    print(f"d({node}) = {G[node].dist}",
                          end="" if node == sorted(G.keys())[-1]
                          else ", ")
            else:
                print(f"Distances from {s}:", end=" ")
                for node in sorted(G):
                    print(f"d({node}) = {G[node].dist if G[node].dist != float('inf') else 'INF'}",
                          end="" if node == sorted(G.keys())[-1]
                          else ", ")
                break


def negative_loop(G, s):

    not_found = True
    loop_nodes = []
    G[s].visited = True
    current_node = G[G[s].prev]

    while not_found:
        if current_node.visited:
            not_found = False
            continue
        current_node.visited = True
        current_node = G[current_node.prev]

    start_node = current_node.name
    loop_not_found = True
    while loop_not_found:
        loop_nodes.append(current_node.name)
        current_node = G[current_node.prev]
        if current_node.name == start_node:
            loop_nodes.append(current_node.name)
            loop_not_found = False

    loop_nodes.reverse()
    str = ""
    for i in loop_nodes:
        str = str + f" {i}"

    cost = 0
    for node in range(1, len(loop_nodes)):
        cost += G[loop_nodes[node-1]].next[loop_nodes[node]]

    print(f"A negative cycle with cost {cost} detected:{str}")


def main(argv):

    #input = open(sys.argv[1])
    input = open("input6.txt")
    node_dict = {}
    for line in input:
        params = line.split()
        if int(params[0]) not in node_dict:
            new_node = Node(int(params[0]))
            node_dict[int(params[0])] = new_node
            new_node.add_next_node(int(params[1]), int(params[2]))
        else:
            node_dict[int(params[0])].add_next_node(int(params[1]), int(params[
                                                                         2]))

        if int(params[1]) not in node_dict:
            new_node = Node(int(params[1]))
            node_dict[int(params[1])] = new_node

    #start_node = int(sys.argv[2])
    start_node = 12
    bellman(node_dict, start_node)



if __name__ == "__main__":
    main(sys.argv)
