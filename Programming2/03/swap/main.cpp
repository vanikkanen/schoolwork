#include <cstdlib>
#include <iostream>

void swap(int& i, int& j) {
    int new_i = j;
    int new_j = i;

    i = new_i;
    j = new_j;
}

#ifndef UNIT_TESTING
int main()
{
    std::cout << "Enter an integer: ";
    int i = 0;
    std::cin >> i;

    std::cout << "Enter another integer: ";
    int j = 0;
    std::cin >> j;

    swap(i, j);
    std::cout << "The integers are " << i << " and " << j << std::endl;

    return EXIT_SUCCESS;
}
#endif
