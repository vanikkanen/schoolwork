#include <iostream>
#include <set>

using namespace std;

std::set<char> OK_CHARACTERS = {'#', '*', '/', '+', '-'};

int main()
{
    std::cout << "Input an expression in reverse Polish notation (end with #):" << std::endl;

    std::string input = "";
    std::cout << "EXPR> ";
    std::getline(std::cin, input);

    std::string::size_type str_length = input.size();
    std::string::size_type i = 0;
    char c;

    int operators = 0;
    int operands = 0;

    int array[5];
    int* position = array;

    for (i = 0; i < str_length; ++i)
    {
        c = input.at(i);

        if (c == ' ')
            continue;

        else if (not isdigit(c) and i == 0) {
            std::cout << "Error: Expression must start with a number" << std::endl;
            return EXIT_FAILURE;

        } if ((OK_CHARACTERS.find(c) == OK_CHARACTERS.end()) and !isdigit(c)){
            std::cout << "Error: Unknown character" << std::endl;
            return EXIT_FAILURE;

        } else {
            if (isdigit(c)) {
                ++operands;

                *position = c - '0';
                ++position;

            } else if (c == '#' and i == str_length -1)
            {
                if (operands - 1 > operators) {
                    std::cout << "Error: Too few operators" << std::endl;
                    return EXIT_FAILURE;
                } else if (operands <= operators){
                    std::cout << "Error: Too few operands" << std::endl;
                    return EXIT_FAILURE;
                } else {
                std::cout << "Correct: " << *array << " is the result" << std::endl;
                return EXIT_SUCCESS;
                }

            } else if (OK_CHARACTERS.find(c) != OK_CHARACTERS.end()) {

                ++operators;

                --position;
                int num_2 = *position;
                *position = 0;
                --position;
                int num_1 = *position;

                if (c == '+'){
                    *position = num_1 + num_2;
                } else if (c == '*'){
                    *position = num_1 * num_2;
                } else if (c == '/') {
                    if (num_2 == 0) {
                        std::cout << "Error: Division by zero" << std::endl;
                        return EXIT_FAILURE;
                    } else {
                        *position = num_1 / num_2;
                    }
                } else if (c == '-') {
                    *position = num_1 - num_2;
                }
                ++position;

            }

        }
    }
}
