'''
COMP.SC.100 Kivi, sakset, paperi -peli v2.0
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():
    p1_input = input("Player 1, enter your choice (R/P/S): ")

    p2_input = input("Player 2, enter your choice (R/P/S): ")


    if p1_input == p2_input:
        print("It's a tie!")
    elif p1_input == "R" and p2_input == "S" or p1_input == "P" and p2_input == "R" or p1_input == "S" and p2_input == "P":
        print('Player 1 won!')
    else:
        print('Player 2 won!')


if __name__ == "__main__":
    main()
