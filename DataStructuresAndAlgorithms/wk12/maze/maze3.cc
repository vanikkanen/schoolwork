#include <iterator>
#include <vector>
#include <algorithm>
#include "maze.hh"

using namespace std;

// Remember to implement your own container here or in another cc file to store the nodes in the maze
// If you define it elsewhere, remember to make sure it's accessible by this file as well.


/**
 * @brief Connect two adjacent nodes together. If the nodes are not adjacent, do nothing
 * 
 * @param fromNode  The node to connect from
 * @param toNode  The node to connect to
 */
void connectNodes(Node& node1, Node& node2) {
    // Check if nodes are adjacent

    // node1 LEFT of node2
    if (node1.loc.first + 1 == node2.loc.first && node1.loc.second == node2.loc.second) {
        node1.RIGHT = &node2;
        node2.LEFT = &node1;
    }
    // node1 RIGHT of node2
    else if (node1.loc.first - 1 == node2.loc.first &&node1.loc.second == node2.loc.second) {
        node1.LEFT = &node2;
        node2.RIGHT = &node1;
    }
    // node1 BELOW node2
    else if (node1.loc.second + 1 == node2.loc.second && node1.loc.first == node2.loc.first) {
        node1.ABOVE = &node2;
        node2.BELOW = &node1;
    }
    // node1 ABOVE node2
    else if (node1.loc.second - 1 == node2.loc.second && node1.loc.first == node2.loc.first) {
         node1.BELOW = &node2;
         node2.ABOVE = &node1;
    }
}
