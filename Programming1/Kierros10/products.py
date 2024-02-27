"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, initial_price):
        """
        A product object is initialized with the name and initial cost of the
        product in question
        :param name: str, name of the product in question
        :param initial_price: float, price of the product in question
        """

        self.__product_name = name
        self.__price = initial_price
        self.__sale_percentage = 0

    def printout(self):
        """
        Prints out the information about the product
        """
        print(self.__product_name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale_percentage:.2f}")

    def get_price(self):
        """
        Calculates the price of the product
        :return: float, returns the price of the product with the discount
        """
        price = self.__price * (1 - self.__sale_percentage/100)

        return price

    def set_sale_percentage(self, sale_percentage):
        """
        Sets the sale percentage to the requested ammount
        :param sale_percentage: float, the requested sale percentage
        """
        self.__sale_percentage = sale_percentage


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
