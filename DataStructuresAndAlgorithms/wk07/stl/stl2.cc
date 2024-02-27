#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;


/**
 * @brief sort a given vector to an descending order
 *
 * @param v a vector to be sorted
 * @return int EXIT_SUCCESS if everything went OK, EXIT_FAILURE otherwise
 */
int sortDesc(std::vector<int>& v)
{
    try
  {
    sort(v.begin(), v.end(), greater<int>());
    return EXIT_SUCCESS;
  }
  catch(const std::exception& e)
  {
    return EXIT_FAILURE;
  }
}

