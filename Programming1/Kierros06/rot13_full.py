'''
COMP.SC.100 # Muuttaa koko viestin rot13 salatuksi
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def read_message():
    """
    Adds the users text lines into a list and returns the list when the user
    inputs an empty line
    :return: list, Contains the text rows that the user wrote
    """
    message = []

    while True:
        new_row = input()

        if new_row == "":
            return message

        else:
            message.append(new_row)

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text in regular_chars or text.lower() in regular_chars:

        if text in regular_chars:
            index = regular_chars.index(text)
            return encrypted_chars[index]

        elif text.lower() in regular_chars:
            text = text.lower()
            index = regular_chars.index(text)
            return encrypted_chars[index].upper()

    else:
        return text

def row_encryption(text):
    """
    Enrypts the whole string by calling another function
    :param text: str, string to be encrypted
    :return: str, returns the encrypted string
    """
    encrypted = ""

    for index in range(0, len(text)):
        char = text[index]

        encrypted += encrypt(char)

    return encrypted

def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for row in msg:
        print(row_encryption(row))

if __name__ == "__main__":
    main()
