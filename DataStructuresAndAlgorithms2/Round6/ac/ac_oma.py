import sys
import string


class Node:

    def __init__(self, val, i):
        self.val = val
        self.num = i
        chars = list(string.ascii_letters)
        self.out = dict.fromkeys(chars, None)
        self.visited = False
        self.strings = []
        self.fac = None
        self.parent = None

    def __repr__(self) -> str:
        return f"{self.val}, {self.num}"


def BFS(s):
    layers = []
    levels = []
    newLayer = []
    new_level = []
    newLayer.append(s)
    s.visited = True
    while newLayer:
        layers.append(newLayer)
        levels.append(new_level)
        expandLayer = []
        expandLevel = []
        for node in newLayer:
            neighbors = {k: v for k, v in node.out.items() if v is not None}
            for x in neighbors:
                next_node = neighbors[x]
                if not next_node.visited:
                    next_node.visited = True
                    expandLayer.append(next_node)
                    expandLevel.append((node.num, next_node.num,
                                        next_node.val))
        newLayer = expandLayer
        new_level = expandLevel
    return levels


def precomputeFac(r):
    r.fac = None
    neighbors = {k: v for k, v in r.out.items() if v is not None}
    for u in neighbors:
        neighbors[u].fac = r
    next_level = list(neighbors.values())

    while next_level:
        expandLevel = []
        for u in next_level:
            out_nodes = {k: v for k, v in u.out.items() if v is
                         not None}
            for node in out_nodes.values():
                expandLevel.append(node)
            w = u.parent
            v = w.fac
            while v is not None and v.out[u.val] == None:
                v = v.fac
            if v is not None:
                u.fac = v.out[u.val]
            else:
                u.fac = r
        next_level = expandLevel


args = sys.argv
if len(args) > 1:
    input_file = args[1]
else:
    input_file = "input1.txt"

strings = open(input_file).read().split("\n")
i = 0
S = Node("start", i)

text_string = strings[0]
pattern_strings = strings[1:]

x = 1
for str in pattern_strings:
    prev_node = S
    for c in str:

        if prev_node.out[c] == None:
            i += 1
            new_node = Node(c, i)
            new_node.parent = prev_node
            prev_node.out[c] = new_node
            new_node.strings.append(x)
        else:
            prev_node.out[c].strings.append(x)
        prev_node = prev_node.out[c]

    x += 1

print("Trie levels:")
levels = BFS(S)
i = 1
for level in levels[1:]:
    print(f" level {i}:", end="")
    for ele in sorted(level, key=lambda x: (x[0], x[2])):
        print(f" ({ele[0]}-{ele[1]}, {ele[2]})", end="")
    print()
    i += 1

i = 0
print("Suffix function:")
precomputeFac(S)

