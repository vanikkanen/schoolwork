#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;


/**
 * @brief duplicates even numbers in the vector, removes uneven numbers. Example: {1, 2, 3 4} -> {2, 2, 4, 4}
 *
 * @param vec vector to be handled
 */
void duplicateEvenRemoveUneven(std::vector<int>& vec) {

    auto end = std::remove_if(vec.begin(), vec.end(), [] (int const &i) {return i & 1;});
    vec.erase(end, vec.end());

    vec.reserve(vec.size()*2);

    for ( auto it = vec.begin(); it < vec.end();){
            vec.insert(it + 1, *it);
            advance(it, 2);
        }
}

