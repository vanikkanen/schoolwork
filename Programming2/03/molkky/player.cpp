#include "player.hh"
#include <iostream>
#include <string>

Player::Player(std::string name)
{
    name_ = name;
    points_ = 0;
}

void Player::add_points(int points)
{
    if (points_ + points > 50) {
        points_ = 25;
        std::cout << name_ << " gets penalty points!" << std::endl;
    } else {
        points_ += points;
    }
}

std::string Player::get_name()
{
    return name_;
}

int Player::get_points()
{
    return points_;
}

bool Player::has_won()
{
    if (points_ == 50) {
        return true;
    } else {
        return false;
    }
}
