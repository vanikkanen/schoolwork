'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    how_many = int(input('How many Fibonacci numbers do you want? '))

    f1 = 1
    f2 = 1

    print('1. 1')
    print('2. 1')

    for number in range(3, how_many + 1):

        fibonacci = f1 + f2
        print(f'{number}.',fibonacci)
        f2 = f1
        f1 = fibonacci

if __name__ == "__main__":
    main()
