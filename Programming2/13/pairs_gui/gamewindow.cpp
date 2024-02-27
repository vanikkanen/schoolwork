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

#include "gamewindow.hh"
#include "ui_gamewindow.h"
#include "mainwindow.hh"
#include "card.hh"
#include <math.h>
#include <string>
#include <random>
#include <algorithm>
#include <vector>
#include <chrono>
#include <fstream>
#include <QGraphicsView>
#include <QGraphicsItem>
#include <QObject>
#include <QTimer>
#include <QPoint>
#include <QCursor>
#include <QLineEdit>
#include <QPushButton>
#include <QDebug>

// Constructs the window and sets the parameters
GameWindow::GameWindow(QWidget *parent, int pairs, int players):
    QMainWindow(parent), ui(new Ui::GameWindow), player_nro_(players),
    pairs_in_play(pairs)
{
    ui->setupUi(this);

    card_nro_ = 2*pairs;

    columns_ = ceil(sqrt(card_nro_));
    rows_ = columns_;

    this->setFixedSize(WINDOW_SIZE_X, WINDOW_SIZE_Y);

    init_btn_grid();
    create_player_boxes();
    init_ui();
    init_cards();
}

GameWindow::~GameWindow()
{
    delete ui;
}

//Makes the buttons to the gameboard
void GameWindow::init_btn_grid()
{
    int index = 1;

    for (int r = 0; r < rows_; ++r)
    {
        for (int c = 0; c < columns_; ++c)
        {
            QPushButton* pushButton = new QPushButton(this);
            //Pacing the card to the right place in the ui.
            pushButton->setGeometry(GRID_MARGIN_X + c*btnWIDTH,
                                    GRID_MARGIN_Y + r*btnHEIGHT,
                                    btnWIDTH, btnHEIGHT);
            connect(pushButton, SIGNAL(clicked()), this,
                    SLOT(handle_button_click()));
            //Setting the icon size for the card images.
            pushButton->setIconSize(QSize(pushButton->width(),
                                          pushButton->height()));
            //Adding the button to the list of buttons.
            buttons_.push_back(pushButton);

            //Checks if there are enough buttons already made or if we need
            //more rows for the buttons yet to come
            if (index == card_nro_) {
                break;
            }
            if (r == rows_) {
                rows_ += 1;
            }

            ++index;
        }
        if (index == card_nro_) {
            break;
        }
    }
}

//Creates players, their name boxes and the graphical elements for the players
void GameWindow::create_player_boxes()
{
    for (int i = 0; i < player_nro_; ++i)
    {
        //Creating the QLineEdit for the player and setting its starting name
        //to PlayerN. Connects the QLineEdit to slot that updates the players
        //name
        QLineEdit* playername = new QLineEdit(this);
        playername->setText("Player" + QString::number(i + 1));
        playername->setGeometry(WINDOW_SIZE_X - 100, 50 + i*100, 80, 40);

        player_boxes_.push_back(playername);

        connect(playername, SIGNAL(editingFinished()), this, SLOT(update_playername()));

        //Creatiing a new player
        player new_player = player(playername->text());

        players_.push_back(new_player);

        //Creating a graphical component that will show the players found pairs
        QGraphicsScene* scene = new QGraphicsScene(this);

        QGraphicsView* view = new QGraphicsView(this);
        view->setScene(scene);
        view->setGeometry(WINDOW_SIZE_X - 210, 50 + i*100, 100, 70);
        view->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        view->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

        card_packs_.push_back(scene);

        view->show();

    }
}

//Initialises the buttons with cards
void GameWindow::init_cards()
{
    //Creating a seed from the current time for the random generator
    unsigned long int seed = std::chrono::duration_cast
            <std::chrono::milliseconds>
            (std::chrono::system_clock::now().time_since_epoch()).count();

    std::default_random_engine randomEng(seed);
    std::uniform_int_distribution<int> distr(0, buttons_.size() - 1);

    distr(randomEng);

    //Creating a card for each of the buttons on the board
    for (unsigned int i = 0, c = 0; i < buttons_.size(); i += 2, ++c)
    {

        QString card_image(CARD_IMAGES.at(c));

        for (int j = 0; j < 2; ++j)
        {
            int rand_button = distr(randomEng);
            QPushButton* pushButton = buttons_.at(next_free(rand_button));

            card new_card = card(pushButton, card_image);
            cards_.insert({pushButton, new_card});
        }
    }
}

//Initialises all the all the time ui elements for the game board
void GameWindow::init_ui()
{
    close_button_ = new QPushButton(this);
    close_button_->setText("CLOSE");
    close_button_->setGeometry(WINDOW_SIZE_X - 100, WINDOW_SIZE_Y - 80,
                               UI_BTN_WIDTH, UI_BTN_HEIGHT);
    connect(close_button_, SIGNAL(clicked()), this, SLOT(close()));

    menu_button_ = new QPushButton(this);
    menu_button_->setText("MENU");
    menu_button_->setGeometry(WINDOW_SIZE_X - 100, WINDOW_SIZE_Y - 130,
                               UI_BTN_WIDTH, UI_BTN_HEIGHT);
    connect(menu_button_, SIGNAL(clicked()), this, SLOT(back_to_menu()));

    game_status_ = new QLabel(this);
    game_status_->setGeometry(WINDOW_SIZE_X - 600, WINDOW_SIZE_Y - 80, 400, 30);
    game_status_->setText(players_.at(player_in_turn).get_name() += "s turn to play");
}

//Helper function for the init_cards function. Returns the next free buttons
//index in the vector
int GameWindow::next_free(int start)
{
    //Starting from start value to the end of the buttons_ vector
    for (unsigned int i = start; i < buttons_.size(); ++i)
    {
        if (cards_.find(buttons_.at(i)) == cards_.end())
        {
            return i;
        }
    }
    //Continues from the start
    for (int i = 0; i < start; ++i)
    {
        if (cards_.find(buttons_.at(i)) == cards_.end())
        {
            return i;
        }
    }
    //Shouldnt ever end up here
    qDebug() << "No more empty buttons";
    return buttons_.size() - 1;
}

//Checks if the 2 turned cards are a pair
void GameWindow::check_pair()
{
    //Disables all the buttons on the board
    toggle_buttons(true);

    QPushButton* card1 = selected_cards_.at(0);
    QPushButton* card2 = selected_cards_.at(1);

    //Checks if the cards are a pair
    if (cards_.at(card1).get_image() == cards_.at(card2).get_image())
    {
        //pair
        add_to_pack(cards_.at(card1).get_image());
        game_status_->setText(players_.at(player_in_turn).get_name()
                              += " found a pair!");
        QTimer::singleShot(2000, this, SLOT(found_pair()));

    }
    else
    {
        //no pair
        player_in_turn += 1;
        if (player_in_turn == player_nro_)
        {
            player_in_turn = 0;
        }
        game_status_->setText(players_.at(player_in_turn).get_name()
                              += "s turn to play");
        QTimer::singleShot(2000, this, SLOT(turn_cards()));
    }

}
//Disables or enables all the buttons
void GameWindow::toggle_buttons(bool state)
{
    for (unsigned int i = 0; i < buttons_.size(); ++i)
    {
        buttons_.at(i)->setDisabled(state);
    }
}

//Ends the game
void GameWindow::end_game()
{
    //Checking who is the winner
    int max_pairs = 0;
    QString winner;

    bool tie = false;

    for (unsigned int i = 0; i < players_.size(); ++i)
    {
        int pairs = players_.at(i).get_pairs();
        if (pairs > max_pairs)
        {
            winner = players_.at(i).get_name();
            max_pairs = pairs;
        }
        else if (pairs == max_pairs and pairs > 0)
        {
            winner += " and " + players_.at(i).get_name();
            tie = true;
        }
    }

    if (tie)
    {
        game_status_->setText("It's a tie between " + winner + " with "
                              + QString::number(max_pairs) + " pairs!");
    }
    else
    {
        game_status_->setText(winner + " has won the game with "
                              + QString::number(max_pairs) + " pairs!");
    }

    //Save the score and go back to menu window
    save_score();
    QTimer::singleShot(2000, this, SLOT(back_to_menu()));
}

//Save the score to the scoreboard file
void GameWindow::save_score()
{
    //Get the old data from the file
    std::vector<std::string> old_scores;
    std::string file_line = "";
    std::ifstream input_file("scoreboard");

    while (getline(input_file, file_line))
    {
        old_scores.push_back(file_line);
    }
    input_file.close();

    //Add the new data to the file
    int index = 0;
    QString line = "";
    std::ofstream output_file("scoreboard");

    for(unsigned int i = 0; i < players_.size(); ++i)
    {
        player player = players_.at(i);
        line = "";
        if (player.get_pairs() == 0)
            continue;

        line += player.get_name() + " got " +
                QString::number(player.get_pairs()) + "/" +
                QString::number(card_nro_/2) + " pairs: " +
                QString::number(player_nro_) + " player game";

        output_file << line.toStdString() << std::endl;
        ++index;
    }

    //Add old data to the file until there is enough
    for (auto score : old_scores)
    {
        ++index;
        output_file << score << std::endl;

        if (index == 29)
            break;
    }
    output_file.close();
}

//Adds the graphical image to the players card pack
void GameWindow::add_to_pack(QString image)
{
    //Rotates the image 90 degrees
    QPixmap pic = QPixmap(image);
    QMatrix rm;
    rm.rotate(90);
    pic = pic.transformed(rm);

    //Scales and adds the card image to the scene of the player
    QGraphicsPixmapItem* item = new QGraphicsPixmapItem( pic.scaledToWidth(95));

    card_packs_.at(player_in_turn)->addItem(item);
    int pairs = players_.at(player_in_turn).get_pairs();

    //Moves the new card slightly to the right in the card pack
    item->moveBy(pairs*15, 0);

}

//Does all the necessary things when a pair is found
void GameWindow::found_pair()
{

    QPushButton* card1 = selected_cards_.at(0);
    QPushButton* card2 = selected_cards_.at(1);

    //Removing cards from the board
    cards_.at(card1).remove_from_game_board();
    cards_.at(card2).remove_from_game_board();

    //Adding score for the player
    players_.at(player_in_turn).add_pair();

    //Removing the buttons from the buttons pool
    buttons_.erase(std::find(buttons_.begin(), buttons_.end(), card1));
    buttons_.erase(std::find(buttons_.begin(), buttons_.end(), card2));

    //Clearing selected cards
    selected_cards_.clear();

    pairs_in_play -= 1;
    if (pairs_in_play == 0)
    {
        //End the game
        end_game();
    }

    //Enables buttons
    toggle_buttons(false);
}

//Takes the user back to the menu and deletes this window
void GameWindow::back_to_menu()
{
    MainWindow* mm = new MainWindow();
    mm->show();
    delete this;
}

//Turns the cards back around if a pair was not found
void GameWindow::turn_cards()
{
    QPushButton* card1 = selected_cards_.at(0);
    QPushButton* card2 = selected_cards_.at(1);

    cards_.at(card1).turn();
    cards_.at(card2).turn();

    selected_cards_.clear();

    toggle_buttons(false);
}

//Updates the player name
void GameWindow::update_playername()
{
    //Checks what players name was changed
    QLineEdit* line_edit = qobject_cast<QLineEdit*>(sender());
    unsigned int index = 0;
    for (unsigned int i = 0; i < player_boxes_.size(); ++i)
    {
        if (player_boxes_.at(i) == line_edit)
        {
            index = i;
            break;
        }
    }
    //Updates the players name
    players_.at(index).update_name(line_edit->text());

    //if the player is in turn now changes the label to display the correct name
    if (players_.at(index).get_name() == players_.at(player_in_turn).get_name())
    {
        game_status_->setText(players_.at(player_in_turn).get_name()
                              += "s turn to play");
    }
}


void GameWindow::handle_button_click()
{
    QPoint global_click_position = QCursor::pos();

    // Counting local cursor position, i.e. decreasing
    // Main Window's location from the global one
    int local_x = global_click_position.x() - geometry().x();
    int local_y = global_click_position.y() - geometry().y();
    QPoint local_click_position = QPoint(local_x, local_y);

    for(unsigned int i = 0; i < cards_.size(); ++i)
    {
        if(buttons_.at(i)->geometry().contains(local_click_position))
        {
            QPushButton* selected_card = buttons_.at(i);

            //Makes sure that the samee button cant be selected again
            if (std::find(selected_cards_.begin(), selected_cards_.end(), selected_card) == selected_cards_.end())
            {
                selected_card->setDisabled(true);
                cards_.at(selected_card).turn();
                selected_cards_.push_back(selected_card);

                if (selected_cards_.size() == 2)
                {
                    check_pair();
                }
            }
            return; // For efficiency reasons
                    // (only one button can be clicked at a time)
        }
    }
}
