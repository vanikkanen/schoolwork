'''
COMP.SC.100 Kysytään ostosten hinta, millä rahalla maksetaan ja minkälaisia vaihtorahoja pitää antaa
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    price_input = input('Purchase price: ') # Kysytään ostosten hintaa
    price = int(price_input)

    paid_input = input('Paid amount of money: ') # Kysystään maksettua määrää
    paid = int(paid_input)

    change1 = (paid - price)
    tens = change1 // 10    # Selvitetään kymmenet eurot
    change2 = change1 - tens * 10
    fives = change2 // 5    # Selvitetään vitoset
    change3 = change2 - fives * 5
    twos = change3 // 2     # Selvitetään kakkoset
    change4 = change3 - twos * 2
    ones = change4          # Selvitetään ykköset

    if tens > 0 or fives > 0 or twos > 0 or ones > 0:
        print('Offer change:')

        if tens > 0:       # Tarkistetaan onko jotain annettavaa
            print(tens,"ten-euro notes")
        if fives > 0:
            print(fives,'five-euro notes')
        if twos > 0:
            print(twos,'two-euro coins')
        if os > 0:ne
            print(ones,'one-euro coins')

    else:
        print('No change')  # Jos ei tule vaihtorahaa tulostetaan tämä

if __name__ == "__main__":
    main()
