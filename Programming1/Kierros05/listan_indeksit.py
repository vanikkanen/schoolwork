'''
COMP.SC.100 # Tulostetaan listan sisältö päinvastaisessa järjestyksessä
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    list_of_numbers = []

    print('Give 5 numbers:')

    for number in range(0, 5):
        new_number = int(input("Next number: "))
        list_of_numbers.append(new_number)

    print("The numbers you entered, in reverse order:")

    for index in range(4, -1, -1):
        print(list_of_numbers[index])

if __name__ == "__main__":
    main()
