import sys
from queue import PriorityQueue


class Edge:

    def __init__(self, from_node_id, to_node_id,  weight):
        self.from_node = from_node_id
        self.to_node = to_node_id
        self.weight = int(weight)


def MST(G, s):
    mst = []
    visited_nodes = []
    cost = 0
    pq = PriorityQueue()
    visited_nodes.append(s)
    for edge_iter in G:
        edge = G[edge_iter]
        if edge.from_node == s or edge.to_node == s:
            pq.put((edge.weight, int(edge.from_node), int(edge.to_node)))

    i = 1
    while not pq.empty():
        print("** Iteration", i, "**")
        i += 1
        [weight, from_node, to_node] = pq.get()
        edge = G[(str(from_node), str(to_node))]

        if edge.from_node not in visited_nodes or edge.to_node not in visited_nodes:

            if edge.from_node not in visited_nodes:
                u = edge.from_node
                visited_nodes.append(u)
            elif edge.to_node not in visited_nodes:
                u = edge.to_node
                visited_nodes.append(u)
            print(
                f"Adding the edge ({edge.from_node}, {edge.to_node}, "
                f"{weight}) with the new node {u}")
            mst.append(edge)
            cost += weight
            for edge_iter in G:
                new_edge = G[edge_iter]
                if new_edge.from_node == u:
                    if new_edge not in mst and new_edge.to_node not in \
                            visited_nodes:
                        pq.put((new_edge.weight, int(new_edge.from_node),
                                int(new_edge.to_node)))
                elif new_edge.to_node == u:
                    if new_edge not in mst and new_edge.from_node not in \
                            visited_nodes:
                        pq.put((new_edge.weight, int(new_edge.from_node),
                                int(new_edge.to_node)))

    return mst, cost


def main(argv):

    input = open(sys.argv[1])
    edge_dict = {}
    for line in input:
        param = line.split()
        node_id = param[0]
        next_node_id = param[1]
        weight = param[2]

        new_edge = Edge(node_id, next_node_id, weight)
        edge_dict[(node_id, next_node_id)] = new_edge

    edges, cost = MST(edge_dict, sys.argv[2])
    results = []
    for edge in edges:
        results.append((int(edge.from_node), int(edge.to_node)))
    sorted_results = sorted(results, key=lambda x: (x[0], x[1]))

    print(f"MST({cost}):", end="")
    for i in sorted_results:
        print(f" {i[0]}-{i[1]}", end="")
    print()


if __name__ == "__main__":
    main(sys.argv)