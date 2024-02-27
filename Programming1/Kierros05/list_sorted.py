'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def is_the_list_in_order(list):
    """
    tarkastelee onko annettu lista suuruusjärjestyksessä
    :param list: list, tarkasteltava lista
    :return: bool, jos lista on suuruusjärjestyksessä True, jos ei, False
    """
    sorted_list = sorted(list)

    return sorted_list == list