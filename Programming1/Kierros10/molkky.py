"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


class Player:
    """
    This class defines a player and methods for keeping track of
    and scoring for them in a game of mölkky
    """

    def __init__(self, name):
        """
        Initializes a new player
        :param name: str, name of the player
        """

        self.__name = name
        self.__score = 0
        self.__throws = 0
        self.__throw_scores = 0
        self.__bad_throws = 0

    def get_name(self):
        """
        Returns the name of the player whose turn it is
        :return: str, name of player
        """
        return self.__name

    def add_points(self, new_points):
        """
        Adds points to the players score
        :param new_points: int, points to be added
        """

        self.__score += new_points
        self.__throw_scores += new_points
        self.__throws += 1

        if new_points == 0:
            self.__bad_throws += 1

        if 40 < self.__score <= 49:
            print(self.__name, "needs only", 50 - self.__score, "points. "
            "It's better to avoid knocking down the pins with higher points.")

        elif self.__score > 50:
            self.__score = 25
            print(f"{self.__name} gets penalty points!")

    def get_points(self):
        """
        Returns the score of the player
        :return: int, score of the player
        """

        return self.__score

    def has_won(self):
        """
        Checks if the player has won by getting their score to even 50
        :return: bool, return true if the player won else returns false
        """
        if self.__score == 50:
            return True
        else:
            return False

    def average(self):
        """
        Returns the average of the players throws
        :return: float, average score of the players throw
        """
        average = self.__throw_scores / self.__throws

        return average

    def hit_ratio(self):
        """
        Calculates the hit percentage of the player
        :return: float, returns the hit percentage
        """
        if self.__throws == 0:
            hit_ratio = 0

        else:
            throws = self.__throws
            hitting_throws = self.__throws - self.__bad_throws
            hit_ratio = (hitting_throws / throws) * 100

        return hit_ratio


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if pts > in_turn.average():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,",
              f"hit percentage {player1.hit_ratio():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p,",
              f"hit percentage {player2.hit_ratio():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
