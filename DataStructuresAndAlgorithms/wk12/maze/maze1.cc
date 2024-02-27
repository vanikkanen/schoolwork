#include <iterator>
#include <vector>
#include <algorithm>
#include <set>
#include "maze.hh"

using namespace std;

// Remember to implement your own container here or in another cc file to store the nodes in the maze
// If you define it elsewhere, remember to make sure it's accessible by this file as well.

/**
 * @brief Create a Node object
 * 
 * @param loc  The location of the node
 * @return Node*  A pointer to the node that is created. If the node already exists, return a pointer to the existing node
 */
Node* createNode  (std::pair<int, int> loc, std::map<std::string, Node*> paths) {
    // try to find by location
    auto it = std::find_if(all_maze_nodes.begin(), all_maze_nodes.end(), [loc](Node* a){
       return a->loc == loc;
    });
    // found
    if (it != all_maze_nodes.end()) {
        return &**it;
    }
    // not found
    else {
        Node* new_node = new Node {paths[ABOVE], paths[BELOW], paths[LEFT], paths[RIGHT], loc};
        all_maze_nodes.push_back(new_node);
        return &*all_maze_nodes.back();
    }
}
