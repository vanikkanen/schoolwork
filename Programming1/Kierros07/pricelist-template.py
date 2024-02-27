"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 282688
Name: Valtteri Nikkanen
Email: valtteri.nikkanen@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    do_loop = True

    while do_loop:

        user_input = input("Enter product name: ")
        user_input = user_input.strip()

        if user_input == "":
            print("Bye!")
            break

        else:
            if user_input in PRICES:
                print(f"The price of {user_input} is {PRICES[user_input]:0.2f} e")
            else:
                print(f"Error: {user_input} is unknown.")


if __name__ == "__main__":
    main()
