'''
COMP.SC.100 # Tulostaa kertotaulun kunnes arvo ylittää 100
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    user_input = int(input("Choose a number: "))

    multiplier = 1

    while (multiplier*user_input) < 100:

        print(multiplier, '*' ,user_input, '=' ,(multiplier*user_input))

        multiplier += 1

    print(multiplier, '*' ,user_input, '=' ,(multiplier*user_input))

if __name__ == "__main__":
    main()
