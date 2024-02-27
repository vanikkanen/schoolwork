#include <iterator>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

struct Place{ int x; int y; string name; };

vector<Place> v;

sort(v.begin(), v.end(), b_sort);


bool b_sort(const Place& A, const Place& B) {
	
  int distA = sqrt(pow(A.x - 0, 2) + pow(A.y - 0, 2));
  int distB = sqrt(pow(B.x - 0, 2) + pow(B.y - 0, 2));

  if (distA < distB) {
    return true;
  }
  else if (distA > distB) {
    return false;
  }

  if ((A.name).compare(B.name) < 0) {
    return true;
  }
  return false;

}