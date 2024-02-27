#include "careperiod.hh"
#include <iostream>

CarePeriod::CarePeriod(const std::string& start, Person* patient):
    patient_(patient), start_(start), ended_(false)
{
}

CarePeriod::CarePeriod(const Date &start, Person* patient):
    patient_(patient), start_(start), ended_(false)
{
}

CarePeriod::~CarePeriod()
{
}

void CarePeriod::print()
{
    std::cout << "* Care period: "; start_.print(); std::cout << " - ";

    if (ended_)
        end_.print();

    std::cout << std::endl;

    std::cout << "  - Staff:";
    if (staff_.empty()){
        std::cout << " None" << std::endl;
    }
    else {
        for (auto name : staff_) {
            std::cout << " "; name->print_id();
        }
        std::cout << std::endl;
    }
}

void CarePeriod::add_staff(Person* staff_name)
{
    staff_.push_back(staff_name);
}

void CarePeriod::end_careperiod(const Date &end)
{
    end_ = end;
    ended_ = true;
}

bool CarePeriod::is_on_going()
{
    return ended_;
}

void CarePeriod::print_staff()
{
    start_.print(); std::cout << " - ";

    if (ended_)
        end_.print();

    std::cout << std::endl;

    std::cout << "* Patient: "; patient_->print_id(); std::cout << std::endl;
}

