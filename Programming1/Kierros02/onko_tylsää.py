'''
COMP.SC.100 # Kysyy käyttäjältä onko tylsää, kunnes on tylsää.
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    not_bored = True # Lippumuuttuja

    while not_bored:
        user_input = input('Bored? (y/n) ') # Kysytään okno käyytäjällä tylsää, jos ei toistetaan kunnes on

        if user_input == 'y': # Jos on tylsää lopetetaan silmukka
            print("Well, let's stop this, then.")
            not_bored = False

if __name__ == "__main__":
    main()
