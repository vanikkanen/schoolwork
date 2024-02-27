'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    not_bored = True # Lippumuuttuja 1

    while not_bored:
        user_input = input('Bored? (y/n) ') # Kysytään onko käyttäjällä tylsää, jos ei toistetaan kunnes on

        if user_input != 'y' or user_input != 'n' or user_input != 'Y' or user_input != 'N':  # Jos vastaus on vääränlainen mennään tähän silmukkaan
            wrong_answer = True # Lippumuuttuja 2

            while wrong_answer:

                    if user_input == 'y' or user_input == 'Y' or user_input == 'n' or user_input == 'N': # Jos annetaan oikeanlainen vastaus mennään ulos tästä silmukasta
                        wrong_answer = False

                    else:
                        print("Incorrect entry.")
                        user_input = input("Please retry: ")

        if user_input == 'y' or user_input == 'Y': # Jos on tylsää lopetetaan silmukka
            print("Well, let's stop this, then.")
            not_bored = False

if __name__ == "__main__":
    main()
