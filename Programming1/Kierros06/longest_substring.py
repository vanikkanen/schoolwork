'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


def longest_substring_in_order(string):
    """
    Ottaa selville pisimmän aakosjärjestyksessä olevan merkkijonon annetussa
    merkkijonossa
    :param string: str, Käsiteltävä nerkkijono
    :return: str, pisimmän akkosjärjestyksessä olevan pätkän annetusta merkkijonosta
    """
    if string == "":
        return string

    else:
        longest_substring = string[0]

        for index in range(0,len(string) - 1):

            a = 0
            b = 1

            while string[index + a] < string[index + b]:

                a = b
                b += 1

                if index + b == len(string):
                    break

            substring = string[index:index + b]

            if len(substring) > len(longest_substring):
                longest_substring = substring

    return longest_substring