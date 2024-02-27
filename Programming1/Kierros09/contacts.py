'''
COMP.SC.100 # Funktio joka lukee yhteystietoja tiedostosta
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def read_file(filename):
    """
    Makes a dictionary off of the contacts in the given file
    :param filename: str, name of the file to be used
    :return: dict, returns a dictionary of the contacts in the given file
    """
    file = open(filename, mode='r')
    dict = {}

    for row in file:
        data = row.rstrip().split(";")
        dict[data[0]] = {'name': data[1], 'phone': data[2], 'email': data[3],
        'skype': data[4]}

    return dict