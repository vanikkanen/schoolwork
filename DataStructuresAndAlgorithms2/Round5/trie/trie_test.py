import sys


class Node:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.connected = {}
        self.parent_id = None
        self.level = -1
        self.prefix = []

    def __repr__(self) -> str:
        return f"{self.name} {self.id}"


def print_trie_levels(s):
    print("Trie levels:")
    layer = [s]
    level = 1
    levels = {}
    while layer:
        next_layer = []
        for node in sorted(layer, key=lambda x: x.id):
            for next_node in sorted(node.connected):
                next_node = node.connected[next_node]
                next_node.parent_id = node.id
                next_node.level = level
                next_layer.append(next_node)
        if next_layer:
            print(f" level {level}:", end="")
            levels[level] = next_layer
            for node in next_layer:
                print(f" ({node.parent_id}-{node.id}, {node.name})", end="")
            print()
        level += 1
        layer = next_layer
    return levels


def search(s, P):
    print(f"Matching P = {P}")
    current_node = s
    found = False
    for i in range(0, len(P)):
        c = P[i]
        outgoing_nodes = sorted(list(current_node.connected.values()),
                                key=lambda x: x.name)
        l = 0
        r = len(outgoing_nodes)
        print(f"  searching {c}:", end="")
        found = False
        while l < r:
            mid = (l+r)//2
            mid_node = outgoing_nodes[mid]
            mid_c = mid_node.name.lower()
            print(f" [{l}, {r}, {mid_c}]", end="")

            if mid_c == c.lower():
                print()
                print(f"  move from {current_node.id} to {mid_node.id} with "
                      f"character P[{i}] = {c}", end="")
                found = True
                current_node = mid_node
                break

            elif mid_c < c.lower():
                l = mid + 1

            else:
                r = mid
        print()

        if not found:
            print(f"  matching failed at {current_node.id} with character P["
                  f"{i}] = {c}")
            break
    if found:
        print(f"  P matches with (prefixes of):", end="")
        for i in current_node.prefix:
            print(f" S{i}", end="")
        print()


args = sys.argv
if len(args) > 1:
    strings_file = args[1]
    patterns_file = args[2]
else:
    strings_file = "strings1.txt"
    patterns_file = "patterns1.txt"

strings = open(strings_file).read().splitlines()
patterns = open(patterns_file).read().splitlines()

start_node = Node("start", 0)
i = 1
x = 1
for string in strings:
    prev_node = start_node
    for c in string:
        if c not in prev_node.connected:
            new_node = Node(c, i)
            i += 1
            prev_node.connected[c] = new_node
        prev_node = prev_node.connected[c]
        prev_node.prefix.append(x)
    x += 1
levels = print_trie_levels(start_node)


for pattern in patterns:
    print()
    search(start_node, pattern)
