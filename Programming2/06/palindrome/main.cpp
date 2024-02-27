#include <iostream>
#include <string>
#ifndef RECURSIVE_FUNC
#define RECURSIVE_FUNC
#endif

bool palindrome_recursive(std::string s)
{
  RECURSIVE_FUNC
  // Do not remove RECURSIVE_FUNC declaration, it's necessary for automatic testing to work
  // ------------


  // Add your implementation here
    int s_length = s.length();

    char s_begin = s.at(0);
    char s_end = s.at(s_length - 1);
    if (s_begin == s_end) {
        if (s_length <= 2)
            return true;
        else {
        if (s_length > 2)
            s = s.substr(1, s_length - 2);
        if (palindrome_recursive(s)){
            return true;
        } else
            return false;
    }
    }
    else {
      return false;
    }
}

// Do not modify rest of the code, or the automated testing won't work.
#ifndef UNIT_TESTING
int main()
{
    std::cout << "Enter a word: ";
    std::string word;
    std::cin >> word;

    if(palindrome_recursive(word)){
        std::cout << word << " is a palindrome" << std::endl;
    } else {
        std::cout << word << " is not a palindrome" << std::endl;
    }
}
#endif
