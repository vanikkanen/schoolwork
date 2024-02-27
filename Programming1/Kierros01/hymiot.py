'''
COMP.SC.100 Ehdotetaan käyttäjälle sopivaa hymiötä tämän mielialan pohjalta
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    user_input = input('How do you feel? (1-10) ' ) #Kysytään mielialaa

    mood_number = int(user_input)

    if mood_number <= 10 and mood_number >= 1: # Tarkistetaan että annettu arvo on sopiva
        if mood_number <= 7 and mood_number >= 4:
             print('A suitable smiley would be :-|') # 7 ja 4 välissä
        elif mood_number > 7 and mood_number < 10:
             print('A suitable smiley would be :-)') # Yli 7 ja alle 10
        elif mood_number < 4 and mood_number > 1:
            print('A suitable smiley would be :-(') # Alle 4 ja ja yli 1 välissä
        elif mood_number == 1:
            print("A suitable smiley would be :'(") # Annettu arvo on 1
        elif mood_number == 10:
            print('A suitable smiley would be :-D') # Annettu arvo on 10

    else:
        # Print error
        print('Bad input!')

if __name__ == "__main__":
    main()
