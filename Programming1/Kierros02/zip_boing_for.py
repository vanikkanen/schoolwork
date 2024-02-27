'''
COMP.SC.100 # Zip boing peli for-loopilla
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    how_far = int(input("How many numbers would you like to have? "))

    for number in range (1 , (how_far + 1)):

        if (number // 3 and (number % 3) == 0) and (number // 7 and (number % 7) == 0):
            print('zip boing')

        elif number // 3 and (number % 3) == 0:
            print("zip")

        elif number // 7 and (number % 7) == 0:
            print("boing")

        else:
            print(number)



if __name__ == "__main__":
    main()
