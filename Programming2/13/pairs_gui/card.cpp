/*
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
#include "card.hh"

card::card():
    card_image_(""), visibility_(EMPTY)
{

}
//Constructs and adds the card back icon to the button
card::card(QPushButton* button, const QString image):
    button_(button), card_image_(image), visibility_(HIDDEN)
{
    button_->setIcon(QIcon(CARD_BACK));
}

void card::set_visibility(const Visibility_type visibility)
{
    visibility_ = visibility;
}

void card::turn()
{
    //Checks which way to turn the card and sets the appropriate image to
    //the button
    if (visibility_ == HIDDEN)
    {
        visibility_ = OPEN;
        QIcon icon(card_image_);
        icon.addPixmap(QPixmap(card_image_),QIcon::Disabled);
        button_->setIcon(icon);
    }
    else if (visibility_ == OPEN)
    {
        visibility_ = HIDDEN;
        button_->setIcon(QIcon(CARD_BACK));
    }
}
//Sets the buttons icon to blank to synmbolize that it is missing
void card::remove_from_game_board()
{
    visibility_ = EMPTY;
    button_->setIcon(QIcon());
}

QString card::get_image()
{
    return card_image_;
}
