#ifndef BOOK_HH
#define BOOK_HH

#include <string>
#include "date.hh"

class Book
{
public:
    // Constructor
    Book(std::string author, std::string title);

    // Print method for book class
    void print() const;
    void loan(Date loan_date);
    void renew();
    void give_back();

private:

    std::string author_;
    std::string title_;
    Date loan_date_;
    bool loaned_ = false;
    Date return_date_;
};

#endif // BOOK_HH
