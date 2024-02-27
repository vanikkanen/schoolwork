'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():
    counter = 0
    for month in range(1, 13):

        if month == 2:
                days_in_month = 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                days_in_month = 31
        else:
                days_in_month = 30

        for day in range(1, days_in_month + 1):
            if day == 3 and month == 1:
                    counter = 0
                    print(day, '.', month, '.',sep="")
            elif counter == 7:
                    print(day, '.', month, '.',sep="")
                    counter = 0
            counter += 1

if __name__ == "__main__":
    main()
