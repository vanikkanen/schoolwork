'''
COMP.SC.100 # Funktio joka laskee kolmion kolmannen kulman
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def calculate_angle(a1, a2 = 90):
    """
    Laskee kolmion kolmannen kulman suuruuden
    :param a1: int, kolmion kulman suuruus
    :param a2: int, kolmion toisen kulman suuruus
    :return:
    """
    if a2 == 90:
        return 180 - a1 - 90

    else:
        return 180 - a1 - a2
