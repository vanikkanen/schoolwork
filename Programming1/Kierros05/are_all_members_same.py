'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def are_all_members_same(list):
    """
    Tutkii ovatko listan kaikki alkiot samoja
    :param list: list, tutkittava lista
    :return: bool, palauttaa True jos alkiot ovat samoja ja False jos eivät
    """

    if list == []:
        return True

    else:
        compare_list = len(list)*[list[0]]
        return compare_list == list