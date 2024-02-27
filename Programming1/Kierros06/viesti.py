"""
COMP.CS.100 Programming 1
Code Template
"""

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

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for row in msg:
        print(row.upper())

if __name__ == "__main__":
    main()
