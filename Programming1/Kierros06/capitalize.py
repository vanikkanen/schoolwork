'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def capitalize_initial_letters(string):
    """
    Käytetään metodia capitalize laittamaan merkkijonon sanojen ensimmäiset
    kirjaimet isoiksi kirjaimiksi ja loput pieniksi
    :param string: str, käsiteltävä merkkijono
    :return:    str, Palauttaa halutun muotoisen merkkijonon
    """

    new_words = []
    words = string.split(" ")

    for word in words:
        new_words.append(word.capitalize())

    new_string = " ".join(new_words)
    return new_string
