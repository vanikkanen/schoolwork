#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;


/**
 * @brief Arrange vector in three subsequent sections:
 *        - those divisible by three (asc order)
 *        - those whose reminder is 1 (asc order)
 *        - those whose reminder is 2 (asc order)
 * @param v a sortable vector
 * @return int EXIT_SUCCESS if everything went OK, EXIT_FAILURE otherwise
 */
int sortMod3(std::vector<int>& v)
{
    if (v.begin() == v.end()) {
    return EXIT_SUCCESS;
  }

  // sort to get x % 3 == 0
    sort(v.begin(), v.end(), [](int a, int b) {
        return a % 3 == 0;
    });
    // find the first not ok iterator
    auto it0 = find_if(v.rbegin(), v.rend(), [](int a) {
        return a % 3 == 0;
    }).base();
    sort(v.begin(), it0);
    
    // sort to get x % 3 == 1
    sort(it0, v.end(), [](int a, int b) {
        return a % 3 == 1;
    });
    // find the first not ok iterator
    it0 = find_if(v.begin(), v.end(), [](int a) {
    	return a % 3 == 1;
    });
    auto it1 = find_if(v.rbegin(), make_reverse_iterator(it0), [](int a) {
        return a % 3 == 1;
    }).base(); 
    sort(it0, it1);
    
    // sort to get x % 3 == 2
  	sort(it1, v.end(), [](int a, int b) {
        return a % 3 == 2;
    });
    // find the first not ok iterator
  	it1 = find_if(v.begin(), v.end(), [](int a) {
    	return a % 3 == 2;
    });
    auto it2 = find_if(v.rbegin(), make_reverse_iterator(it1), [](int a) {
        return a % 3 == 2;
    }).base();
    sort(it1, it2);

    if (it0 == v.end() || it1 == v.end() || it2 == v.end()) {
      return EXIT_SUCCESS;
    } else {
      return EXIT_FAILURE;
    }
}

