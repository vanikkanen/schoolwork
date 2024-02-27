#ifndef TEST_HH
#define TEST_HH

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

const int NOT_FOUND = -1;


/**
 * @brief duplicates even numbers in the vector, removes uneven numbers. Example: {1, 2, 3, 4} -> {2, 2, 4, 4}
 *
 * @param vec vector to be handled
 */
void duplicateEvenRemoveUneven(std::vector<int>& vec) {

    auto end = std::remove_if(vec.begin(), vec.end(), [] (int const &i) {return i & 1;});
    vec.erase(end, vec.end());

    std::copy(vec.begin(), vec.end(), std::ostream_iterator<int>(std::cout, " "));
	std::cout << std::endl << std::endl;

    vec.reserve(vec.size()*2);

    for ( auto it = vec.begin(); it < vec.end();){

            std::cout << "Iterator pos: " << it - vec.begin() << " Iterator val: " << *it << std::endl;

            vec.insert(it + 1, *it);

            std::copy(vec.begin(), vec.end(), std::ostream_iterator<int>(std::cout, " "));
            std::cout << std::endl << std::endl;

            advance(it, 2);
        }
}


/**
 * @brief creates a vector with ascending numbers from 0 - n-1
 *
 * @param n the size of the vector to be created
 */
std::vector<int> ascendingVector(int n) {
    std::vector<int> v;
    for (int i = 0; i < n; ++i) {   
        v.push_back(i); 
    }

    return v;
}

/**
 * @brief Erases every second item from the vector. Example: {1, 2, 3, 4} -> {1, 3}
 *
 * @param vec vector where every second item is erased.
 */
void eraseEverySecond(std::vector<int>& vec) {
    auto size = vec.size();
    auto mid = size/2;
    for(int i = 0; i < mid; ++i){
        vec.erase(vec.begin() + (i+1));
    }
}

#endif // TEST_HH
