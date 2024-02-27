#include <iterator>
#include <map>
#include <algorithm>

#include "test.hh" // NOT_FOUND constant

using namespace std;


/**
 * @brief From a map find the first element, whose value is at least given limit
 *        regardless of the key of the element. Return only the value or
 *        NOT_FOUND if none of the values match the the search criteria.
 * @param m map that is scanned trough
 * @param given
 * @return int
 */
int findAtLeastGiven(std::map<std::string, int>& m, int given)
{
    auto element = find_if(m.begin(), m.end(), [given](auto & x) -> bool { return x.second > given;});
    if (element != m.end()) {
        return element->second;
    } else {
        return NOT_FOUND;
    }
}

