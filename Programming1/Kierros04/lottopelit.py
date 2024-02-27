'''
COMP.SC.100 # Kertoo todennäköisyyden voittaa lottopelissa yhdellä arvalla
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def factorial(num):
    """
    Laskee kertoman
    :param num: int, luku minkä kertoma lasketaan
    :return: int, palauttaa annetun luvun kertoman
    """
    factorial = 1

    if num == 0:
        return 1
    else:
        for i in range(1, 1+num):
            factorial = (factorial * i)
        return factorial

def check_input(input_total_balls,input_drawn_balls):
    """
    Tarkistaa pallojen määrän

    :param drawn_balls: int, arvottujen pallojen lukumäärä
    :param total_balls: int, kaikkien pallojen lukumäärä
    :return:
    """

    if input_total_balls < 0:
        print('The number of balls must be a positive number.')
    elif input_drawn_balls > input_total_balls:
        print('At most the total number of balls can be drawn.')
    else:
        return True

def chances(total_balls, drawn_balls):

    """
    Laskee vaihtoehtojen määrän
    :param total_balls: int, arvottujen pallojen lukumäärä
    :param drawn_balls: int, kaikkien pallojen lukumäärä
    :return: int, palauttaa mahdollisuuksien lukumäärän
    """
    n = factorial(total_balls)
    p = factorial(drawn_balls)
    y = factorial(total_balls - drawn_balls)

    return int(n/(y*p))

def main():

    total_balls = int(input('Enter the total number of lottery balls: '))
    drawn_balls = int(input('Enter the number of the drawn balls: '))

    input_ok = check_input(total_balls, drawn_balls)

    if input_ok:
        how_many = chances(total_balls, drawn_balls)
        print(f'The probability of guessing all {drawn_balls} balls correctly is 1/{how_many}',sep='')

if __name__ == "__main__":
    main()
