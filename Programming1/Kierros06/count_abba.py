'''
COMP.SC.100 # Laskee merkkijonojen "abba" lukumäärän merkkijonossa
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def count_abbas(string):
    """
    Counts the ammount of the string "abba" in the provided string
    :param string: str, teh string to be analyzed
    :return: int, returns the ammount of the string "abba" found
    """
    abbas = 0
    for index in range(0, len(string)):
        char = string[index]

        if char.lower() == 'a':
            if string[index:index + 4].lower() == 'abba':
                abbas += 1

    return abbas