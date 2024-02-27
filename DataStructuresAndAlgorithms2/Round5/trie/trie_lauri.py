import sys


class Node:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.level = -1
        self.next = {}
        self.previous = self
        self.prefix_to = set()

    def __repr__(self) -> str:
        return f"{self.name=}, {self.id=}"


def bin_search(level, c):
    low = 0
    high = len(level)
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
    string_file = "strings1"
    pattern_file = "patterns1"
    if len(argv) > 1:
        string_file = argv[1]
        pattern_file = argv[2]

    with open(string_file) as f:
        strings = f.read().splitlines()
        f.close()
    with open(pattern_file) as f:
        patterns = f.read().splitlines()
        f.close()

    tree = {"start": (0, {})}
    start_node = Node("start", 0)
    start_node.level = 0
    i = 1
    j = 1
    levels = [[start_node]]
    for string in strings:
        prefix = "S" + str(j)
        i = trie_node(start_node, string, i, 1, levels, prefix)
        j += 1
    a = 'a'
    tree_print(levels)
    for pattern in patterns:
        print()
        print(f"Matching P = {pattern}")
        next = list(start_node.next.values())
        next_node = 1
        while len(pattern) > 0 and next_node:
            print(f"  searching {pattern[0]}:", end="")
            next_node = bin_search(next, pattern[0])
            pattern = pattern[1:]
            if len(pattern) == 0 and not next_node == -1:
                print(f"  P matches with (prefixes of): ", end="")
                print(*sorted(next_node.prefix_to, key=lambda x: int("".join([i for i in x if i.isdigit()]))))

            if not next_node == -1:
                next = list(next_node.next.values())


if __name__ == '__main__':
    main(sys.argv)
