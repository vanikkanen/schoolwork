#include <iostream>
#include <string>
#include <fstream>
#include <map>


using namespace std;

void split_and_add(const string line, const int line_nro, map<string, string>& words){

    string::size_type str_length = line.size();
    string::size_type i = 0;

    char c;
    string word = "";

    for (i = 0; i < str_length; ++i){
        c = line.at(i);
        if (c == ' '){
           if (words.find(word) != words.end()){
               if (words.at(word).find(to_string(line_nro)) != string::npos)
                   word = "";
               else {
                   words.at(word) += ", " + to_string(line_nro);
                   word = "";
               }
           } else {
               words.emplace(word, to_string(line_nro));
               word = "";
           }

    } else
        word += c;
}
    if (words.find(word) != words.end()){
        if (words.at(word).find(to_string(line_nro)) != string::npos)
            word = "";
        else {
            words.at(word) += ", " + to_string(line_nro);
            word = "";
        }
    } else {
        words.emplace(word, to_string(line_nro));
        word = "";
}
}
int main()
{
    cout << "Input file: ";
    string input_file_name = "";
    getline(cin, input_file_name);

    ifstream input_file(input_file_name);

    if (not input_file) {
        cout << "Error! The file " << input_file_name << " cannot be opened." << endl;
        return EXIT_FAILURE;

    } else {
        map<string, string> words;
        string line = "";
        int line_nro = 1;
        while (getline(input_file, line)){
            split_and_add(line, line_nro, words);
            ++line_nro;
        }
            string lines = "";
            for (auto data : words){
                int appearances = 0;
                cout << data.first << " ";
                string::size_type line_length = data.second.size();
                string::size_type index = 0;

                for (index = 0; index < line_length; ++index){
                    char c = data.second.at(index);
                    if (isdigit(c))
                        ++appearances;
                }
                cout << appearances << ": " << data.second << endl;
            }






    } input_file.close();
}

