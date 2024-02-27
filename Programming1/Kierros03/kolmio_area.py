'''
COMP.SC.100 # Laskee kolmion pinta-alan annettujen sivujen pituuksien perusteella
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

from math import sqrt

def area(a, b, c):
    """
    Laskee kolmion pinta-alan
    :param a: float: Kolmion a sivu
    :param b: float: Kolmion b sivu
    :param c: float: Kolmion c sivu
    :return: float: Palauttaa lasketun pinta-alan
    """
    s = (a + b + c)/2
    A = sqrt(s * (s - a) * (s - b) * (s - c))
    return A

def main():

    line_a = float(input("Enter the length of the first side: "))
    line_b = float(input("Enter the length of the second side: "))
    line_c = float(input("Enter the length of the third side: "))

    calc_area = area(line_a, line_b, line_c)

    print(f"The triangle's area is {calc_area:.1f}")

if __name__ == "__main__":
    main()
