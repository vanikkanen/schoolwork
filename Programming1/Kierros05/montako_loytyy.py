'''
COMP.SC.100 # Käsittelee listaa halutulla tavalla
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def input_to_list(how_many):
    """
    Saa tiedon kuinka monta lukua halutaan listaan ja tekee
    kyseisen listan halutuista alkioista
    :param how_many: int, kuinka monta alkiota listaan halutaan
    :return:
    """

    list = []

    print(f"Enter {how_many} numbers:")

    for number in range(0,how_many):
        new_number = (int(input()))
        list.append(new_number)
    return list

def main():


    how_many = int(input("How many numbers do you want to process: "))

    list = input_to_list(how_many)

    to_search = int(input("Enter the number to be searched: "))

    in_list = list.count(to_search)

    if in_list > 0:
        print(f"{to_search} shows up {in_list} times among the numbers you have entered.")
    else:
        print(f"{to_search} is not among the numbers you have entered.")

if __name__ == "__main__":
    main()
