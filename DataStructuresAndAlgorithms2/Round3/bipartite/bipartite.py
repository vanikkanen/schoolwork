import sys

class Node:

    def __init__(self, name, left):
        self.name = name
        self.left = left
        self.connected = set()
        self.match = None


def bipartite_match(G):
    left_nodes = [node for node in G if G[node].left]

    matches = {}
    for node in left_nodes:
        if G[node].match is None:
            visited = set()
            if dfs(G, G[node], visited):
                matches[node] = G[node].match

    while True:
        visited = set()
        updated = False
        for node in left_nodes:
            if node not in matches:
                if dfs(G, G[node], visited):
                    updated = True
        if not updated:
            break

    result = {}
    for node in left_nodes:
        if G[node].match is not None:
            result[G[node].name] = G[node].match.name
    return result


def dfs(G, node, visited):
    visited.add(node)
    for neighbor in node.connected:
        if neighbor not in visited:
            visited.add(neighbor)
            if neighbor.match is None or dfs(G, neighbor.match, visited):
                node.match = neighbor
                neighbor.match = node
                return True
    return False


def main():

    #args = sys.argv
    #filename = args[1]
    filename = "input2.txt"

    node_dict = {}
    with open(filename) as input:
        for line in input:
            params = line.split()
            node1 = params[0]
            node2 = params[1]
            if node1 not in node_dict:
                node_dict[node1] = Node(node1, True)
            if node2 not in node_dict:
                node_dict[node2] = Node(node2, False)
            node_dict[node1].connected.add(node_dict[node2])

    results = bipartite_match(node_dict)
    print(f"A maximum bipartite matching with {len(results)} pairs:")
    for pair in results:
        print(f"{pair} {results[pair]}")

    input.close()


if __name__ == "__main__":
    main()
