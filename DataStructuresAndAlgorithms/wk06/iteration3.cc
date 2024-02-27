/**
 * iteration3.cc
 *
 * Print beginning half of a list
 */

/**
 * DO NOT ADD ANY INCLUDES!!
 */

#include <iostream>
#include <iterator> // for iterators
#include <list> // for lists
using namespace std;


void printHalf(const list<int>& lst)
{
  /**
  * Use iterators to go through the list and print elements
  */

  list<int>::const_iterator it;
  list<int>::const_iterator mid_it = lst.begin();
  advance(mid_it, lst.size()/2);

  for (it = lst.begin(); it != mid_it; it++) {
    cout << *it << ' ';
  }
}
