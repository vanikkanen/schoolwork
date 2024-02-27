'''
COMP.SC.100 # Zip boing peli, jossa 3 jaolliset ovat zip ja 7 jaolliset boing
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    how_far = int(input("How many numbers would you like to have? "))

    variable = 1

    while variable <= how_far:

        if (variable // 3 and (variable % 3) == 0) and (variable // 7 and (variable % 7) == 0):
            print('zip boing')

        elif variable // 3 and (variable % 3) == 0:
            print('zip')

        elif variable // 7 and (variable % 7) == 0:
            print('boing')

        else:
            print(variable)

        variable += 1

if __name__ == "__main__":
    main()
