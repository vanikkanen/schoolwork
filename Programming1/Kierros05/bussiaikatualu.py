'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    depart = [630, 1015, 1415, 1620, 1720, 2000]

    time = int(input("Enter the time (as an integer): "))


    departures = len(depart)

    for times in range(0, departures):

        if depart[times] >= time:
            bus = times
            break
        elif time > 2000:
            bus = 0
            break

    print("The next buses leave:")

    three_buses = 3

    while three_buses > 0:

        print(depart[bus])
        bus = bus + 1
        three_buses = three_buses - 1
        if bus > 5:
            bus = 0

if __name__ == "__main__":
    main()
