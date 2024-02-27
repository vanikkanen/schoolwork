'''
COMP.SC.100 # Laskee kuinka paljon potilaalle saa antaa parasetamolia
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def calculate_dose(weight, time, total_doze_24):
    """Laskee parasetamoli annostuksen annettujen arvojen perusteella"""
    doze = weight * 15
    if time < 6:
        doze = 0
        return doze
    elif total_doze_24 + doze >= 4000:
        new_doze = 4000 - total_doze_24
        return new_doze
    else:
        return doze


def main():

    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))

    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, time, total_doze_24)}")

if __name__ == "__main__":
    main()
