"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""


class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    def __init__(self, name, hitpoints):
        """
        Initializes the object, requires a name for the object
        :param name: str, name of the object
        """
        self._name = name
        self._hitpoints = hitpoints
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
        if self._inventory[item] <= 0:
            del self._inventory[item]

    def printout(self):
        """
        Prints out the objects information
        """
        print("Name:", self._name)
        print("Hitpoints:", self._hitpoints)
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

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """
        if item in self._inventory:
            self.remove_item(item)
            target.give_item(item)
        else:
            return

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """
        if weapon not in WEAPONS:
            print(f'Attack fails: unknown weapon "{weapon}".')
            return
        if weapon not in self._inventory:
            print(f"Attack fails: {self._name} doesn't have", f'"{weapon}".')
            return
        if target is self:
            print(f"Attack fails: {self._name} can't attack him/herself.")
            return

        target._hitpoints -= WEAPONS[weapon]
        print(f'{self._name} attacks {target.get_name()} delivering'
              f' {WEAPONS[weapon]} damage.')
        if target._hitpoints <= 0:
            print(f"{self._name} successfully defeats"
                  f" {target.get_name()}.")


WEAPONS = {
    # Weapon          Damage
    # --------------   ------
    "elephant gun": 15,
    "gun": 5,
    "light saber": 50,
    "sword": 7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword")  # Conan doesn't have a sword.
    conan.attack(conan, "gun")  # A character is not allowed to attack himself.
    conan.attack(conan, "pen")  # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")  # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword")  # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")  # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
