'''
COMP.SC.100 # Tulostaa halutun kokoisen ruudun halutulla merkillä
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def print_box(W, H, M):
    """Tulostaa halutun kokoisen ruudun halutulla merkillä"""
    for line in range(0, H):
        print(W * M)

def main():

    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
