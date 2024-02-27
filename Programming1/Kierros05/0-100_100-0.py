'''
COMP.SC.100 # Tulostaa lukusarjan 0-100 ja sitten 100-0
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    for number in range(0, 100+1, 2):
        print(number)
        number + 2
    for number in range(100, -1, -2):
        print(number)
        number + 2

if __name__ == "__main__":
    main()
