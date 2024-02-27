'''
COMP.SC.100 # Kirjoittaa tiedostoon numeroituja rivejä tekstiä
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

def main():

    filename = input("Enter the name of the file: ")
    line_number = 1

    try:
        file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    lines = read_message()

    for line in lines:
        line = line.rstrip()
        print(line_number, line, file=file)
        line_number += 1

    file.close()

    print(f"File {filename} has been written.")

if __name__ == "__main__":
    main()
