#include <iterator>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include "maze.hh"

using namespace std;

// Remember to implement your own container here or in another cc file to store the nodes in the maze
// If you define it elsewhere, remember to make sure it's accessible by this file as well.


/**
 * @brief Find the shortest path from startNode to endNode using Djikstra's algorithm, where all path distances are 1
 * @param startNode  The node to start the search from
 * @param endNode  The node to end the search at
 * @param path  The path from startNode to endNode. If no path is found or if startNode is the same as endNode, path should be empty. The path should be in the order of the nodes visited, starting with startNode and ending with endNode
 * @return bool True if a path was found, false otherwise
 */

bool findShortestPath(Node &startNode, Node &endNode, std::vector<std::pair<int, int>>& path) {


    if (&startNode == &endNode) {
        return true;
    }
    std::vector<std::string> directions{ABOVE, BELOW, LEFT, RIGHT};
    // Dijkstra
    auto comp = [](Node* a, Node* b) { return a->cost > b->cost;};
    std::priority_queue<Node*, vector<Node*>, decltype(comp)> Q(comp);

    startNode.color = "gray";
    startNode.cost = 0;

    Q.push(&startNode);
    while(!Q.empty()) {

        auto u = Q.top();
        // goal
        if (u == &endNode) {
            path.push_back(u->loc);
            Node* pi = u->PI;
            while (pi != &startNode) {
                path.push_back(pi->loc);
                pi = pi->PI;
            }
            path.push_back(pi->loc);
            std::reverse(path.begin(), path.end());
            return true;
        }

        for (const auto &dir : directions) {
            auto v = getNeighbour(dir, *u);
            if (v == nullptr) {
                continue;
            }
            // Relax
            bool cheaper = false;;
            if (v->cost == -1  || v->cost > u->cost + 1) {
                v->cost = u->cost + 1;
                v->PI = u;
                cheaper = true;
            }
            // After relax
            if (v->color == "white") {
                v->color = "gray";
                Q.push(v);
            } else {
                if (cheaper) {
                    Q.push(v);
                }
            }
        }
        u->color = "black";
        Q.pop();
    }
    return false;
}
