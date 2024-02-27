"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 282688
Name:       Valtteri Nikkanen
Email:      valtteri.nikkanen@tuni.fi

Code for counter program.
"""

from tkinter import *


class Counter:
    """
    Creates a interface that can count and reset itself
    """
    def __init__(self):

        self.__main_window = Tk()

        self.__counter = 0
        self.__current_value = Label(self.__main_window, text=self.__counter)
        self.__current_value.grid(row=0, column=1, columnspan=2)

        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        self.__increase_button = Button(self.__main_window, text="Increase",
                                        command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        self.__decrease_button = Button(self.__main_window, text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__main_window, text="Quit",
                                    command=self.quit)
        self.__quit_button.grid(row=1, column=3)

        self.__main_window.mainloop()

    def increase(self):
        """
        Deducts one from the counter in the interface
        """
        self.__counter += 1
        self.__current_value.configure(text=self.__counter)

    def decrease(self):
        """
        Adds one to the counter in the interface
        """
        self.__counter -= 1
        self.__current_value.configure(text=self.__counter)

    def reset(self):
        """
        Resets the counter in the interface to 0
        """
        self.__counter = 0
        self.__current_value.configure(text=self.__counter)

    def quit(self):
        """
        Destroys the interface and ends the program
        """
        self.__main_window.destroy()


def main():

    Counter()


if __name__ == "__main__":
    main()
