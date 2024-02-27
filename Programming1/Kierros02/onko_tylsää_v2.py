'''
COMP.SC.100 # Kysyy käyttäjältä vastausta kunnes se on oikea.
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    user_input = input("Answer Y or N: ")

    wrong_answer = True

    while wrong_answer:

        if user_input =='y' or user_input == 'Y' or user_input == 'n' or user_input == 'N':
            print("You answered", user_input)
            wrong_answer = False

        else:
            print("Incorrect entry.")
            user_input = input("Please retry: ")




if __name__ == "__main__":
    main()
