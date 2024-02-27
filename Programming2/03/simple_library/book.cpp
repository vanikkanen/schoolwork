#include "book.hh"
#include "date.hh"
#include <iostream>

Book::Book(std::string author, std::string title)
{
  author_ = author;
  title_ = title;
}

void Book::print() const
{
    std::cout << author_ << " : " << title_ << std::endl;
    if (not loaned_) {
        std::cout << "- available" << std::endl;
    } else {
        std::cout << "- loaned: "; loan_date_.print();
        std::cout << "- to be returned: "; return_date_.print();
    }
}

void Book::loan(Date date)
{
    if (not loaned_) {

        loan_date_ = date;
        return_date_ = date;
        return_date_.advance(28);
        loaned_ = true;

    } else {
        std::cout << "Already loaned: cannot be loaned" << std::endl;
    }
}

void Book::renew()
{
    if (not loaned_) {
        std::cout << "Not loaned: cannot be renewed" << std::endl;
    } else {
        return_date_.advance(28);
    }
}

void Book::give_back()
{
    if (loaned_) {
        loaned_ = false;
    }
}
