'''
COMP.SC.100 # Funktio joka kääntää annetut nimet
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def reverse_name(names):
    """
    Kääntää annetut nimet toisinpäin ja poistaa ylimääräiset välimerkit
    :param names: str, merkkijono jossa halutut nimet
    :return: str, merkkijono jossa nimet oikeinpäin tai muu haluttu data
    """

    if names != "":

        name = names.split(",")

        name_1 = name[1].strip()
        name_0 = name[0].strip()

        fullname = name_1 + " " + name_0

        if name_1 != "" and name_0 != "":

            return fullname

        elif name_1 == "" or name_0 == "":

            return (name_1 + name_0)

    else:

        return ""
