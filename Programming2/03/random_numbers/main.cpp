#include <iostream>
#include <random>
#include <string>

using namespace std;

void produce_random_numbers(unsigned int lower, unsigned int upper, unsigned int seed)
{
    default_random_engine gen(seed);

    uniform_int_distribution<int> distr(lower, upper);

    bool on_going = true;
    while (on_going) {
        cout << "" << endl;
        cout << "Your drawn random number is " << distr(gen) << endl;

        cout << "Press c to continue or q to quit: ";
        string command = "";
        cin >> command;

        if (command == "c") {
            continue;
        }
        else if (command == "q") {
            on_going = false;
        }
        else {
            on_going = false;
        }
}
}

int main()
{
    unsigned int lower_bound, upper_bound, seed_value;
    cout << "Enter a lower bound: ";
    cin >> lower_bound;
    cout << "Enter an upper bound: ";
    cin >> upper_bound;

    if(lower_bound >= upper_bound)
    {
        cout << "The upper bound must be strictly greater than the lower bound"
             << endl;
        return EXIT_FAILURE;
    }
    cout << "Enter a seed value: ";
    cin >> seed_value;

    produce_random_numbers(lower_bound, upper_bound, seed_value);

    return EXIT_SUCCESS;
}
