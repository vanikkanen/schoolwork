"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:

    def __init__(self, name):
        """
        Initializes the object, requires a name for the object
        :param name: str, name of the object
        """
        self._name = name
        self._inventory = {}

    def give_item(self, item):
        """
        Adds an item to the objects inventory
        :param item: str, item to be added to the inventory
        """
        if item in self._inventory:
            self._inventory[item] += 1
        else:
            self._inventory[item] = 1

    def remove_item(self, item):
        """
        Removes an item from the objects inventory
        :param item: str, item to be removed
        :return:
        """
        self._inventory[item] -= 1

    def printout(self):
        """
        Prints out the objects information
        """
        print("Name:", self._name)
        if self._inventory == {}:
            print("  --nothing--")
        else:
            for item in sorted(self._inventory):
                if self._inventory[item] > 0:
                    print(" ", self._inventory[item], item)

    def get_name(self):
        """
        Returns the objects name
        :return: str, name of the object
        """
        return self._name

    def has_item(self, item):
        """
        Checks if an item is in the objects inventory
        :param item: str, item to be checked
        :return: bool, True if it is in inventory False otherwise
        """
        if item in self._inventory and self._inventory[item] > 0:
            return True
        else:
            return False

    def how_many(self, item):

        try:
            amount = self._inventory[item]
            return amount

        except KeyError:
            return 0

def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
