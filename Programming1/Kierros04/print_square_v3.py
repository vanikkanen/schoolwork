'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Prints a box
    :param height: int, height of the box
    :param width: int, width of the box
    :param inner_mark: string, mark for the boxes outer layer
    :param border_mark: string, mark for the boxes inner layers
    :return:
    """

    for rivi in range(1,height+1):
        if rivi == 1 or rivi == height:
            print(width * border_mark)
        else:
            print(f'{border_mark}{(width - 2 ) * inner_mark}{border_mark}')
    print()

def main():

    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()
