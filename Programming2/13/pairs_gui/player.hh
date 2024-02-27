/* Class: player
 * ----------------
 * Represents a single player that is playing the game.
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

#ifndef PLAYER_HH
#define PLAYER_HH

#include <QString>

class player
{
public:
    //Constructor
    player(const QString& player_name);

    //Adds a pair to the players total
    void add_pair();

    //Updates the players name
    void update_name(QString new_name);

    //Returns the players name
    QString get_name();

    //Returns the players pair amunt
    int get_pairs();

private:
    //Name and pairs for the player
    QString name_;
    int pairs_ = 0;
};

#endif // PLAYER_HH
