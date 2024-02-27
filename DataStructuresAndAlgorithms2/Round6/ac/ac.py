import sys


class Node:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.level = -1
        self.next = {}
        self.previous = self
        self.prefix_to = set()
        self.fac = ""

    def __repr__(self) -> str:
        return f"{self.id} {self.name}"


def precomputeFac(r, levels):
    r.fac = None
    for child in r.next:
        r.next[child].fac = r
    for level in range(1, len(levels)):
        for u in levels[level]:
            w = u.previous
            v = w.fac
            while v is not None and u.name not in v.next:
                v = v.fac
            if v is not None:
                u.fac = v.next[u.name]
            else:
                u.fac = r


def bin_search(level, c):
    low = 0
    high = len(level)
    mid = 0
    c = c.upper()
    level = sorted(level, key=lambda x: (x.previous.id, x.name))
    while low <= high:

        mid = (high + low) // 2
        if mid < len(level) and mid != high:
            print(f" [{low}, {high}, {level[mid].name.lower()}]", end="")

            if level[mid].name.upper() < c:
                low = mid + 1

            elif level[mid].name.upper() > c:
                high = mid

            else:
                print()
                print(f"  move from {level[mid].previous.id} to {level[mid].id} with character P[{level[mid].previous.level}] = {level[mid].name}")
                return level[mid]
        else:
            print()
            print(f"  matching failed at {level[0].previous.id} with character P[{level[0].previous.level}] = {c.lower()}")
            return -1
    print()
    return -1


def tree_print(levels):
    print(f"Trie levels:")
    i = 0
    for level in levels:
        level = sorted(level, key=lambda x: (x.previous.id, x.name))
        if i >= 1:
            print(f" level {i}:", end="")
            for n in level:
                print(f" ({n.previous.id}-{n.id}, {n.name})", end="")
            print()
        i += 1


def suffix_print(levels):
    print("Suffix function:")
    i = 0
    for level in levels:
        level = sorted(level, key=lambda x: (x.id, x.name))
        print(f" level {i}:", end="")
        for node in level:
            if node.fac == None:
                print(f" <{node.id}: null>", end="")
            else:
                print(f" <{node.id}: {node.fac.id}>", end="")
        print()
        i += 1


def process_text(T, r):
    print(f"Processing the text '{T}':")
    node = r
    for c in T:
        print(f" {c}:", end="")
        if c in node.next:
            print(f" {node.id} {node.next[c].id}", end="")
            node = node.next[c]

        elif node.fac != None:
            print(f" {node.id}", end="")
            while node.fac is not None and c not in node.next:
                print(f" {node.fac.id}", end="")
                node = node.fac
                if c in node.next:
                    print(f" {node.next[c].id}", end="")
                    node = node.next[c]
                    break
                elif node != r:
                    node = node.fac
                    print(f" {node.id}", end="")
            if c in node.next and node.name is not c:
                print(f" {node.next[c].id}", end="")
                node = node.next[c]
        else:
            node = r
            print(f" {node.id}", end="")
        print()


def trie_node(node, s, i, level, levels, prefix):
    node.prefix_to.add(prefix)
    if len(s) == 0:
        return i
    if s[0] not in node.next:
        new_node = Node(s[0], i)
        new_node.previous = node
        new_node.level = level
        if len(levels) < level + 1:
            levels.append([])
        levels[level].append(new_node)
        node.next.update({s[0]: new_node})
        i += 1
    level += 1
    i = trie_node(node.next[s[0]], s[1:], i, level, levels, prefix)
    return i


def main(argv):
    filename = "input3.txt"
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        patterns = f.read().splitlines()
        f.close()

    string = patterns[0]
    patterns = patterns[1:]
    start_node = Node("start", 0)
    start_node.level = 0
    i = 1
    j = 1
    levels = [[start_node]]
    for pattern in patterns:
        prefix = "S" + str(j)
        i = trie_node(start_node, pattern, i, 1, levels, prefix)
        j += 1
    tree_print(levels)
    precomputeFac(start_node, levels)
    print()
    suffix_print(levels)
    print()
    process_text(string, start_node)


if __name__ == '__main__':
    main(sys.argv)
