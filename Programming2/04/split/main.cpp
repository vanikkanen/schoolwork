#include <iostream>
#include <string>
#include <vector>

std::vector <std::string> split(std::string line, char separator, bool no_empty = false) {

    std::vector <std::string> parts;
    std::string::size_type line_length = line.size();

    std::string::size_type index = 0;

    char line_char;
    std::string part;

    for ( index = 0; index < line_length; ++index ) {
        line_char = line.at(index);

        if ( line_char == separator ) {
            if ( no_empty == true and part == "") {
                continue;
            } else {
            parts.push_back(part);
            part = "";
            }
        } else {
            part += line_char ;
        }
    }
    parts.push_back(part);
    return parts;
}


int main()
{
    std::string line = "";
    std::cout << "Enter a string: ";
    getline(std::cin, line);
    std::cout << "Enter the separator character: ";
    char separator = getchar();

    std::vector< std::string > parts  = split(line, separator);
    std::cout << "Splitted string including empty parts: " << std::endl;
    for( auto part : parts ) {
        std::cout << part << std::endl;
    }

    std::vector< std::string > parts_no_empty  = split(line, separator, true);
    std::cout << "Splitted string ignoring empty parts: " << std::endl;
    for( auto part : parts_no_empty ) {
        std::cout << part << std::endl;
    }
}
