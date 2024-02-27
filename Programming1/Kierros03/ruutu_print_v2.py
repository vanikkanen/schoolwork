'''
COMP.SC.100 # Printtaa halutun kokoisen ruudun halutulla merkillä ja tarkistaa että sillä on laillisia arvoja
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def read_input(insert):
    """Tarkastelee annetun syötteen laatua"""
    do_loop = True
    while do_loop:
        user_input = int(input(insert))
        if user_input > 0:
            return user_input

def print_box(W, H, M):
    """Tulostaa halutun kokoisen ruudun halutulla merkillä"""
    for line in range(0, H):
        print(W * M)

def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)

if __name__ == "__main__":
    main()
