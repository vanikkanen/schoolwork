import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.layer = -1
        self.connections = {}
        self.forward_connections = set()
        self.backward_connections = set()
        self.full_connections = set()
        self.empty_connections = set()
        self.backtracked_already = False

    def adjust_flow(self, connection, flow):

        capacity = self.connections[connection][1]
        old_flow = self.connections[connection][0]
        new_flow = old_flow + flow
        self.connections[connection] = (new_flow, capacity)

        if self.connections[connection][0] == 0:
            self.empty_connections.add(connection)
        elif connection in self.empty_connections:
            self.empty_connections.discard(connection)
        if self.connections[connection][0] == self.connections[connection][1]:
            self.full_connections.add(connection)
        elif self.connections[connection][0] < self.connections[connection][1]:
            self.full_connections.discard(connection)


def dinitz(nodes, s, t):
    layers = []
    counter = 0
    while bfs(nodes, s, t, layers):
        counter += 1
        print(f"Edges of the level graph for iteration {counter}:")

        for level in range(1, len(layers)):

            print(f" level {level}:", end="")

            print_list = []
            for node in sorted(layers[level - 1]):

                for connection in nodes[node].connections:
                    if nodes[connection].layer == level:
                        if connection in nodes[node].forward_connections and connection not in nodes[node].full_connections:
                            print_list.append((node, connection))
                        elif connection in nodes[node].backward_connections and connection not in nodes[node].empty_connections:
                            print_list.append((connection, node))

            for pair in sorted(print_list):
                print(f" {pair[0]}-{pair[1]}", end="")
            print()
        path = []
        for node in nodes:
            nodes[node].backtracked_already = False
        while dfs(nodes, s, t, float('inf'), path):
            print(*path, sep=" ")
            path = []
            pass
        print()
        layers = []

    max_flow = 0
    for node in nodes[t].connections:
        max_flow += nodes[t].connections[node][0]
    print(f"Maximum flow: {max_flow}")


def dfs(nodes, s, t, flow, path):
    if s == t:
        path.append(s)
        print(f"Found a path with capacity {flow}: ", end="")
        return flow

    for node in sorted(nodes[s].connections):
        # Check if node is currently eligible to be connected to s due to layering,
        # and have they been backtracked from already
        if nodes[node].layer == nodes[s].layer + 1 and not nodes[node].backtracked_already:
            if node in nodes[s].forward_connections and node not in nodes[s].full_connections:
                room_for_flow = nodes[s].connections[node][1] - nodes[s].connections[node][0]
                if s not in path:
                    path.append(s)
                print(f"DFS steps from {s} to {node} with available capacity {room_for_flow}")
                min_flow = min(flow, room_for_flow)
                return_flow = dfs(nodes, node, t, min_flow, path)
                if return_flow and return_flow > 0:
                    nodes[s].adjust_flow(node, return_flow)
                    nodes[node].adjust_flow(s, return_flow)

                    return return_flow
                nodes[node].backtracked_already = True
                print(f"DFS backtracks from {node} to {s}")
                path.pop()

            elif node in nodes[s].backward_connections and node not in nodes[s].empty_connections:
                room_for_flow = nodes[s].connections[node][0]
                path.append(s)
                print(f"DFS steps from {s} to {node} with available reverse capacity {room_for_flow}")
                min_flow = min(flow, room_for_flow)
                if s not in path:
                    path.append(s)
                return_flow = dfs(nodes, node, t, min_flow, path)
                if return_flow and return_flow > 0:
                    nodes[s].adjust_flow(node, -return_flow)
                    nodes[node].adjust_flow(s, return_flow)
                    return return_flow
                nodes[node].backtracked_already = True
                print(f"DFS backtracks from {node} to {s}")
                path.pop()


def bfs(nodes, s, t, layers):
    # reset layers to -1
    for node in nodes:
        nodes[node].layer = -1

    nodes[s].layer = 0
    new_layer = [s]
    while new_layer and t not in new_layer:
        layers.append(new_layer)
        expand_layer = []
        for x in new_layer:
            for y in nodes[x].connections:
                if nodes[y].layer == -1:
                    # Check if connection can be used, depending on if forward or backward connection.
                    if (y in nodes[x].forward_connections and y not in nodes[x].full_connections) \
                            or (y in nodes[x].backward_connections and y not in nodes[x].empty_connections):
                        # set the layer
                        nodes[y].layer = nodes[x].layer + 1
                        expand_layer.append(y)
        new_layer = expand_layer
    layers.append(new_layer)

    return t in layers[-1]


def main(argv):
    input = argv
    filename = "input2"
    if len(input) > 1:
        filename = input[1]

    file = open(filename)
    nodes = {}
    first = True
    for row in file:
        data = row.split()
        if first:
            source = int(data[0])
            sink = int(data[1])
            source_node = Node(source)
            sink_node = Node(sink)
            nodes.update({source: source_node})
            nodes.update({sink: sink_node})
            first = False
        else:
            node_1_name = int(data[0])
            node_2_name = int(data[1])
            max_flow = int(data[2])
            flow = (0, max_flow)
            if node_1_name not in nodes:
                new_node = Node(node_1_name)
                nodes.update({node_1_name: new_node})
            nodes[node_1_name].forward_connections.add(node_2_name)
            nodes[node_1_name].connections.update({node_2_name: flow})
            nodes[node_1_name].adjust_flow(node_2_name, 0)
            if node_2_name not in nodes:
                new_node = Node(node_2_name)
                nodes.update({node_2_name: new_node})
            nodes[node_2_name].backward_connections.add(node_1_name)
            nodes[node_2_name].connections.update({node_1_name: flow})
            nodes[node_2_name].adjust_flow(node_1_name, 0)

    file.close()
    dinitz(nodes, source, sink)


if __name__ == '__main__':
    main(sys.argv)
