#include "account.hh"
#include <iostream>

using namespace std;

Account::Account(const std::string& owner, bool has_credit):
    owner_(owner), credit_(has_credit) {


    generate_iban();
}

// Setting initial value for the static attribute running_number_
int Account::running_number_ = 0;

void Account::generate_iban()
{
    ++running_number_;
    std::string suffix = "";
    if(running_number_ < 10)
    {
        suffix.append("0");
    }
    else if(running_number_ > 99)
    {
        std::cout << "Too many accounts" << std::endl;
    }
    suffix.append(std::to_string(running_number_));

    iban_ = "FI00 1234 ";
    iban_.append(suffix);
}

void Account::print() const {
    cout << owner_ << " : " << iban_ << " : " << money_ << " euros" << endl;
}
void Account::save_money(int money) {
    money_ += money;
}
void Account::take_money(int money) {
    if (money <= money_ + credit_limit_) {
        money_ -= money;
        cout << money << " euros taken: new balance of " << iban_ << " is " << money_ << " euros" << endl;
    } else if (credit_) {
        cout << "Cannot take money: credit limit overflow" << endl;
    } else {
        cout << "Cannot take money: balance underflow" << endl;
    }
}
void Account::set_credit_limit(int money) {
    if (credit_ == true) {
        credit_limit_ = money;
    } else {
        cout << "Cannot set credit limit: the account has no credit card" << endl;
    }
}
void Account::transfer_to(Account& dest_account, int money) {
    if (money <= money_ + credit_limit_) {
        money_ -= money;
        dest_account.save_money(money);
        cout << money << " euros taken: new balance of " << iban_ << " is " << money_ << " euros" << endl;
    } else {
        if (credit_ == true) {
            cout << "Cannot take money: credit limit overflow" << endl;
        } else {
            cout << "Cannot take money: balance underflow" << endl;
        }
        cout << "Transfer from " << iban_ << " failed" << endl;
    }
}
