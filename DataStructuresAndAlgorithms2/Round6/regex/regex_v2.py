import sys

class State:

    def __init__(self):
        self.id = ""
        self.next = []
        self.visited = False
        self.made_in = ""

    def __repr__(self) -> str:
        return f"{self.id}"


args = sys.argv
if len(args) > 1:
    input_file = args[1]
else:
    input_file = "input1.txt"

input = open(input_file)
nfa_dict = {}
for line in input:
