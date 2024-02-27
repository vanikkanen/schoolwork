'''
COMP.SC.100 # Vertaillaan liukulukuja toisiinsa funktion avulla
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

EPSILON = 0.000000001

def compare_floats(num_1, num_2, EPSILON):
    """
    Vertailee liukulukuja toisiinsa ja palauttaa bool-arvon
    :return:
    """
    return abs(num_1 - num_2) < EPSILON

def main():

    num_1 = float(input('Input first number: '))
    num_2 = float(input('Input second number: '))

    answer = compare_floats(num_1, num_2, EPSILON)
    print(answer)
if __name__ == "__main__":
    main()
