/*
 * Ohjelma, joka käynnistyessään lukee ratikkalinjoihin liittyviä tietoja
 * tiedostosta,tallentaa ne sopivaan tietorakenteeseen ja antaa käyttäjälle
 * mahdollisuuden tehdä hakuja,lisäyksiä ja poistoja kyseiseen
 * tietorakenteeseen.
 *
 * Ohjelman kirjoittajat
 * Nimet: Valtteri Nikkanen, Atte Harmoinen
 * Opiskelijanumerot: 282688, 284930
 * Käyttäjätunnus: nikkanev (Koodi on tehty tällä), harmoine
 * E-Mail: valtteri.nikkanen@tuni.fi, atte.harmoinen@tuni.fi
 *
 * In english:
 *
 * Program that reads a file as it is started and saves the data to a sensible
 * data structure. The program then allows the user to print or modify the data
 * saved in the data structure as the user wants to. The program makes error
 * checking and doesnt allow the user to make the wrong kind of or nonsensical
 * edits or modifications. Program lets the user Print, Add, or remove stops and
 * print or add lines to the data structure. These modifications dont affect the
 * original source file for the non modified data.
 *
 * Writers of the program:
 * Names: Valtteri Nikkanen, Atte Harmoinen
 * Student numbers: 282688, 284930
 * User id's: nikkanev (The code was written with this), harmoine
 * E-mail: valtteri.nikkanen@tuni.fi, atte.harmoinen@tuni.fi
 * */

#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>

using Tramway_type = std::map<std::string,std::map<std::string,double>>;

// The most magnificent function in this whole program.
// Prints a RASSE
void print_rasse()
{
    std::cout <<
                 "=====//==================//===\n"
                 "  __<<__________________<<__   \n"
                 " | ____ ____ ____ ____ ____ |  \n"
                 " | |  | |  | |  | |  | |  | |  \n"
                 " |_|__|_|__|_|__|_|__|_|__|_|  \n"
                 ".|                  RASSE   |. \n"
                 ":|__________________________|: \n"
                 "___(o)(o)___(o)(o)___(o)(o)____\n"
                 "-------------------------------" << std::endl;
}
// Adds the vector containing the right data to the data structure
bool add_to_map(Tramway_type& tramways, std::vector<std::string> words)
{
    if (tramways.find(words.at(0)) != tramways.end())
    {
        if (tramways.at(words.at(0)).find(words.at(1)) !=
                tramways.at(words.at(0)).end())
        {
           std::cout << "Error: Stop/line already exists." << std::endl;
           return false;
        }

        else
        {
            for (auto stops : tramways.at(words.at(0)))
            {
                if (stops.second == stod(words.at(2)))
                {
                    std::cout << "Error: Stop/line already exists."
                              << std::endl;
                    return false;
                }
            }
           if (tramways.find(words.at(0)) != tramways.end())
               tramways.at(words.at(0))[words.at(1)]=stod(words.at(2));
           else
           {
               tramways[words.at(0)];
               tramways.at(words.at(0))[words.at(1)]=stod(words.at(2));
           }
        }
    }
    else
    {
        tramways[words.at(0)];
        tramways.at(words.at(0))[words.at(1)]=stod(words.at(2));
    }
    return true;
}
// Converts a given strings words to a vector with the given separator
//character
std::vector<std::string> string_to_vector(std::string str, char separator)
{
    bool quote = false;
    std::vector<std::string> words;
    std::string new_word = "";
    std::string::size_type line_length = str.size();
    std::string::size_type i = 0;
    char c;

    if(str == "")
    {
        words.push_back(new_word);
        return words;
    }

    for (i = 0; i < line_length; ++i)
    {
        c = str.at(i);
        if (c == '"')
            {
                if (quote)
                    quote = false;
                else
                    quote = true;
            }
        else if (c == separator and quote == false)
        {
            words.push_back(new_word);
            new_word = "";
        }
        else
            new_word += c;
    }
    if (new_word != "")
        words.push_back(new_word);

    return words;
}
// Reads the file and checks that everything is as it is supposed to be
bool read_file(Tramway_type& tramways, std::ifstream& input_file)
{
    std::string line = "";
    std::vector<std::string> words;

    while (getline(input_file, line))
    {
            words = string_to_vector(line, ';');

            if (words.size() > 3 or words.size() < 2)
            {
                std::cout << "Error: Invalid format in file." << std::endl;
                return false;
            }

            if (words.at(0) == "" or words.at(1) == "")
            {
                std::cout << "Error: Invalid format in file." << std::endl;
                return false;
            }

            if (words.size() == 2)
                words.push_back("0");

            bool adding_succesful = add_to_map(tramways, words);

            if (adding_succesful == false)
                return false;

            words.clear();
    }
    return true;
}
// Prints all the lines that are in the data structure
void print_lines(const Tramway_type tramways)
{
    std::cout << "All tramlines in alphabetical order:" << std::endl;
    for (auto lines : tramways)
        std::cout << lines.first  << std::endl;
}
// Prints all the stops in the line in question
void print_line_stops(const Tramway_type tramways, std::string line)
{
    std::cout << "Line " << line << " goes through these stops in the order"
                                    " they are listed:" << std::endl;
    if (not tramways.at(line).empty())
    {
        std::map<double, std::string> sorted_line;
        for (auto stops : tramways.at(line))
            sorted_line[stops.second] = stops.first;

        for (auto stops : sorted_line)
            std::cout << " - " << stops.second << " : " << stops.first
                      << std::endl;
    }
}
// Prints all the stops in all the lines
void print_stops(const Tramway_type tramways)
{
    std::cout << "All stops in alphabetical order:" << std::endl;

    std::set<std::string> all_stops;

    for (auto line : tramways)
    {
        for (auto line_stops : line.second)
            all_stops.insert(line_stops.first);
    }

    for (auto stop : all_stops)
        std::cout << stop << std::endl;
}
// Prints all the lines the stop in question is found in
void print_stop_in_lines(const Tramway_type tramways, std::string stop)
{
    std::cout << "Stop " << stop << " can be found on the following lines:" << std::endl;
    for (auto line : tramways)
    {
        if (line.second.find(stop) != line.second.end())
            std::cout << " - " << line.first << std::endl;
    }
}
// Checks that the user input vector isnt smaller thań the required ammount of
// parameters number of parameters
bool input_size_ok(std::vector<std::string> user_input, std::string::size_type param_nr)
{
    if (user_input.size() < param_nr)
        return false;
    else
        return true;
}
// Checks that the user input is as it is supposed to be
bool input_not_ok(const Tramway_type tramways, std::vector<std::string> user_input,
              std::string::size_type param_nr, bool line)
{
    if (!(input_size_ok(user_input, param_nr)))
    {
        std::cout << "Error: Invalid input." << std::endl;
        return true;
    }

    else
    {
        if (line)
        {
            if (tramways.find(user_input.at(1)) == tramways.end())
            {
                std::cout << "Error: Line could not be found." << std::endl;
                return true;
            }
            else
                return false;
        }
        else
        {
            for (auto tramline : tramways)
                if (tramline.second.find(user_input.at(1)) != tramline.second.end())
                    return false;
        }
        std::cout << "Error: Stop could not be found." << std::endl;
        return true;

    }
}

// Changes the command word to be uppercase letters only
void cmd_word_toupper(std::vector<std::string>& user_input)
{
    std::string new_word = "";
    std::string::size_type str_length = user_input.at(0).size();
    std::string::size_type i = 0;
    char c;

        for (i = 0; i < str_length; ++i)
        {
            c = user_input.at(0).at(i);
            new_word += toupper(c);
        }

        user_input.erase(user_input.begin());
        user_input.insert(user_input.begin(), new_word);
}
// Checks that the stop is in the line and returns true or false depending on if
// the stop is wanted to be there or not.
bool stop_in_line(const Tramway_type tramways, std::string line, std::string stop, bool opposite)
{
    if (tramways.at(line).find(stop) == tramways.at(line).end())
    {
        if (!opposite)
        {
            std::cout << "Error: Stop could not be found." << std::endl;
            return false;
        }
        else
            return true;
    }
    else
    {
        if (!opposite)
            return true;
        else
        {
            std::cout << "Error: Stop/line already exists." << std::endl;
            return false;
        }
    }
}
// Calculates the distance between two stops in a line.
void calc_distance(const Tramway_type tramways, std::string line, std::string stop1, std::string stop2)
{
    std::cout << "Distance between " << stop1 << " and " << stop2 << " is ";

    double distance_between = 0;

    distance_between = tramways.at(line).at(stop1) - tramways.at(line).at(stop2);

    std::cout << std::abs(distance_between) << std::endl;
}
// Adds a line to the data structure
void add_line(Tramway_type& tramways, std::vector<std::string> user_input)
{
    if(!(input_size_ok(user_input, 2)))
        std::cout << "Error: Invalid input." << std::endl;

    else if (tramways.find(user_input.at(1)) != tramways.end())
        std::cout << "Error: Stop/line already exists." << std::endl;

    else
    {
        tramways[user_input.at(1)];
        std::cout << "Line was added." << std::endl;
    }
}
// Checks if the distance is already in the line.
bool dist_in_line(const Tramway_type tramways, std::string line, std::string dist)
{
    for (auto stop : tramways.at(line))
    {
        if (stod(dist) == stop.second)
        {
            std::cout << "Error: Stop/line already exists." << std::endl;
            return true;
        }
    }
   return false;
}
// Adds a stop to the wanted line.
void add_stop(Tramway_type& tramways, std::vector<std::string> user_input)
{
    tramways.at(user_input.at(1))[user_input.at(2)] = stod(user_input.at(3));
    std::cout << "Stop was added." << std::endl;
}
// Removes the wanted stop from all the lines.
void remove_stop(Tramway_type& tramways, std::string stop)
{
    for (auto line : tramways)
    {
        if (line.second.find(stop) == line.second.end())
            continue;
        else
            tramways.at(line.first).erase(stop);
    }
    std::cout << "Stop was removed from all lines." << std::endl;
}

// The user interface and command hub of the program
bool UI(Tramway_type& tramways)
{
    while (true)
    {
        std::string user_input_str = "";
        std::cout << "tramway> ";
        std::getline(std::cin, user_input_str);

        std::vector<std::string> user_input;
        user_input = string_to_vector(user_input_str, ' ');

        cmd_word_toupper(user_input);

        if (user_input.at(0) == "QUIT")
            return true;

        else if (user_input.at(0) == "LINES")
            print_lines(tramways);

        else if (user_input.at(0) == "LINE")
        {
            if (input_not_ok(tramways, user_input, 2, true))
                continue;
            else
                print_line_stops(tramways, user_input.at(1));
        }

        else if (user_input.at(0) == "STOPS")
            print_stops(tramways);

        else if (user_input.at(0) == "STOP")
        {
            if (input_not_ok(tramways, user_input, 2, false))
                continue;
            else
                print_stop_in_lines(tramways, user_input.at(1));
        }
        else if (user_input.at(0) == "DISTANCE")
        {
            if (input_not_ok(tramways, user_input, 4, true))
                continue;
            else
                {
                if(!(stop_in_line(tramways, user_input.at(1), user_input.at(2), false))
                        or !(stop_in_line(tramways, user_input.at(1), user_input.at(3),false)))
                    continue;
                else
                    calc_distance(tramways, user_input.at(1), user_input.at(2), user_input.at(3));
                }
        }
        else if (user_input.at(0) == "ADDLINE")
        {
            add_line(tramways, user_input);
        }
        else if (user_input.at(0) == "ADDSTOP")
        {
            if (input_not_ok(tramways, user_input, 4, true))
                continue;
            if (!(stop_in_line(tramways, user_input.at(1), user_input.at(2), true)))
                continue;
            if (dist_in_line(tramways, user_input.at(1), user_input.at(3)))
                continue;
            add_stop(tramways, user_input);
        }

        else if (user_input.at(0) == "REMOVE")
        {
            if (input_not_ok(tramways, user_input, 2, false))
                continue;
            else
                remove_stop(tramways, user_input.at(1));
        }
        else
            std::cout << "Error: Invalid input." << std::endl;
    }
}

// Short and sweet main.
int main()
{
    print_rasse();

    Tramway_type tramways;

    std::string input_file_name = "";
    std::cout << "Give a name for input file: ";
    std::getline(std::cin, input_file_name);

    std::ifstream input_file(input_file_name);

    if (not input_file)
    {
        std::cout << "Error: File could not be read." << std::endl;
        return EXIT_FAILURE;
    }

    bool file_read_succesful = read_file(tramways, input_file);
    if (not file_read_succesful)
        return EXIT_FAILURE;

    input_file.close();

    bool quit = UI(tramways);
    if (quit)
        return EXIT_SUCCESS;
    else
        return EXIT_FAILURE;
}
