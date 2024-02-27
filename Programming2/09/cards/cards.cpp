#include "cards.hh"

// TODO: Implement the methods here

Cards::Cards(): top_(nullptr){
}

void Cards::add(int id)
{
    Card_data* new_card = new Card_data{id, nullptr};

    if (top_ == nullptr) {
        top_ = new_card;
    } else {
        Card_data* previous_top = top_;
        top_ = new_card;
        top_->next = previous_top;
    }
}

void Cards::print_from_top_to_bottom(std::ostream &s)
{
    Card_data* to_print = top_;
    int running_number = 1;

    while (to_print != nullptr) {
        s << running_number << ": " << to_print->data << std::endl;
        to_print = to_print->next;
        ++running_number;
    }
}

bool Cards::remove(int &id)
{
    if (top_ == nullptr)
        return false;

    id = top_->data;
    Card_data* to_remove = top_;
    top_ = to_remove->next;

    delete to_remove;

    return true;
}

bool Cards::bottom_to_top()
{
    if (top_ == nullptr)
        return false;

    Card_data* current_top = top_;
    Card_data* current_bottom = top_;
    Card_data* index = top_;

    while (index != nullptr) {
        current_bottom = index;
        index = index->next;
    }
    current_bottom->next = current_top;
    top_ = current_bottom;
    index = top_;

    while (index != nullptr) {
        if (index->next == top_)
            index->next = nullptr;
        index = index->next;
    }
    return true;
}

bool Cards::top_to_bottom()
{
    if (top_ == nullptr)
        return false;

    Card_data* current_top = top_;
    Card_data* current_bottom = top_;
    Card_data* index = top_;

    while (index != nullptr) {
        current_bottom = index;
        index = index->next;
    }
    current_bottom->next = current_top;
    top_ = current_top->next;
    current_top->next = nullptr;
    return true;
}

void Cards::print_from_bottom_to_top(std::ostream &s)
{
    int running_number = 1;
    s << recursive_print(top_, running_number, s) << std::endl;
}

Cards::~Cards()
{
    while ( top_ != nullptr ) {
       Card_data* item_to_be_released = top_;
       top_ = top_->next;

       delete item_to_be_released;
    }
}

