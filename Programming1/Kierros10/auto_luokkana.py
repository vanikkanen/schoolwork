"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for a simplified car assignment
implementation using a class.
"""


class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0
        self.__odometer = 0

    def print_information(self):
        """
        Prints out the current information about the car
        """
        print(f"The tank contains {self.__gas:.1f} liters of gas and the"
              f" odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, to_fill):
        """
        Fills out the cars gas tank with the requested ammount of gas
        :param to_fill: float, the ammount of gas to be filled into the car
        :return:
        """

        if to_fill < 0:
            print("You cannot remove gas from the tank")

        elif self.__tank_volume <= to_fill + self.__gas:
            self.__gas = self.__tank_volume

        else:
            self.__gas += to_fill

    def drive(self, distance):
        """
        Moves the car for the requested distance. Calculates the gas
        consumption.
        :param distance: float, the distance to travel with the car
        """

        if distance < 0:
            print("You cannot travel a negative distance")

        gas_per_km = self.__consumption / 100
        distance_in_tank = self.__gas / gas_per_km

        if distance <= distance_in_tank:
            self.__odometer += distance
            self.__gas -= gas_per_km * distance

        elif distance > distance_in_tank:
            self.__odometer += distance_in_tank
            self.__gas = 0


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")

            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")

            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
