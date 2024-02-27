#include <iostream>
#include <string>
#include <algorithm>
#include <random>

int main()
{
    // This is a random number generator that should be given as parameter to the
    // function of the algorithm library to shuffle letters
    std::minstd_rand generator;

    std::cout << "Enter some text. Quit by entering the word \"END\"." << std::endl;
    std::string word;

    while (std::cin >> word)
    {
        if (word == "END")
        {
            return EXIT_SUCCESS;
        }

        std::string::iterator word_first = word.begin();
        std::string::iterator word_last = word.end();

        if (word.length() > 3){
            ++word_first;
            --word_last;

            shuffle(word_first, word_last, generator);
        }
        std::cout << word << std::endl;
    }
}
