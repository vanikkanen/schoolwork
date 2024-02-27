import sys
from queue import PriorityQueue


class Node:

    def __init__(self, node_id):
        self.id = node_id
        self.next_nodes = {}
        self.prev = ""
        self.visited = False

    def add_edge(self, next_node, weight):
        self.next_nodes[next_node] = int(weight)

    def return_id(self):
        return self.id


def MST(G, s):
    mst = []
    cost = 0
    pq = PriorityQueue()

    start_node = G[s]
    start_node.visited = True
    for edge in start_node.next_nodes:
        pq.put((start_node.next_nodes[edge], int(start_node.id), int(edge),
                (edge, start_node.id)))

    i = 1
    while not pq.empty():
        print("** Iteration ", i, " **")
        i += 1
        edge = pq.get()
        node = G[edge[3][0]]
        prev_node = G[edge[3][1]]
        weight = edge[0]
        if not node.visited:
            node.visited = True
            node.prev = prev_node.id
            print(f"Adding the edge ({prev_node.id}, {node.id}, {weight}) "
                  f"with the new node {node.id}")
            mst.append(f"{edge[3][1]}-{edge[3][0]}")
            cost += weight
            for edge in node.next_nodes:
                if not G[edge].visited:
                    pq.put((node.next_nodes[edge], int(node.id), int(edge),
                            (edge, node.id)))
    return mst, cost


def main():

    input = open("input1.txt")
    node_dict = {}
    for line in input:
        param = line.split()
        node_id = param[0]
        next_node_id = param[1]
        weight = param[2]

        #check that node_id and next_node are both existing nodes
        if node_id not in node_dict:
            new_node = Node(node_id)
            node_dict[node_id] = new_node
        if next_node_id not in node_dict:
            new_next_node = Node(next_node_id)
            node_dict[next_node_id] = new_next_node

        node_dict[node_id].add_edge(next_node_id, weight)
        node_dict[next_node_id].add_edge(node_id, weight)

    #print(node_dict)
    print(MST(node_dict, "5"))


if __name__ == "__main__":
    main()