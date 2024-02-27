'''
COMP.SC.100 # Ristinolla -peli
Tekijä: Valtteri Nikkanen, Atte Harmoinen
Opiskelijanumero: 282688, 284930
Sähköposti: valtteri.nikkanen@tuni.fi, atte.harmoinen@tuni.fi

Koodin tehtävä:

Ohjelma tekee aluksi menu ikkunan josta voi valita millaisen pelin haluaa
pelata. Valittavana on paras yhdestä, paras kolmesta, paras viidestä ja
vapaapeli muoto jolla voi pelata niin kauan kuin haluaa. Menu ikkunassa on
myös nappi jolla ohjelman voi sulkea. Kun jokin pelimuoto valitaan sulkeutuu
menu ikkuna ja peli ikkuna aukeaa. Peli ikkunassa on loopilla valmistetut napit
joilla itse ristinollaa pelataan. Peli ikkunassa on myös sen oikealla puolella
kirjanpidollisia komponentteja jotka päivittyvät pelin edetessä. Kun peli
päättyy joko voittoon tai tasapeliin menee sekuntti ja sitten peli lauta
palautuu alkutilaan mutta kirjanpito jää ennalleen. Kun koko matsi (eli paras
x määrästä pelejä) päättyy joko voittoon jommallekummalle pelaajalle tai
tasapeliin peli ikkuna ilmoittaa tuloksen ja taas menee hetki ennen kuin peli
ikkuna sulkeutuu ja menu ikkuna avautuu. Peli ikkunassa on myös nappi menuun ja
koko ohjelman sulkemiseen.

Työllä pyrittiin kehittyneeseen versioon projektista.
'''

from tkinter import *
from math import inf

# Global variables are a list of the possible winning sets and a dictionary to
# determine a squares "name" by its coordinates

WIN_COMB = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
            {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
            {1, 5, 9}, {3, 5, 7}
            ]
SQUARES = {0: {0: 1, 1: 2, 2: 3}, 1: {0: 4, 1: 5, 2: 6}, 2: {0: 7, 1: 8, 2: 9}}


class Main_menu:
    """
    Creates the main menu window.
    """
    def __init__(self):
        """
        Initializes the required components for the window.
        """
        # --------------------------------------------------------------------
        # Creating the window itself and assigning some parameters

        # like size for it. We also add an icon photo for the window
        self.__menu_mainw = Tk()
        self.__menu_mainw.title("Main Menu")
        self.__menu_mainw.geometry("250x400")
        self.__menu_mainw.resizable(False, False)
        self.__menu_mainw.iconphoto(False, PhotoImage(file="icon.png"))

        # We make a background image for the main menu window and place it
        # in the window. We make the background image with a label
        self.__bg_image = PhotoImage(file="background.png")
        self.__bg_label = Label(self.__menu_mainw, image=self.__bg_image)
        self.__bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Now we add some other components to the window. We first make
        # the title label for the window.
        self.__title = Label(self.__menu_mainw, text="TicTacToe",
                             font=("Comic Sans MS", 30))
        self.__title.pack()

        # --------------------------------------------------------------------
        # Making the menubutton

        # Then we make a menubutton for choosing the desired game mode
        self.__new_game_menu = Menubutton(self.__menu_mainw, text="New Game",
                                          font=("Comic Sans MS", 15))
        self.__new_game_menu.pack(pady=100)

        # We make the menu for the menubutton
        self.__new_game_menu.menu = Menu(self.__new_game_menu, tearoff=0)
        self.__new_game_menu["menu"] = self.__new_game_menu.menu

        # Now we add some options or game modes to the menu we created
        self.__new_game_menu.menu.add_command(label="Best of 1",
                                              command=lambda: self.play(1),
                                              font=("Comic Sans MS", 13))
        self.__new_game_menu.menu.add_command(label="Best of 3",
                                              command=lambda: self.play(3),
                                              font=("Comic Sans MS", 13))
        self.__new_game_menu.menu.add_command(label="Best of 5",
                                              command=lambda: self.play(5),
                                              font=("Comic Sans MS", 13))
        self.__new_game_menu.menu.add_command(label="Freeplay",
                                              command=lambda: self.play(inf),
                                              font=("Comic Sans MS", 13))

        # --------------------------------------------------------------------
        # Creating the other button and starting the mainloop

        # Quit button for the menu window
        self.__quit_button = Button(self.__menu_mainw, text="Quit",
                                    command=self.quit,
                                    font=("Comic Sans MS", 10))
        self.__quit_button.pack(side=BOTTOM, padx=(220, 0))

        self.__menu_mainw.mainloop()

    def play(self, games_to_play):
        """
        Destroys the menu window and calls the game window class and gives
        it the maximum number of games to play
        :param games_to_play: int, how many games we want to play at most
        """

        self.__menu_mainw.destroy()
        TicTacToe(games_to_play)

    def quit(self):
        """
        Destroys the menu window and closes the program
        """
        self.__menu_mainw.destroy()


class TicTacToe:
    """
    Creates the game window for tictactoe
    """
    def __init__(self, games_to_play):
        """
        Initializes the required components for the window.
        :param games_to_play: int, maximum number of games to play
        """
        # --------------------------------------------------------------------
        # Making the game window itself and giving it some parameters

        self.__game_mainw = Tk()
        self.__game_mainw.title("TicTacToe")
        self.__game_mainw.iconphoto(False, PhotoImage(file="icon.png"))
        self.__game_mainw.resizable(False, False)

        # --------------------------------------------------------------------
        # Creating some empty lists and variables for the game

        self.__x_score = 0
        self.__O_score = 0
        self.__games_to_play = games_to_play
        self.__games = 0
        self.__winningtext = Label(self.__game_mainw,
                                   font=("Comic Sans MS", 20))
        self.__winningtext.grid(row=3, column=0, columnspan=3, sticky=E + W)
        self.__turn_limit = 0
        self.__turn = 0
        self.__player1 = []
        self.__player2 = []
        self.__buttons = []

        # --------------------------------------------------------------------
        # Creating and saving images for the game board

        self.__empty_image = PhotoImage(height=86, width=86)
        self.__images = []
        for image in ["X.png", "O.png"]:
            new_image = PhotoImage(file=image)
            self.__images.append(new_image)

        # --------------------------------------------------------------------
        # Creating and placing the labels for scores and such in the game board

        self.__x_label = Label(self.__game_mainw, text=self.__x_score,
                               font=("Comic Sans MS", 20))
        self.__x_label.grid(row=1, column=4, sticky=W, padx=(40, 0))
        self.__O_label = Label(self.__game_mainw, text=self.__O_score,
                               font=("Comic Sans MS", 20))
        self.__O_label.grid(row=1, column=4, sticky=E, padx=(0, 40))
        self.__games_played = Label(self.__game_mainw, text=self.__games,
                                    font=("Comic Sans MS", 20))
        self.__games_played.grid(row=2, column=4, sticky=S, pady=(0, 10))

        score = Label(self.__game_mainw, text="Scores",
                      font=("Comic Sans MS", 20))
        score.grid(row=0, column=4, sticky="N")
        dash = Label(self.__game_mainw, text="-", font=("Comic Sans MS", 20))
        dash.grid(row=1, column=4)
        games_title = Label(self.__game_mainw, text="Games played",
                            font=("Comic Sans MS", 20))
        games_title.grid(row=2, column=4, sticky=N)
        vs_title = Label(self.__game_mainw, text="X vs O",
                         font=("Comic Sans MS", 20))
        vs_title.grid(row=0, column=4, sticky=S)

        # --------------------------------------------------------------------
        # Creating and placing the menu and quit buttons for the game board

        self.__mainmenu_button = Button(self.__game_mainw, text="Main Menu",
                                        command=self.main_menu,
                                        font=("Comic Sans MS", 10))
        self.__mainmenu_button.grid(row=3, column=4, padx=(20, 0), sticky=S)

        self.__quit_button = Button(self.__game_mainw, text="Quit",
                                    command=self.quit,
                                    font=("Comic Sans MS", 10))
        self.__quit_button.grid(row=3, column=4, sticky=E + S)

        # --------------------------------------------------------------------
        # Starting a new game and running the mainloop

        self.new_game()
        self.__game_mainw.mainloop()

    def change_button(self, x, y):
        """
        Changes the button and calls for other methods to determine if the
        player has won the game
        :param x: int, x-coordinate for the button that has been pressed
        :param y: int, y-coordinate for the button that has been pressed
        """

        # Firstly we save the button that was pressed into the "clicked_button"
        # and advance the turn by 1
        clicked_button = self.__buttons[x][y]
        self.__turn += 1

        # Then we check which players turn it is and change the button to the
        # corresponding image and save the buttons coordinates to the player
        if self.__turn % 2:
            clicked_button.configure(image=self.__images[0], state=DISABLED)
            self.__player1.append([x, y])

        else:
            clicked_button.configure(image=self.__images[1], state=DISABLED)
            self.__player2.append([x, y])

        # Then we call a function to determine if the game is over
        self.is_over()

        # Lastly we check if the turn limit has been reached and the game was
        # a tie
        if self.__turn >= self.__turn_limit:
            self.game_over()

    def is_over(self):
        """
        Checks if the game has been won by either of the players
        """
        # We only need to check if either of the players has already chosen 3
        # or more squares
        if len(self.__player1) >= 3 or len(self.__player2) >= 3:

            # First we create an empty set into which we save the players
            # squares
            picked_squares = set([])
            player1 = False
            player2 = False

            # Then we check which players turn it is and save the squares in
            # their list into the set we created in the correct format
            # Or we take the correct square number from the global SQUARES by
            # the squares coordinates
            if self.__turn % 2:
                for square in self.__player1:
                    x, y = square[0], square[1]
                    picked_squares.add(SQUARES[x][y])
                    player1 = True
            else:
                for square in self.__player2:
                    x, y = square[0], square[1]
                    picked_squares.add(SQUARES[x][y])
                    player2 = True

            # Then we check if any of the winning combinations in the players
            # chosen squares
            for comb in WIN_COMB:

                # If a winning combination is found we add 1 to the players
                # score and call another method to determine what to do next
                if comb.issubset(picked_squares):

                    if player1:
                        self.__x_score += 1
                        self.__x_label.configure(text=self.__x_score)

                    elif player2:
                        self.__O_score += 1
                        self.__O_label.configure(text=self.__O_score)

                    self.game_over()

    def game_over(self):
        """
        Determines what to do after the game is over
        """
        # First we update some statistics and disable the mainmenu button for
        # a short while for error control reasons
        self.__games_to_play -= 1
        self.__games += 1
        self.__games_played.configure(text=self.__games)
        self.__mainmenu_button.configure(state=DISABLED)

        # Then we disable the TicTacToe buttons for error control reasons
        for row in self.__buttons:
            for button in row:
                button.configure(state=DISABLED)

        # If the match is over we tell the players who has won and call the
        # main menu method after a short period
        if self.__games_to_play == 0 or self.__x_score > self.__games_to_play\
                + self.__O_score or self.__O_score > self.__games_to_play +\
                self.__x_score:

            if self.__x_score > self.__O_score:
                self.__winningtext.configure(text="X wins the match!")

            elif self.__O_score > self.__x_score:
                self.__winningtext.configure(text="O wins the match!")

            else:
                self.__winningtext.configure(text="It's a tie!")

            self.__game_mainw.after(2500, self.main_menu)

        # If the match isn't over we call the new game method to start a
        # new game after a short period
        else:

            self.__game_mainw.after(1000, self.new_game)

    def new_game(self):
        """
        Starts a new game with a clean board
        """
        # First we determine whose turn it is to start the game and set the
        # turn limit by that
        if self.__games % 2:
            self.__turn = 1
        else:
            self.__turn = 0

        self.__turn_limit = self.__turn + 9

        # We clear the players if there is something there
        self.__player1 = []
        self.__player2 = []
        self.__buttons = []

        # We create a correct size list to save the tictactoe squares to
        for row in range(0, 3):
            self.__buttons.append([None] * 3)

        # Now we create the tictactoe squares in a loop and save the into the
        # list and to the correct place in the window
        for y in range(0, 3):
            for x in range(0, 3):

                def button_press(button_y=y, button_x=x):
                    self.change_button(button_x, button_y)

                new_button = Button(self.__game_mainw,
                                    activebackground="light gray",
                                    image=self.__empty_image,
                                    command=button_press)

                self.__buttons[x][y] = new_button

                new_button.grid(row=x, column=y)

        # After this we set the mainmenu button to the normal state again
        self.__mainmenu_button.configure(state=NORMAL)

        return

    def main_menu(self):
        """
        Takes the user back into the main menu window and closes the game
        window
        """
        self.__game_mainw.destroy()
        Main_menu()

    def quit(self):
        """
        Closes the window and the program
        """
        self.__game_mainw.destroy()


def main():

    Main_menu()


if __name__ == "__main__":
    main()
