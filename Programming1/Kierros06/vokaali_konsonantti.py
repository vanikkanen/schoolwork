'''
COMP.SC.100 # Laskee konsonattien ja vokaalien määrän sanassa
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    word = input("Enter a word: ")
    vowels_in_word = 0

    for character in word:
        vowels = 'a', 'e', 'i', 'o', 'u', 'y', 'ö', 'ä', 'å'
        if character in vowels:
            vowels_in_word += 1

    consonants_in_word = len(word) - vowels_in_word

    print(f'The word {word} contains {vowels_in_word} vowels and {consonants_in_word} consonants')

if __name__ == "__main__":
    main()
