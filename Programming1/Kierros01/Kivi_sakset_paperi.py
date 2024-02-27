'''
COMP.SC.100 Kivi, sakset, paperi -peli
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    p1_input = input("Player 1, enter your choice (R/P/S): ")

    p2_input = input("Player 2, enter your choice (R/P/S): ")

    if p1_input == "R":
        if p2_input == "S":
            print('Player 1 won!')
        elif p2_input == "P":
            print('Player 2 won!')
        elif p2_input == "R":
            print("It's a tie!")

    elif p1_input == "P":
        if p2_input == "R":
            print('Player 1 won!')
        elif p2_input == "S":
            print('Player 2 won!')
        elif p2_input == "P":
            print("It's a tie!")

    elif p1_input == "S":
        if p2_input == "P":
            print('Player 1 won!')
        elif p2_input == "R":
            print('Player 2 won!')
        elif p2_input == "S":
            print("It's a tie!")



if __name__ == "__main__":
    main()
