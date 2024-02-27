import sys
import random


class Node:

    def __init__(self, name):
        self.name = name
        self.next = []
        self.type = None
        self.prev = None

    def __repr__(self) -> str:
        return f"{self.name} {self.type}"


class State:

    def __init__(self):
        self.next = []
        self.visited = False
        self.made_in = ""
        self.incoming_connections = []

    def __repr__(self) -> str:
        return f"{self.id}"


def nfa_builder(regex_nodes, node):
    node = regex_nodes[node]
    if not node.next:
        state1 = State()
        state1.made_in = [node.type, node.name]
        if "\\" not in node.type:
            prev_state = state1
            for c in node.type:
                new_state = State()
                new_state.made_in = node.type
                prev_state.next.append([c, new_state, prev_state])
                new_state.incoming_connections.append(prev_state)
                prev_state = new_state
            return state1, prev_state

        else:
            state2 = State()
            state2.made_in = [node.type, node.name]
            if "." in node.type:
                state1.next.append([".", state2, state1])
            else:
                state1.next.append([node.type, state2, state1])
            state2.incoming_connections.append(state1)
            return state1, state2

    if node.type == "concat" or node.type == "|":
        both = False

    for next_node in node.next:
        start_state, end_state = nfa_builder(regex_nodes,next_node)

        if node.type == "+":
            end_state.next.append(["EPS", start_state, end_state])
            start_state.incoming_connections.append(end_state)
            return start_state, end_state

        elif node.type == "*":
            state1 = State()
            state2 = State()
            state1.made_in = node.type
            state2.made_in = node.type
            state1.next.append(["EPS", start_state, state1])
            start_state.incoming_connections.append(state1)
            state1.next.append(["EPS", state2, state1])
            state2.incoming_connections.append(state1)
            end_state.next.append(["EPS", start_state, end_state])
            start_state.incoming_connections.append(end_state)
            end_state.next.append(["EPS", state2, end_state])
            state2.incoming_connections.append(end_state)
            return state1, state2

        elif node.type == "concat":
            if not both:
                start_state_1, end_state_1 = start_state, end_state
                both = True
            else:
                for incoming_state in start_state.incoming_connections:
                    for next_next_state in incoming_state.next:
                        if next_next_state[1] is start_state:
                            next_next_state[1] = end_state_1
                for next_state in start_state.next:
                    next_state[2] = end_state_1


                end_state_1.next.extend(start_state.next)
                del start_state
                both = False
                return start_state_1, end_state

        elif node.type == "|":
            if not both:
                start_state_1, end_state_1 = start_state, end_state
                both = True
            else:
                state1 = State()
                state2 = State()
                state1.made_in = node.type
                state2.made_in = node.type
                state1.next.append(["EPS", start_state_1, state1])
                start_state_1.incoming_connections.append(state1)
                state1.next.append(["EPS", start_state, state1])
                start_state.incoming_connections.append(state1)
                end_state_1.next.append(["EPS", state2, end_state_1])
                state2.incoming_connections.append(end_state_1)
                end_state.next.append(["EPS", state2, end_state])
                state2.incoming_connections.append(end_state)
                both = False
                return state1, state2


def BFS(s):
    layers = []
    newLayer = []
    i = 0
    newLayer.append(s)
    s.id = i
    i += 1
    s.visited = True
    while newLayer:
        if newLayer[0].next:
            layers.append(newLayer)
        expandLayer = []
        for state in newLayer:
            for next_state in state.next:
                if not next_state[1].visited:
                    next_state[1].id = i
                    i += 1
                    next_state[1].visited = True
                    expandLayer.append(next_state[1])

        newLayer = expandLayer
    return layers


args = sys.argv
if len(args) > 1:
    input_file = args[1]
else:
    input_file = "input2.txt"

input = open(input_file).read().splitlines()
regex_dict = {}
for line in input:
    attr = line.split()
    new_node = Node(int(attr[0]))
    new_node.type = attr[1]
    new_node.next = [eval(i) for i in attr[2:]]
    regex_dict[int(attr[0])] = new_node
for line in input:
    attr = line.split()
    name = attr[0]
    type = attr[1]
    nexts = [eval(i) for i in attr[2:]]
    for node in nexts:
        regex_dict[node].prev = name


start_state, end_state = nfa_builder(regex_dict, 0)
levels = BFS(start_state)
print("NFA transitions:")
i = 1
for level in levels:
    print(f"Level {i}:", end="")
    transition_list = []
    for node in level:
        for transition in sorted(node.next, key=lambda x: (x[0].startswith(
                                                            "EPS"), x[2].id)):
            transition_list.append([transition[0], transition[1].id, transition[2].id])

    for transition in transition_list:
        print(f" [{transition[2]}-{transition[1]}: {transition[0]}]", end="")
    i += 1
    transition_list = []
    print()