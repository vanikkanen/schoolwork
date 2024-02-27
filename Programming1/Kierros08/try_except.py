'''
COMP.SC.100 # Prints a box
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def read_input(insert):
    """
    Checks that the input is an integer
    :param insert: str, The question for which we want the answer to
    :return: int, Returns the wanted integer
    """
    while True:
        try:
            user_input = int(input(insert))
            break
        except ValueError:
            pass

    return user_input

def print_box(W, H, M):
    """
    Prints the right size box with the right mark
    :param W: int, Width of the box
    :param H: int, Height of the box
    :param M: str, The mark with what the box is printed
    """
    for line in range(0, H):
        print(W * M)

def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)

if __name__ == "__main__":
    main()
