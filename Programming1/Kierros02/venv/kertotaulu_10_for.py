'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    user_input = int(input("Choose a number: "))

    for number in range(1,11):
        print(user_input * number)


if __name__ == "__main__":
    main()
