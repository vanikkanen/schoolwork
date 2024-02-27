import sys


class Node:

    def __init__(self, name):
        self.name = name
        self.next = {}
        self.prev = {}
        self.connected = set()
        self.visited = False
        self.full_connections = set()
        self.empty_connections = set()
        self.valid = True
        self.layer_nro = 0

    def add_next(self, name, weight):
        self.next[name] = weight
        self.connected.add(name)

    def add_prev(self, name, weight):
        self.prev[name] = weight
        self.connected.add(name)


def BFS(G, s, t, layers):
    for node in G:
        G[node].visited = False
    new_layer = []
    new_layer.append(s)
    G[s].visited = True
    while new_layer and not any(t in sublist for sublist in layers):
        layers.append(new_layer)
        expand_layer = []
        for node in new_layer:
            for next_node in G[node].next:
                if not G[next_node].visited and \
                        G[node].next[next_node][0] < G[node].next[next_node][1]:
                    G[next_node].visited = True
                    expand_layer.append(next_node)
            for prev_node in G[node].prev:
                if not G[prev_node].visited and prev_node not in G[
                    node].empty_connections:
                    G[prev_node].visited = True
                    expand_layer.append(prev_node)
        new_layer = expand_layer

    return any(t in sublist for sublist in layers)


def DFS(L, s, t):
    path = []
    path.append(s)
    while path:
        current_node = path[-1]
        L[current_node].visited = True
        valid_next_nodes = []
        for node in L[current_node].connected:
            if node in L[current_node].next and node not in L[
                current_node].full_connections and not L[node].visited and \
                    L[node].valid and L[node].layer_nro > L[current_node].layer_nro:
                    valid_next_nodes.append(node)
            elif node in L[current_node].prev and node not in L[
                node].empty_connections and L[node].valid and not L[node].visited  and L[
                node].layer_nro > L[current_node].layer_nro:
                valid_next_nodes.append(node)

        if current_node == t:
            bottleneck = float('inf')
            for i in range(1, len(path)):
                node1 = path[i-1]
                node2 = path[i]

                if node2 in L[node1].next:
                    currentflow = L[node1].next[node2][0]
                    capacity = L[node1].next[node2][1]
                    if capacity - currentflow < bottleneck:
                        bottleneck = capacity - currentflow
                elif node2 in L[node1].prev:
                    currentflow = L[node1].prev[node2][0]
                    if currentflow < bottleneck:
                        bottleneck = currentflow

            for i in range(1, len(path)):
                node1 = path[i-1]
                node2 = path[i]
                if node2 in L[node1].next:
                    flow = L[node1].next[node2][0] + bottleneck
                    capacity = L[node1].next[node2][1]
                    L[node1].next[node2] = (flow, capacity)
                    L[node2].prev[node1] = (flow, capacity)
                    L[node2].empty_connections.discard(node1)
                    L[node1].empty_connections.discard(node2)
                    if flow == capacity:
                        L[node2].full_connections.add(node1)
                        L[node1].full_connections.add(node2)
                elif node2 in L[node1].prev:
                    flow = L[node1].prev[node2][0] - bottleneck
                    capacity = L[node1].prev[node2][1]
                    L[node2].next[node1] = (flow, capacity)
                    L[node1].prev[node2] = (flow, capacity)
                    L[node2].full_connections.discard(node1)
                    L[node1].full_connections.discard(node2)
                    if flow == 0:
                        L[node2].empty_connections.add(node1)
                        L[node1].empty_connections.add(node2)


            print(f"Found a path with capacity {bottleneck}: ", end="")
            print(*path, sep=" ")
            for node in L:
                L[node].visited = False
            path = [s]

        elif valid_next_nodes:
            path.append(sorted(valid_next_nodes)[0])
            if sorted(valid_next_nodes)[0] in L[current_node].next:
                print(f'DFS steps from {current_node} to {path[-1]} with '
                      f'available capacity '
                      f'{L[current_node].next[path[-1]][1]-L[current_node].next[path[-1]][0]}')
            else:
                print(f'DFS steps from {current_node} to {path[-1]} with '
                      f'available reverse capacity '
                      f'{L[current_node].prev[path[-1]][0]}')
        else:
            if len(path) > 1:
                print(f"DFS backtracks from {current_node} to {path[-2]}")
            path.remove(current_node)
            L[current_node].valid = False


def dinitz(G, s, t):
    layers = []
    counter = 1
    while BFS(G, s, t, layers):
        L = {}
        print(f"Edges of the level graph for iteration {counter}:")
        for level in range(1, len(layers)):
            print(f" level {level}:", end="")
            layer_print = []
            for node in sorted(layers[level-1]):
                for connection in sorted(G[node].connected):
                    if connection in layers[level]:
                        if node not in L:
                            L.update({node: Node(node)})
                            L[node].layer_nro = level
                        if connection not in L:
                            L.update({connection: Node(connection)})
                            L[connection].layer_nro = level+1
                        if connection in G[node].next and connection not in \
                                G[node].full_connections:
                            weight = G[node].next[connection]
                            L[node].add_next(connection, weight)
                            L[connection].add_prev(node, weight)
                            layer_print.append((node,connection))
                        if connection in G[node].prev and connection not in \
                                G[node].empty_connections:
                            weight = G[node].prev[connection]
                            L[node].add_prev(connection, weight)
                            L[connection].add_next(node, weight)
                            layer_print.append((connection, node))
                        L[node].empty_connections = G[node].empty_connections
                        L[connection].empty_connections = G[connection].empty_connections
                        L[node].full_connections = G[node].full_connections
                        L[connection].full_connections = G[connection].full_connections
            for pair in sorted(layer_print):
                print(f" {pair[0]}-{pair[1]}", end="")
            print()

        DFS(L, s, t)

        for node in L:
            for connected_node in L[node].connected:
                G[node].full_connections = L[node].full_connections
                G[node].empty_connections = L[node].empty_connections
                if connected_node in L[node].next:
                    G[node].next[connected_node] = L[node].next[connected_node]
                elif connected_node in L[node].prev:
                    G[node].prev[connected_node] = L[node].prev[connected_node]
        counter += 1
        layers = []
        print()


def main():
    #args = sys.argv
    #filename = args[1]

    filename = "input5.txt"

    node_dict = {}
    input = open(filename)
    source_node = ""
    sink_node = ""

    for line in input:
        params = line.split()
        node1 = int(params[0])
        node2 = int(params[1])
        if len(params) > 2:
            weigth = int(params[2])
            if node1 not in node_dict:
                node_dict.update({node1: Node(node1)})
            if node2 not in node_dict:
                node_dict.update({node2: Node(node2)})
            node_dict[node1].add_next(node2, (0, weigth))
            node_dict[node1].empty_connections.add(node2)
            node_dict[node2].add_prev(node1, (0, weigth))
            node_dict[node2].empty_connections.add(node1)
        else:
            source_node = node1
            sink_node = node2
            node_dict.update({source_node: Node(source_node)})
            node_dict.update({sink_node: Node(sink_node)})

    dinitz(node_dict, source_node, sink_node)

    flow = 0
    for connection in node_dict[sink_node].prev:
        flow += node_dict[sink_node].prev[connection][0]
    print(f"Maximum flow: {flow}")


if __name__ == "__main__":
    main()
