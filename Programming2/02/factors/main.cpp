#include <iostream>

using namespace std;

int main()
{
    int num = 0;
    cout << "Enter a positive number: ";
    cin >> num;

    if ( num <= 0 ) {
        cout << "Only positive numbers accepted" << endl;
    } else {
      int part1 = 1;
      int part2 = num;
      int working_part1 = 0;
      int working_part2 = 0;

      while (part1 <= part2) {

          if (part1 * part2 == num) {
              working_part1 = part1;
              working_part2 = part2;
          }

          ++part1;
          if (num % part1 == 0) {
              part2 = num / part1;
          }
      }
      cout << num << " = " << working_part1 << " * " << working_part2 << endl;
    }
    return 0;
}
