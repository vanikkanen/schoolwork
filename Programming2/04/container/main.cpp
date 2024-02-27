#include <cstdlib>
#include <iostream>
#include <vector>


void read_integers(std::vector< int >& ints, int count)
{
    int new_integer = 0;
    for(int i = 0; i < count; ++i)
    {
        std::cin >> new_integer;
        ints.push_back(new_integer);
    }
}

bool same_values(const std::vector< int > ints)
{
    for ( auto vector_int : ints ) {
        if ( ints.at(0) != vector_int )
            return false;
    }
    return true;
}

bool is_ordered_non_strict_ascending(const std::vector< int > ints)
{
    int previous_int = ints.at(0);
    for ( auto vector_int : ints ) {
        if ( previous_int > vector_int )
            return false;
        previous_int = vector_int;
    }
    return true;
}

bool is_arithmetic_series(const std::vector< int > ints)
{
    int size = ints.size();
    int index;
    int int_gap = ints.at(0) - ints.at(1);

    for (index = 1; index < size - 1; ++index) {
        if (ints.at(index) - ints.at(index + 1) != int_gap) {
            return false;
        }
    }
    return true;
}

bool is_geometric_series(const std::vector< int > ints)
{
    int size = ints.size();
    int index;

    int zeros = 0;
    for ( auto vector_int : ints ) {
        if (  vector_int == 0 ) {
            ++zeros;
        }
    }

    if (zeros == size) {
        return false;
    }

    int int_ratio = ints.at(1) / ints.at(0);
    for (index = 1; index < size - 1; ++index) {
        if (ints.at(index + 1) / ints.at(index) != int_ratio ) {
            return false;
        }
    }
    return true;
}

int main()
{

    std::cout << "How many integers are there? ";
    int how_many = 0;
    std::cin >> how_many;

    std::cout << "Enter the integers: ";
    std::vector<int> integers;
    read_integers(integers, how_many);

    if(same_values(integers))
        std::cout << "All the integers are the same" << std::endl;
     else
        std::cout << "All the integers are not the same" << std::endl;

    if(is_ordered_non_strict_ascending(integers))
        std::cout << "The integers are in a non-strict ascending order" << std::endl;
    else
        std::cout << "The integers are not in a non-strict ascending order" << std::endl;

    if(is_arithmetic_series(integers))
        std::cout << "The integers form an arithmetic series" << std::endl;
    else
        std::cout << "The integers do not form an arithmetic series" << std::endl;

    if(is_geometric_series(integers))
        std::cout << "The integers form a geometric series" << std::endl;
    else
        std::cout << "The integers do not form a geometric series" << std::endl;

    return EXIT_SUCCESS;
}
