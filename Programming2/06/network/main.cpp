#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

const std::string HELP_TEXT = "S = store id1 i2\nP = print id\n"
                              "C = count id\nD = depth id\n";


std::vector<std::string> split(const std::string& s, const char delimiter, bool ignore_empty = false){
    std::vector<std::string> result;
    std::string tmp = s;

    while(tmp.find(delimiter) != std::string::npos)
    {
        std::string new_part = tmp.substr(0, tmp.find(delimiter));
        tmp = tmp.substr(tmp.find(delimiter)+1, tmp.size());
        if(not (ignore_empty and new_part.empty()))
        {
            result.push_back(new_part);
        }
    }
    if(not (ignore_empty and tmp.empty()))
    {
        result.push_back(tmp);
    }
    return result;
}

void print_tree(std::map<std::string, std::vector<std::string>> network, std::string id, int recursion)
{
    ++recursion;
    if (network.find(id) != network.end()){
        for (auto person : network.at(id)){
                std::cout << std::string(recursion*2, '.') << person << std::endl;
                print_tree(network, person, recursion);
        }
    }
}

int count_tree(std::map<std::string, std::vector<std::string>> network, std::string id, int& sum)
{
    if (network.find(id) != network.end()){
        sum += network.at(id).size();
        for (auto person : network.at(id)) {
            count_tree(network, person, sum);
        }
    }
    return sum;
}

int tree_depth(std::map<std::string, std::vector<std::string>> network, std::string id, int depth, int& max_depth)
{
        ++depth;

        if (depth > max_depth)
            max_depth = depth;

        if (network.find(id) != network.end()){
            if (network.at(id).size() > 0)
                for (auto person : network.at(id)){
                    tree_depth(network, person, depth, max_depth);
                }
            }
    if (depth > max_depth)
        max_depth = depth;
    return max_depth;
}

int main()
{
    // TODO: Implement the datastructure here
    std::map<std::string, std::vector<std::string>> network;

    while(true){
        std::string line;
        std::cout << "> ";
        getline(std::cin, line);
        std::vector<std::string> parts = split(line, ' ', true);

        std::string command = parts.at(0);

        if(command == "S" or command == "s"){
            if(parts.size() != 3){
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id1 = parts.at(1);
            std::string id2 = parts.at(2);

            if ( network.find(id1) != network.end() ){
                network[id1].push_back(id2);
            } else {
                network[id1];
                network[id1].push_back(id2);
            }

        } else if(command == "P" or command == "p"){
            if(parts.size() != 2){
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            if (network.find(id) != network.end()) {
                std::cout << id << std::endl;
                int recursion = 0;
                print_tree(network, id, recursion);
            } else
                std::cout << 0 << std::endl;

        } else if(command == "C" or command == "c"){
            if(parts.size() != 2){
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            if (network.find(id) != network.end()) {
                int sum = 0;
                std::cout << count_tree(network, id, sum) << std::endl;
            } else
                std::cout << 0 << std::endl;

        } else if(command == "D" or command == "d"){
            if(parts.size() != 2){
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            if (network.find(id) != network.end()) {
                int depth = 0;
                int max_depth = 0;
                std::cout << tree_depth(network, id, depth, max_depth) << std::endl;
            } else
                std::cout << 1 << std::endl;

        } else if(command == "Q" or command == "q"){
           return EXIT_SUCCESS;
        } else {
            std::cout << "Erroneous command!" << std::endl << HELP_TEXT;
        }
    }
}
/*
 *
void print_tree(std::map<std::string, std::vector<std::string>> network, std::string id, int& recursion)
{
    if (network.find(id) != network.end()){

        if (network.at(id).size() > 0){

            for (auto person : network.at(id)){

                std::cout << std::string(recursion*2, '.') << person << std::endl;
                ++recursion;
                print_tree(network, person, recursion);
            }
            --recursion;
        } else {
            --recursion;
            }
       } else {
        --recursion;
        }
}
 */
