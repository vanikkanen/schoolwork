#include <iostream>

using namespace std;

unsigned long int factorial (int num) {
    unsigned long int result = 1;
    while (num > 0) {
        result = result * num;
        --num;
    }
    return result;
}

int main()
{
    int total_balls = 0;
    cout << "Enter the total number of lottery balls: ";
    cin >> total_balls;

    int drawn_balls = 0;
    cout << "Enter the number of drawn balls: ";
    cin >> drawn_balls;

    if ( total_balls <= 0 ) {
        cout << "The number of balls must be a positive number." << endl;
    } else if ( drawn_balls > total_balls ) {
        cout << "The maximum number of drawn balls is the total amount of balls." << endl;
    } else {

        unsigned long int probability = 0;

        probability = factorial(total_balls) / (factorial(total_balls - drawn_balls) * factorial(drawn_balls));

        cout << "The probability of guessing all " << drawn_balls << " balls correctly is 1/" << probability << endl;
        }
        return 0;
}

