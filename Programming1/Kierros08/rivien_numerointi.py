'''
COMP.SC.100 # Lukee tiedoston, tulostaa sen sisällön ja numeroi sen rivit
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    filename = input("Enter the name of the file: ")
    line_number = 1

    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    for file_line in file:

        file_line = file_line.rstrip()

        print(f"{line_number} {file_line}")
        line_number += 1

    file.close()
if __name__ == "__main__":
    main()
