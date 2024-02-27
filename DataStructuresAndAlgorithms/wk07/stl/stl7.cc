#include <iterator>
#include <vector>
#include <algorithm>

#include "test.hh" // NOT_FOUND constant

using namespace std;


/**
 * @brief Find the median value of a given vector, whose elements are in random
 *        order. Return NOT_FOUND if the size of the vector is zero.
 *
 * @param v a random vector
 * @return int
 */
int findMedian(std::vector<int>& v)
{
    // tyhjä ja jos kaksi keskimmäistä
    if (v.begin() == v.end()) {
        return NOT_FOUND;
    }
    if (v.size()%2 != 0) {
        sort(v.begin(), v.end());
        auto mid = v.begin() + v.size() / 2;
        return *mid;
    }
    else {
        sort(v.begin(), v.end());
        auto mid2 = v.begin() + v.size() / 2;
        auto mid1 = mid2 - 1;
        return (*mid1 + *mid2)/2;
    }
}

