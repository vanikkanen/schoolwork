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
#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include "gamewindow.hh"
#include <QGridLayout>
#include <QPoint>
#include <QCursor>
#include <QGraphicsView>
#include <QDebug>
#include <QPushButton>
#include <QSpinBox>
#include <cmath>
#include <QLineEdit>
#include <QLabel>
#include <fstream>
#include <iostream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->statusBar()->setDisabled(true);
    this->setFixedSize(300, 400);

    init_ui_elements();

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::init_ui_elements()
{
    QLabel* player_label = new QLabel(this);
    player_label->setText("Insert amount of players:");
    int label_width = player_label->width() + 80;
    player_label->setGeometry(10, 25, label_width, 20);

    player_spinbox_ = new QSpinBox(this);
    player_spinbox_->setRange(1, 5);
    int width = player_spinbox_->width() - 40;
    int height = player_spinbox_->height();
    player_spinbox_->setSingleStep(1);
    player_spinbox_->setGeometry(label_width + 10, 20, width, height);

    QLabel* pair_label = new QLabel(this);
    pair_label->setText("Insert ammount of pairs:");
    pair_label->setGeometry(10, 55, label_width, 20);

    pair_spinbox_ = new QSpinBox(this);
    pair_spinbox_->setRange(2, 26);
    player_spinbox_->setSingleStep(1);
    pair_spinbox_->setGeometry(label_width + 10, 50, width, height);

    start_button_ = new QPushButton(this);
    start_button_->setText("Start Game");
    start_button_->setGeometry(40, 110, start_button_->width(), start_button_->height());
    connect(start_button_, SIGNAL(clicked()), this, SLOT(open_window()));

    close_button_ = new QPushButton(this);
    close_button_->setText("Close");
    close_button_->setGeometry(50 + start_button_->width(), 110, start_button_->width(), start_button_->height());
    connect(close_button_, SIGNAL(clicked()), this, SLOT(close()));

    QLabel* scoreboard_label = new QLabel(this);
    scoreboard_label->setText("Scoreboard of last 30 games");
    scoreboard_label->setGeometry(10, 170, 200, scoreboard_label->height());

    scoreboard_ = new QTextBrowser(this);
    scoreboard_->setGeometry(10, 200, 280, 100);
    read_file();
}

void MainWindow::read_file()
{
    //Adds teh file line by line to the text browser
    std::string line = "";
    std::ifstream input_file("scoreboard");
    while (getline(input_file, line))
    {
        scoreboard_->append(QString::fromStdString(line));
    }
    input_file.close();
}

void MainWindow::open_window()
{
    //Opens the game window and hides this window
    start_button_->setEnabled(false);
    players_ = player_spinbox_->value();
    pairs_ = pair_spinbox_->value();

    gw = new GameWindow(this, pairs_, players_);
    gw->show();
    this->hide();
}

