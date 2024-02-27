"""
COMP.CS.100 Programming 1
Code template for geometric shapes.
"""

import math

def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            square_input()
            # dealing with square.

        elif answer == "r":
            rectangle_input()
            # dealing with a rectangle

        elif answer == "c":
            circle_input()
            # dealing with a circle

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability

def rectangle_input():
    """
    This function asks and checks your rectangles side lenghts
    :return:
    """
    side1_negative = True
    side2_negative = True

    while side1_negative:
        side_1 = float(input("Enter the length of the rectangle's side 1: "))
        if side_1 > 0:
            break

    while side2_negative:
        side_2 = float(input("Enter the length of the rectangle's side 2: "))
        if side_2 > 0:
            break

    rectangle_circ = rectangle_c(side_1, side_2)
    rectangle_area = rectangle_a(side_1, side_2)

    print(f'The total circumference is {rectangle_circ:.2f}')
    print(f'The surface area is {rectangle_area:.2f}')

def square_input():
    """
    This function asks and checks your squares sides length
    :return:
    """

    side_negative = True

    while side_negative:
        side = float(input("Enter the length of the square's side: "))
        if side > 0:
            break

    square_area = square_a(side)
    square_circ = square_c(side)

    print(f'The total circumference is {square_circ:.2f}')
    print(f'The surface area is {square_area:.2f}')

def circle_input():
    """
    This function asks and checks the radius of your circle
    :return:
    """

    radius_negative = True

    while radius_negative:
        radius = float(input("Enter the circle's radius: "))
        if radius > 0:
            break

    circle_area = circle_a(radius)
    circle_circ = circle_c(radius)

    print(f'The total circumference is {circle_circ:.2f}')
    print(f'The surface area is {circle_area:.2f}')

def rectangle_a(side1, side2):

    """
    This function calculates the area of a rectangle
    :param side1: float, the lenght of the rectangles side 1
    :param side2: float, the lenght of the rectangles side 2
    :return:
    """

    area = side1 * side2
    return area

def rectangle_c(side1, side2):

    """
    This function calculates the cirumference of a rectangle
    :param side_1: float, the lenght of the rectangles side 1
    :param side_2: float, the lenght of the rectangles side 2
    :return:
    """

    circumference = 2*side1 + 2*side2
    return circumference

def square_a(side):
    """
    This function calculates the area of a square
    :param side: float, the lenght of the squares side
    :return:
    """

    area = side ** 2
    return area

def square_c(side):
    """
    This function calculates the circumference of a square
    :param side: float, the lenght of the squares side
    :return:
    """

    circumference = side * 4
    return circumference

def circle_a(radius):
    """
    This function calculates the area of a circle
    :param radius: float, lenght of the radius
    :return:
    """

    area = math.pi * (radius ** 2)
    return area

def circle_c(radius):
    """
    This function calculates the circumference of a circle
    :param radius: float, lenght of the radius
    :return:
    """

    circumference = 2 * math.pi * radius
    return circumference

def main():

    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
