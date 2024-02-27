/* Class: GameWindow
 * ----------------
 * Represents the gameboard on what the gmae is played on. Also handles all the
 * logic in the game. Calls other classes as necesary.
 *
 * Writer of the program:
 * Name: Valtteri Nikkanen
 * Student number: 282688
 * User id's: nikkanev
 * E-mail: valtteri.nikkanen@tuni.fi
 *
 * COMP.CS.110 K2021
 *
This program is a memory game. The games objective is to fiind all the pairs of
cards on the board.

The program starts the user at the menu window where the user can choose how
many players and pairs of cards there will be in the game. The game will then
start with the given parameters when the start button is pressed. There is also
a close button that shuts the program down. Also in the menu is a text browser
that shows the results of the last 30 player scores. The players score is only
saved and showed if the player got more than 0 pairs in the game. There is a
maximum amount of 5 players and 26 pairs and minimum amount of 1 player and 2
pairs that the game can be ran with. Both of these can be affected with the
spinbox components.

When the start button is clicked a new window with the game components. Here
there are a grid of buttons representing the cards and player name boxes and
players card packs. There is also a button to return to the menu window and
to close the whole program. There is also a text label that tells whose turn it
is. If a pair is found the turn stays on the player who found the pair.

You can turn the card by clicking on it. Only 2 cards can be turned at a time.
After the second card is turned it is checked and then either turned or removed
from the board, depending if the turned cards were a pair or not. If the cards
turned were a pair the label is updated to show that a pair was found by what
player and the card is added to the players card pack. After this the cards are
removed from the board and turn kept on the player. After all the cards are
found the game announces the winner or winners if a tie. It saves the scores to
a file and returns to the menu window.

The player names can be updated at any time during the game but they start with
generic "PlayerX" names. After the name is updated it is updated on the label
if it is that players turn at the moment.
*/

#ifndef GAMEWINDOW_HH
#define GAMEWINDOW_HH

#include <QMainWindow>
#include <QPushButton>
#include "card.hh"
#include "player.hh"
#include <QLineEdit>
#include <QLabel>
#include <QGraphicsScene>

//All the card images in a neat vector where they can be accessed from
const std::vector<QString> CARD_IMAGES = {"images/2H.png", "images/3H.png",
                                          "images/4H.png", "images/5H.png",
                                          "images/6H.png", "images/7H.png",
                                          "images/8H.png", "images/9H.png",
                                          "images/10H.png", "images/JH.png",
                                          "images/QH.png", "images/KH.png",
                                          "images/AH.png", "images/2S.png",
                                          "images/3S.png", "images/4S.png",
                                          "images/5S.png", "images/6S.png",
                                          "images/7S.png", "images/8S.png",
                                          "images/9S.png", "images/10S.png",
                                          "images/JS.png", "images/QS.png",
                                          "images/KS.png", "images/AS.png",};

namespace Ui {
class GameWindow;
}

class GameWindow : public QMainWindow
{
    Q_OBJECT

public:
    //Constructor that gets the card and player ammount from the menu window
    explicit GameWindow(QWidget *parent = nullptr,
                        int cards = 0,
                        int players = 0);
    //Deconstructor
    ~GameWindow();

private slots:

    //Handles all the card QPushButton clicks
    void handle_button_click();

    //Turns the cards back if they were not a pair
    void turn_cards();

    //Updates the players name when changed in the QLineEdit
    void update_playername();

    //Takes the user back to the main menu window
    void back_to_menu();

    //Does the necessary operations when a pair is found.
    void found_pair();

private:
    Ui::GameWindow *ui;

    //Initialises the card grid of QPushButtons
    void init_btn_grid();

    //Creates the players, the QLineEdits for the players and the QGraphics
    //components for the players decks
    void create_player_boxes();

    //Initialises the cards to the already made button grid.
    void init_cards();

    //Looks for the next free button and returns its index
    int next_free(int start);

    //Initialises the other UI components, the menu and quit buttons and  the
    //status label.
    void init_ui();

    //Checks if the 2 chosen cards are a pair or not
    void check_pair();

    //Disables or enables all of the buttons ini the grid.
    void toggle_buttons(bool state);

    //Ends the game. Does all the necessary announcements and scoresaving
    //before it takes the user back to main menu window
    void end_game();

    //Saves the non-zero scores to the scoreboard file.
    void save_score();

    //Adds the card image to the players graphical card pack.
    void add_to_pack(QString image);

    //UI placement and size constants
    const int btnMARGIN = 20;
    const int btnWIDTH = 50;
    const int btnHEIGHT = 80;

    const int GRID_MARGIN_X = 80;
    const int GRID_MARGIN_Y = 50;

    const int WINDOW_SIZE_X = 700;
    const int WINDOW_SIZE_Y = 700;

    const int UI_BTN_WIDTH = 80;
    const int UI_BTN_HEIGHT = 50;

    //Useful and necessary information for the game to run

    //Grid size
    int columns_ = 0;
    int rows_ = 0;

    //Card and player numbers
    int card_nro_ = 0;
    int player_nro_ = 0;

    //How many pairs are still on the board
    int pairs_in_play = 0;

    //What players turn it is
    int player_in_turn = 0;

    //Ui element pointers
    QPushButton* close_button_;
    QPushButton* menu_button_;
    QLabel* game_status_;

    //Information about the game status and game components for easy access

    //Card by button
    std::map<QPushButton*, card> cards_;

    //All the buttons
    std::vector<QPushButton*> buttons_;

    //Currently selected cards
    std::vector<QPushButton*> selected_cards_;

    //Players QLineEdits
    std::vector<QLineEdit*> player_boxes_;

    //All the players
    std::vector<player> players_;

    //The players graphical card packs.
    std::vector<QGraphicsScene*> card_packs_;

};

#endif // GAMEWINDOW_HH
