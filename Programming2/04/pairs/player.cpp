#include "player.hh"
#include "card.hh"
#include <iostream>

Player::Player(const std::string &name)
{
    name_ = name;
}

std::string Player::get_name() const
{
    return name_;
}

unsigned int Player::number_of_pairs() const
{
    return cards_/2;
}

void Player::add_card(Card &card)
{
    card.remove_from_game_board();
    ++cards_;
}

void Player::print() const
{
    std::cout <<"*** " << name_ << " has " << cards_/2 << " pair(s)." << std::endl;
}
