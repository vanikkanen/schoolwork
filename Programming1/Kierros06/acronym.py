'''
COMP.SC.100 # Tekee akronyymin annetusta fraasista
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def create_an_acronym(string):
    """
    Muodostaa akronyymin annetusta merkkijonosta
    :param string: str, merkkijono josta aakronyymi halutaan muodostaa
    :return: str, palauttaa halutun akronyymin
    """
    words = string.split(' ')
    letters = []

    for word in words:

        mod_word = word.strip().upper()
        letter = mod_word[0]
        letters.append(letter)

    acronym = "".join(letters)
    return acronym