'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''



def main():

    wanted_year = int(input('Which year would you like? '))
    weekday = input('Mon/Tue/Wed/Thu/Fri/Sat/Sun: ')

    counter = 0
    leap_counter = 4

    if wanted_year <= 2020:

        for year in range(2020, 1800, -1):

            for month in range(12, 0, -1):

                if month == 2:
                    days_in_month = 28
                    if leap_counter == 4:
                        days_in_month = 29
                        leap_counter = 0
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    days_in_month = 31
                else:
                    days_in_month = 30

                for day in range(days_in_month , 0, -1):
                    if day == 25 and month == 12 and year == 2020 and weekday == 'Fri' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year ,sep="")
                    elif day == 30 and month == 12 and year == 2020 and weekday == 'Wed' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 31 and month == 12 and year == 2020 and weekday == 'Thu' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 26 and month == 12 and year == 2020 and weekday == 'Sat' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 27 and month == 12 and year == 2020 and weekday == 'Sun' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 28 and month == 12 and year == 2020 and weekday == 'Mon' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 29 and month == 12 and year == 2020 and weekday == 'Tue' :
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif counter == 7:
                        if wanted_year == year:
                            print(day, '.', month, '.', year ,sep="")
                        counter = 0
                    counter += 1
            leap_counter += 1

    elif wanted_year > 2020:

        for year in range(2020, 2050):

            for month in range(1, 13):

                if month == 2:
                    days_in_month = 28
                    if leap_counter == 4:
                        days_in_month = 29
                        leap_counter = 1
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    days_in_month = 31
                else:
                    days_in_month = 30


                for day in range(1, days_in_month + 1):
                    if day == 3 and month == 1 and year == 2020 and weekday == 'Fri':
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 1 and month == 1 and year == 2020 and weekday == 'Wed':
                         counter = 0
                         if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 2 and month == 1 and year == 2020 and weekday == 'Thu':
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 4 and month == 1 and year == 2020 and weekday == 'Sat':
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 5 and month == 1 and year == 2020 and weekday == 'Sun':
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 6 and month == 1 and year == 2020 and weekday == 'Mon':
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif day == 7 and month == 1 and year == 2020 and weekday == 'Tue':
                        counter = 0
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                    elif counter == 7:
                        if wanted_year == year:
                            print(day, '.', month, '.', year, sep="")
                        counter = 0
                    counter += 1
            leap_counter += 1

if __name__ == "__main__":
    main()