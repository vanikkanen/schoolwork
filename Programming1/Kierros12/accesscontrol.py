"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Project: accesscontrol, program template
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name
        """

        # Luodaan oliolle tunnus ja nimi
        self.__id = id
        self.__name = name
        # Luodaan oliolle tyhjä lista mihin tallennetaan pääsykoodit
        self.__access = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        """

        # Luodaan merkkijono millä tulostetaan myöhemmin kaikki olion
        # pääsykoodit
        access_string = ""
        for code in sorted(self.__access):
            if access_string == "":
                access_string = code
            else:
                access_string += f", {code}"

        # Tulostetaan olion tiedot halutussa formaatissa
        print(f"{self.__id}, {self.__name}, access: {access_string}")

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

        return self.__name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.
        """

        # Tarkistetaan onko oliolla jo ko. pääsykoodi
        if new_access_code not in self.__access:

            # Tarkisteaan onko uusi pääsykoodi ovikoodi jos kyllä niin
            # tarkistetaan check.access -metodilla onko oliolla jo pääsy
            # kyseiseen oveen, jos ei niin lisätään pääsykoodi oliolle
            if new_access_code in DOORCODES:
                if not self.check_access(new_access_code):
                    self.__access.append(new_access_code)

            # Jos pääsykoodi ei ollut ovikoodi niin se on kulkualuekoodi.
            # Tarkistetaan mihin oviin kulkualuekoodilla päästään ja
            # poistetaan ne oliolta. Try-except rakenne pitää huolen siitä
            # että mahdolliset muut aluekulkukoodit eivät haittaa. Lopuksi
            # lisätään aluekoodi oliolle
            else:
                for code in self.__access:
                    try:
                        if new_access_code in DOORCODES[code]:
                            self.__access.remove(code)
                    except KeyError:
                        pass

                self.__access.append(new_access_code)
        else:
            return

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        """

        # Käydään läpi olion kulkukoodit.
        for accesscode in self.__access:
            # Tarkistetaan onko koodi suoraan ovikoodina oliolla
            if door == accesscode:
                return True
            # Tarkisteaan kattaako jokin kulkualuekoodi ko. oven.
            elif accesscode not in DOORCODES:
                if accesscode in DOORCODES[door]:
                    return True
        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added
         to this card.
        """

        for code in card.__access:
            self.add_access(code)


def check_accesscode(code):
    """
    Checks if the accesscode is in either the DOORCODES dict or in the values
    of the DOORCODES dict.

    :param code: str, accesscode to be checked
    :return: bool, True if either in dict or in values of dict, false if not in
    """

    if code in DOORCODES:
        return True
    else:
        for accesscodes in DOORCODES.values():
            if code in accesscodes:
                return True
        return False


def main():
    # Luodaan tyhjä sanakirja mihin tallennetaan kulkukortit
    dict_of_cards = {}

    # Avataan ja luetaan tiedosto missä on halutut tiedot.
    try:
        filename = "accessinfo.txt"
        input_file = open(filename, mode="r")

        # Käydään tiedosto rivi kerrallaan läpi ja luodaan niiden perusteella
        # olioita, joille tallennetaan oikeat kulkukoodit. Tallennetaan oliot
        # tunnusta avaimena käyttäen luotuun sanakirjaan
        for row in input_file:
            id, name, access_codes = row.split(";")
            access_card = Accesscard(id, name)
            for code in access_codes.rstrip().split(","):
                access_card.add_access(code)
            dict_of_cards[id] = access_card

        input_file.close()

    # Jos jokin virhe tiedoston lukemisessa, niin lopetetaan suorittaminen
    except FileNotFoundError or ValueError:
        print("Error: file cannot be read.")
        return

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:

            # Tulostetaan kaikki kulkukorttien tiedot sanakirjasta
            # info -metodin avulla
            for card_id in sorted(dict_of_cards):
                dict_of_cards[card_id].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]

            # Tarkistetaan onko tunnus sanakirjassa, jos on niin tulostetaan
            # olion tiedot info -metodilla muuten tulostetaan error viesti
            if card_id in dict_of_cards:
                dict_of_cards[card_id].info()
            else:
                print("Error: unknown id.")

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            # Tarkistetaan tunnuksen ja ovikoodin olemassa olo
            if card_id not in dict_of_cards:
                print("Error: unknown id.")
            elif door_id not in DOORCODES:
                print("Error: unknown doorcode.")

            # Tarkistetaan onko oliolla oveen sopivaa kulkulupaa
            else:
                is_it_in = dict_of_cards[card_id].check_access(door_id)
                # Jos on printataan tämä
                if is_it_in:
                    print(f"Card {card_id}"
                          f" ( {dict_of_cards[card_id].get_name()} )"
                          f" has access to door {door_id}")
                # Jos ei niin tämä
                else:
                    print(
                        f"Card {card_id}"
                        f" ( {dict_of_cards[card_id].get_name()} )"
                        f" has no access to door {door_id}")

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]

            # Tarkistetaan onko tunnusta tai kulkukoodia olemassa
            if card_id not in dict_of_cards:
                print("Error: unknown id.")
            elif not check_accesscode(access_code):
                print("Error: unknown accesscode.")

            # Jos ei virheitä niin lisätään oliolle kulkukoodi
            else:
                dict_of_cards[card_id].add_access(access_code)

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]

            # Tarkistetaan ovatko molemmat oliot olemassa
            if card_id_to not in dict_of_cards or \
                    card_id_from not in dict_of_cards:

                print("Error: unknown id.")

            else:
                dict_of_cards[card_id_to].merge(dict_of_cards[card_id_from])

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
