'''
COMP.SC.100 # Tulostaa energiatilaston histogrammina
              syötetyistä energian-arvoista
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

def input_values():
    """
    Kasaa ja palauttaa listan annetuista arvoista. Tarkastaa samalla että
    arvot ovat positiivisia kuten kuuluukin.
    :return: list, Palauttaa listan int muotoisia ja positiivisia arvoja.
    """
    # Asetetaan lippumuuttuja todeksi
    inputting = True
    # Tehdään tyhjä lista johon sitten kerätään käyttäjän syötteet
    list = []

    while inputting:

        new_data = (input("Enter energy consumption (kWh): "))
        # Kun käyttäjä syöttää tyhjän rivin palautetaan kasattu lista
        if new_data == '':
            return list
        # Jos käyttäjän syöte on jotian muuta kuin tyhjää tarkastellaan sitä.
        # Jos syöte on vähemmän kuin nolla printataan virhe viesti ja muuten
        # lisätään se listaan
        else:
            if int(new_data) <= 0:
                print(f"You entered: {new_data}. Enter non-negative numbers only!")
            else:
                list.append(int(new_data))

def process_data(user_input):
    """
    Käy läpi käyttäjän listan alkioittain ja jakaa kulutusluokittain
    uuteen listaan

    :param user_input: list, Käyttäjän syötteistä koottu int arvoja sisältävä
                             lista

    :return: list, Funktion kasaama kulutusluokkien määrän sisältävä lista
    """
    # Lasketaan kuinka monta eri kulutusluokkaa tarvitaan
    no_of_class = number_of_class(user_input)

    # Tehdään lista jossa on riittävästi tilaa kaikille arvoille
    list_by_class = [0] * no_of_class

    # Loopilla käydään läpi kaikki käyttäjän syöttämät arvot, löydetään
    # niille oikea kulutusluokka ja lisätään sen kulutusluokan arvoa tehdyssä
    # listassa mihin käyttäjän syöttämä arvo kuuluu
    for value in user_input:
        class_value = 1
        index = 0
        not_in_class = True

        while not_in_class:

            class_min = class_min_value(class_value)
            class_max = class_max_value(class_value)

            if class_min <= value and value <= class_max:

                list_by_class[index] = list_by_class[index] + 1
                not_in_class = False

            else:
                class_value += 1
                index += 1

    # Palautetaan lista missä kaikki arvot on jaettu oikeisiin kulutusluokkiin
    return list_by_class

def number_of_class(list):
    """
    Laskee kulutusluokkien määrän arvioimalla sen käyttäjän suurimman antaman
    perusteella
    :param list: list, Lista joka sisältää käyttäjän syöttämät arvot
    :return: int, Palauttaa suurimman kulutusluokan arvon
    """
    # Tarkastetaan suurin arvo käyttäjän syötteistä
    max_value = max(list)
    class_value = 1
    # Loopilla lasketaan mihin kulutusluokkaan suurin arvo kuuluu
    while True:

        class_min = int(class_min_value(class_value))
        class_max = int(class_max_value(class_value))

        if class_min <= max_value and max_value < class_max:
            # Palautetaan suurimman arvon kulutusluokan arvo
            return class_value

        class_value += 1

def print_histogram(data_list):
    """
    Käy läpi kaikki arvot listassa ja lähettää ne toiselle funktiolle
    printattavaksi
    :param data_list: list, Lista joka pitää sisällään int tyyppisiä arvoja
                     jotka kertovat kuinka plajon mitäkin kulutusarvoa on
    """
    # Asetetaan listan indeksin arvoksi nolla
    index = 0

    for data in data_list:

        # Kulutusluokan arvo on indeksin arvo + 1, sillä lista alkaa nollasta
        # mutta kulutusluokat yhdestä
        class_number = index + 1

        # Printattavien merkkien määrä on listasta indeksin paikalta löytyvä
        # arvo
        count = data

        # Suurin kulutusluokka on listan pituus
        largest_class_number = len(data_list)

        # Lähetetään tarvittavat tiedot toiselle funktiolle printattavksi
        print_single_histogram_line(class_number, count, largest_class_number)

        # Kasvatetaan indeksiä yhdellä
        index += 1

def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Tämä on luultavasti projektin haastavin funktio, joten tässä se on
    valmiina.  Funktio tulostaa oikean muotoisen histogrammin rivin,
    kuhan kutsut sitä oikeilla parametrien arvoilla.

    :param class_number: int,
        Mitä kulutuskatergoriaa tulostettava rivi kuvaa (1, 2, 3, ...)
        Parametria <class_number> käytetään päättämään, mikä arvoväli
        (0-9, 10-99, 100-999, ...) riville tulostuu ennen diagrammin
        "*"-merkkejä.

    :param count: int,
        Kuinka monta "*"-merkkiä riville on tarpeen tulostaa, eli
        kuinka monta käyttäjän syöttämää arvoa kuuluu <class_number>-
        parametrin kuvaamalle välillä.

    :param largest_class_number: int,
        Mikä on kaikkein suurin kategorian numero.  Riippuu
        suurimmasta käyttäjän syöttämästä kulutusarvosta.
        Esimerkiksi jos suurin käyttäjän syöttämä luku
        oli 91827364 (8 numeromerkkiä) <largest_class_number>-parametrin
        arvon tulisi myös olla 8.  Parametrin arvoa käytetään
        määriteltäessä, kuinka monta välilyöntiä muiden kuin viimeisen
        histogrammin rivin eteen pitäisi tulostaa.
    """

    # <range_string>-muuttujaan talletetaan merkijonona rivin
    # histogrammissa kuvaama arvoväli. Esimerkiksi "1000-9999".
    # Apufunktiot class_minimum_value ja class_maximum_value
    # sinun on määriteltävä itse.

    min_value = class_min_value(class_number)
    max_value = class_max_value(class_number)
    range_string = f"{min_value}-{max_value}"


    # Kun histogrammin viimeinen rivi tulostetaa, kuinka monta
    # merkkiä leveä tulee <range_string> silloin olemaan.
    # Jos esimerkiksi <largest_class_number> on 7, tarkoittaisi
    # se, että arvoväliksi tulostetaan "1000000-9999999" eli
    # muuttujaan <largest_width> pitää tallentaa arvo 15.
    # Kaikkien arvovälien <range_string> tulostetaan tämän
    # levyisen kentän oikeaan laitaan.

    largest_width = 2 * largest_class_number + 1


    # Kaikki valmistelun on tehty, voidaan tulostaa rivi,
    # jonka alussa on oikea määrä välilyöntejä, niiden perässä
    # arvoväli ja lopulta oikea määrä "*"-merkkejä.
    # Merkki ">" seuraavassa f""-merkkijonossa tulostaa
    # <range_string>:in arvon tulostuskentän oikeaan laitaan
    # (täytevälilyönnit tulostetaan alkuun).

    print(f"{range_string:>{largest_width}}: {'*' * count}")

def class_min_value(class_number):
    """
    Laskee arvovälin pienimmän arvon
    :param class_number: int, Kulutusluokan järjestysnumero
    :return: int, Halutun kulutusluokan minimiarvo
    """
    # Lasketaan kulutusluokan minimin arvo alla olevalla kaavalla
    min_value = int(10 ** class_number // 100 * 10)

    # Palautetaan kulutusluokan minimiarvo
    return min_value

def class_max_value(class_number):
    """
     Laskee arvovälin suurimman arvon
    :param class_number: int, Kulutusluokan järjestysnumero
    :return: int, Halutun kulutusluokan maksimiarvo
    """
    # Lasketaan kulutusluokan maksimin arvo alla olevalla kaavalla
    max_value = int(10 ** class_number - 1)

    # Palautetaan kulutusluokan maksimiarvo
    return max_value

def main():

    # Printataan alkutekstit
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()


    # Käyttäjä syöttää halaumansa arvot
    input_data = input_values()

    # Jos käyttäjä palauttaa tyhjän listan printataan viesti
    if input_data == []:
        print('Nothing to print. Done.')
    # Jos lista ei ole tyhjä jatkojalostetaan käyttäjän syöttämiä arvoja
    else:
        # Prosessoidaan käyttäjän arvot missä ne on jaoteltu kulutusluokkiin
        processed_data = process_data(input_data)
        # Printataan kulutusluokat sisältävästä listasta haluttu histogrammi
        print_histogram(processed_data)


if __name__ == "__main__":
    main()