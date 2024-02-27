'''
COMP.SC.100 # Koodin tehtävä tähän
Tekijä: Valtteri Nikkanen
Opiskelijanumero: 282688
'''


from tkinter import *

def main():

    window = Tk()

    menub = Menubutton(window, text="New Game")
    menub.pack()

    menub.menu = Menu(menub, tearoff=0)
    menub["menu"] = menub.menu

    menub.menu.add_command(label="Button 1")


    window.mainloop()

if __name__ == "__main__":
    main()
