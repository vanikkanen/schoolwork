#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
   cout << "Input file: ";
   string input_file_name = "";
   getline(cin, input_file_name);

   cout << "Output file: ";
   string output_file_name = "";
   getline(cin, output_file_name);

   ifstream input_file(input_file_name);

   if (not input_file) {
       cout << "Error! The file " << input_file_name << " cannot be opened." << endl;
       return EXIT_FAILURE;

   } else {
       ofstream output_file(output_file_name);
       char line_nro = '1';
       string line;
       string new_line;

       while (getline(input_file, line)) {

           new_line = " " + line;
           new_line = line_nro + new_line;

           output_file << new_line << endl;

           new_line = "";
           ++line_nro;
       } input_file.close();
   }
}
