#include <iostream>
#include <string>
#include <fstream>
#include <map>

using namespace std;

void split(string str, string& name, int& points){

    string::size_type str_length = str.size();
    string::size_type i = 0;

    string points_to_be = "";

    char c;

    for (i = 0; i < str_length; ++i) {
        c = str.at(i);
        if (c == ':')
            continue;
        else if (isdigit(c))
            points_to_be += c;
        else
            name += c;
    }
    points = stoi(points_to_be);
}

int main()
{
    cout << "Input file: ";
    string input_file_name = "";
    getline(cin, input_file_name);

    ifstream input_file(input_file_name);
    if (not input_file){
        cout << "Error! The file " << input_file_name << " cannot be opened." << endl;
        return EXIT_FAILURE;
    } else {
        map<string, int> scores;
        string line = "";
        string name = "";
        int points = 0;
        while (getline(input_file, line)){
            name = "";
            points = 0;
            split(line, name, points);

            if (scores.find(name) != scores.end())
                scores.at(name) += points;
            else
                scores.insert({name, points});
        } cout << "Final scores:" << endl;
        for (auto data : scores){
            cout << data.first << ": " << data.second << endl;
        }

    }

}
