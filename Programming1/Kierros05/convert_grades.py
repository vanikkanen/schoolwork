'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def convert_grades(grades):
    """
    Muuttaa eri arvosanan kuin nolla numeroksi 6
    :param grades: list, pitää sisällään kaikki arvosanat
    :return:
    """

    index = len(grades)

    for index in range(0, index):
        if grades[index] > 0:
            grades[index] = 6



def main():

    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
