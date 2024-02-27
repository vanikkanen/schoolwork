'''
COMP.SC.100 # Laskee kohdetiedostosta henkilöiden psitemäärät ja tulostaa
ne aakkosjärjestyksessä yhteenlaskettuna
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    filename = input("Enter the name of the score file: ")
    scores = {}

    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    file_lines = file.readlines()

    for file_line in sorted(file_lines):

        line = file_line.rstrip().split(" ")

        try:
            if line[0] in scores:
                scores[line[0]] += int(line[1])
            else:
                scores[line[0]] = int(line[1])

        except ValueError:
            print("There was an erroneous score in the file:")
            print(str(line[1]))
            return

        except IndexError:
            print("There was an erroneous line in the file:")
            print(str(line[0]))
            return

    print("Contestant score:")
    for player in sorted(scores):
        print(player, scores[player])

if __name__ == "__main__":
    main()
