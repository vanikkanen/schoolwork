"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 282688
Name: Valtteri Nikkanen
Email: valtteri.nikkanen@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():

    for entry in sorted(PRICES.values()):
        for product in PRICES:
            if entry == PRICES[product]:
                print(f"{product} {entry:0.2f}")


if __name__ == "__main__":
    main()
