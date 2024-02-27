#include <iostream>

using namespace std;

int main()
{
    int num = 0;
    cout << "Enter a number: ";
    cin >> num;

    int cube = num * num * num;

    if (num == 0 or (cube / num) / num == num) {
        cout << "The cube of " << num << " is " << cube <<"." << endl;
    } else {
        cout << "Error! The cube of " << num << " is not " << cube <<"." << endl;
    }
}
