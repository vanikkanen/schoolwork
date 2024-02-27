#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main()
{
    string encryption_key = "";
    cout << "Enter the encryption key: ";
    cin >> encryption_key;
    int length = encryption_key.length();

    if ( length != 26 ) {
        cout << "Error! The encryption key must contain 26 characters." << endl;
        return 1;
    }

    for ( int i = 0; i < length; ++i) {
        int c = encryption_key[i];
        if (isupper(c)){
            cout << "Error! The encryption key must contain only lower case characters." << endl;
            return 1;
        }
    }
    string::size_type in_text = 0;
    for( char letter = 'a'; letter < 'z'; ++letter ) {
        in_text = encryption_key.find(letter);
        if ( in_text == string::npos) {
            cout << "Error! The encryption key must contain all alphabets a-z." << endl;
            return 1;
        }
    }

    string text = "";
    cout << "Enter the text to be encrypted: ";
    cin >> text;
    int text_length = text.length();

    for ( int i = 0; i < text_length; ++i) {
        int c = text[i];
        if (isupper(c)){
            cout << "Error! The encryption key must contain only lower case characters." << endl;
            return 1;
        }
    }
    string encrypted_text = "";

    for ( int i = 0; i < text_length; ++i) {
        int c = text[i];
        int place_in_key = c - 97;
        encrypted_text += encryption_key[place_in_key];

    }
    cout << "Encrypted text: " <<encrypted_text << endl;
}
