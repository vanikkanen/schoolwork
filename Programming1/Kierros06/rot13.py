"""
COMP.CS.100 Programming 1
ROT13 program code template
"""

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

    to_encrypt = input('To encrypt: ')

    print(row_encryption(to_encrypt))


if __name__ == "__main__":
        main()