"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""
def dict_contents(dict):
    """
    Tulostaa dictionaryn sisällön merkkijonona
    :param dict: dict, tulostettavaksi haluttu sanakirja
    :return:
    """
    print("Dictionary contents:")
    print(", ".join(sorted(dict)))

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    dict_contents(english_spanish)
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")

            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ")
            spa_word = input("Give the word to be added in Spanish: ")

            english_spanish[eng_word] = spa_word
            dict_contents(english_spanish)

        elif command == "R":
            del_word = input("Give the word to be removed: ")
            if del_word not in english_spanish:
                print("The word", del_word, "could not be found from the dictionary.")
            else:
                del english_spanish[del_word]

        elif command == "P":
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()
            print("Spanish-English")
            for word in sorted(english_spanish.values()):
                for eng_word in english_spanish:
                    if word == english_spanish[eng_word]:
                        print(word, eng_word)
                        break
            print()

        elif command == "T":

            translated = ""
            to_translate = input("Enter the text to be translated into Spanish: ")
            words = to_translate.split(" ")

            for element in words:
                if element in english_spanish:
                    translated += english_spanish[element] + " "
                else:
                    translated += element + " "
            print("The text, translated by the dictionary:")
            print(translated.rstrip())

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
