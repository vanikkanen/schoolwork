"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 282688
Name:       Valtteri Nikkanen
Email:      valtteri.nikkanen@tuni.fi

Body Mass Index
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_text = Label(self.__mainwindow, text="Weight in kg")
        self.__weight_value = Entry()

        self.__height_text = Label(self.__mainwindow, text="Height in meters")
        self.__height_value = Entry()

        self.__calculate_button = Button(self.__mainwindow,
                                         text="Calculate BMI",
                                         background="gray",
                                         command=self.calculate_BMI)

        self.__result_text = Label(self.__mainwindow, text="",
                                   borderwidth=2, relief=GROOVE)

        self.__explanation_text = Label(self.__mainwindow,
                                        text="",
                                        borderwidth=2, relief=GROOVE)

        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                    command=self.stop)

        self.__weight_text.grid(row=0, column=0)
        self.__height_text.grid(row=0, column=1)
        self.__weight_value.grid(row=1, column=0)
        self.__height_value.grid(row=1, column=1)
        self.__calculate_button.grid(row=2, column=0, columnspan=2)
        self.__stop_button.grid(row=5, column=1, sticky=E)
        self.__result_text.grid(row=3, column=0, columnspan=2, sticky=E+W)
        self.__explanation_text.grid(row=4, column=0, columnspan=2, sticky=E+W)

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())

            if weight <= 0 or height <= 0:
                self.__explanation_text.configure(
                    text="Error: height and weight"
                         " must be positive.")
                self.reset_fields()
                return

        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight"
                                                   " must be numbers.")
            self.reset_fields()

        else:
            self.reset_fields()

            bmi = float(weight)/float(height/100)**2
            self.__result_text.configure(text=f"{bmi:.2f}")

            if 18.5 <= bmi <= 25:
                self.__explanation_text.configure(
                    text="Your weight is normal.")
            elif bmi < 18.5:
                self.__explanation_text.configure(
                    text="You are underweight.")
            else:
                self.__explanation_text.configure(
                    text="You are overweight.")

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
