'''
COMP.SC.100 # 21 tulitikun lastenpeli. Pelaajat vuorotellen poistavat tulitikkuja, se joka poistaa viimeisen häviää.
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def main():

    print('Game of sticks')

    # Asetetaan tulitikkujen alkuarvoksi 21
    sticks = 21

    # Kun tulitikkuja on vielä jäljellä pelataan peliä
    while sticks > 0:
        # Ensin on pelaajan 1 vuoro
        invalid_p1 = True
        while invalid_p1:
            # Pelaaja kertoo kuinka monta tikkua haluaa poistaa
            p1 = int(input('Player 1 enter how many sticks to remove: '))
            # Jos poistettavien tikkujen määrä on 1,2 tai 3 mennään eteenpäin
            if p1 == 1 or p1 == 2 or p1 == 3:
                # Lasketaan tikkujen uusi arvo
                sticks = sticks - p1
                # Jos tikut menevat 0 tai alle pysäytetään peli
                if sticks <= 0:
                    print('Player 1 lost the game!')
                    break
                # Jos tikut eivät loppuneet printataan jäljellä oleva määrä ja poistutaan pelaajan 1 loopista
                print('There are', sticks, 'sticks left')
                invalid_p1 = False
            # Jos tikkuja yritetään poistaa laiton määrä printataan virhe viesti
            else:
                print('Must remove between 1-3 sticks!')

        # Jos tikut loppuvat halutaan myös ulos tästä loopista
        if sticks <= 0:
            break

        # Pelaajan 2 vuoro toimii samanlaillala kuin pelaajan 1
        invalid_p2 = True
        while invalid_p2:
            p2 = int(input('Player 2 enter how many sticks to remove: '))
            if p2 == 1 or p2 == 2 or p2 == 3:
                sticks = sticks - p2
                if sticks <= 0:
                    print('Player 2 lost the game!')
                    break
                print('There are', sticks, 'sticks left')
                invalid_p2 = False
            else:
                print('Must remove between 1-3 sticks!')

        if sticks <= 0:
            break
if __name__ == "__main__":
    main()
