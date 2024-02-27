'''
COMP.SC.100 # Käydään läpi lista ja tulostetaan siitä kaikki luvut jotka > 0
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    list_of_numbers = []

    print('Give 5 numbers:')

    for number in range(0,5):
        new_number = int(input("Next number: "))
        list_of_numbers.append(new_number)

    print("The numbers you entered that were greater than zero were:")

    for digit in list_of_numbers:
        if digit > 0:
            print(digit)

if __name__ == "__main__":
    main()
