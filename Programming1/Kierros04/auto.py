'''
COMP.SC.100 # Autolla ajo "simu"
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''

from math import sqrt

def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(size, to_fill, current):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """

    if to_fill + current > size:
        return size

    else:
        new_ammount = current + to_fill
        return new_ammount

def drive(x, y, new_x, new_y, gas, consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    # It might be useful to make one or two assisting functions
    # to help the implementation of this function.

    to_travel = distance(x, y, new_x, new_y)
    gas_in_km = gas_for_km(gas, consumption)

    if to_travel <= gas_in_km:
        gas_leftover = gas_left(to_travel, gas, consumption)
        return gas_leftover, new_x, new_y
    else:
        delta_x = (gas_in_km/to_travel) * (new_x - x)
        delta_y = (gas_in_km/to_travel) * (new_y - y)
        new_new_x = delta_x + x
        new_new_y = delta_y + y
        return 0.0, new_new_x, new_new_y

def distance(x, y, new_x, new_y):
    """
    Calculates the new coordinates
    :param x: float, old x coordinate
    :param y:  float, old y coordinate
    :param new_x:  float, new x coordinate
    :param new_y:  float, new y coordinate
    :return:
    """
    travel_x = (abs(new_x - x))
    travel_y = (abs(new_y - y))

    distance = sqrt((travel_x ** 2) + (travel_y ** 2))
    return distance

def gas_left(distance, gas, consumption):
    """
    Calculates the gas in the tank
    :param distance:
    :param gas:
    :param consumption:
    :return:
    """

    new_gas = gas - (distance * (consumption/100))
    return new_gas

def gas_for_km(gas, consumption):
    """
    Calculates the consumed gas
    :param gas: float, ammount of gas in tank
    :param consumption: float, how much tha car consumes per 100km
    :param distance: float, the travelled distance
    :return:
    """
    consumption_per_km = consumption / 100
    gas_for_km = gas / consumption_per_km

    return gas_for_km

def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)

def main():

    menu()

if __name__ == "__main__":
    main()
