'''
COMP.SC.100 # Tasaa syötetyn tekstin halutun mittaiseksi
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
        new_row = input().replace("  ", " ")
        if new_row == "":
            return message
        else:
            message.append(new_row)

def to_words(text):
    """
    Converts the users input to list that contains the words in the lists
    elements
    :param text: list, the text that the user input
    :return: list, return a list that contains the words in the users text
    """
    text_in_words = []

    for row in text:

        words = row.split(" ")

        for word in words:
            text_in_words.append(word)

    return text_in_words

def print_text(text, chars_per_row):
    """
    Prints the users text in the correct format
    :param text: list, contains the text in words in a list
    :param chars_per_row: int, how many characters the user wanted per row
    :return:
    """
    row = ""
    final_text = []

    for word in text:

        if row == "":
            row += word

        elif len(row) + len(word) + 1 <= chars_per_row:
            row += " " + word

        else:
            spaces = row.count(" ")
            missing_chars = chars_per_row - len(row)

            if spaces > 0:
                full_spaces = missing_chars//spaces
                partial_spaces = missing_chars % spaces

                row = row.replace(" ", " " * (full_spaces + 1))
                row = row.replace(" " * (full_spaces + 1), " " * (full_spaces + 2), partial_spaces)

            final_text.append(row)

            row = word

    final_text.append(row)

    for rows in final_text:
        print(rows)

def main():

    print('Enter text rows. Quit by entering an empty row.')
    user_text = read_message()

    text = to_words(user_text)
    char_per_line = int(input('Enter the number of characters per line: '))

    print_text(text, char_per_line)

if __name__ == "__main__":
    main()
