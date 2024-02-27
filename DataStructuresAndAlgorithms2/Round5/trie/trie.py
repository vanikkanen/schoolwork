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
            neighbors = {k:v for k,v in node.out.items() if v is not None}
            for x in neighbors:
                next_node = neighbors[x]
                if not next_node.visited:
                    next_node.visited = True
                    expandLayer.append(next_node)
                    expandLevel.append((node.num,next_node.num,next_node.val))
        newLayer = expandLayer
        new_level = expandLevel
    return levels


def bin_search(arr, l, r, x):

     while l <= r:
         lo = l
         hi = r+1
         mid = (lo+hi)//2
         print(f" [{lo}, {hi}, {arr[mid].lower()}]", end="")
         if arr[mid] == x:
             return
         elif arr[mid] < x:
             l = mid + 1
         else:
             r = mid - 1


def search(S, str):
    print()
    print(f"Matching P = {str}")
    node = S
    no_errors = True
    v_node = S
    for i in range(len(str)):
        u = node.num
        print(f"  searching {str[i]}:", end="")
        neighbors = {k: v for k, v in node.out.items() if v is not None}
        bin_search(sorted(list(neighbors.keys())), 0, len(neighbors)-1, str[i])
        print()
        if node.out[str[i]] != None:
            v = node.out[str[i]].num
            v_node = node.out[str[i]]
            print(f"  move from {u} to {v} with character P[{i}] = {str[i]}")
            node = node.out[str[i]]
        else:
            print(f"  matching failed at {u} with character P[{i}] = "
                  f"{str[i]}",end="")
            no_errors = False
    if no_errors:
        print(f"  P matches with (prefixes of):", end="")
        for i in v_node.strings:
            print(f" S{i}", end="")


args = sys.argv
if len(args) > 1:
    strings_file = args[1]
    patterns_file = args[2]
else:
    strings_file = "strings1.txt"
    patterns_file = "patterns1.txt"

strings = open(strings_file).read().split()
i = 0
S = Node("start", i)

x = 1
for str in strings:
    prev_node = S
    for c in str:

        if prev_node.out[c] == None:
            i += 1
            new_node = Node(c, i)
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
    print(f" level {i}:",end="")
    for ele in sorted(level, key=lambda x: (x[0], x[2])):
        print(f" ({ele[0]}-{ele[1]}, {ele[2]})", end="")
    print()
    i += 1


patterns = open(patterns_file).read().split()
for str in patterns:
    search(S, str)
    print()

