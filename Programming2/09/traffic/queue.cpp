#include "queue.hh"
#include <iostream>
// Implement the member functions of Queue here

Queue::Queue(unsigned int cycle)
{
    cycle_ = cycle;
}

Queue::~Queue()
{

}

void Queue::enqueue(string reg)
{
    Vehicle* new_vehicle = new Vehicle {reg, nullptr};

    if (is_green_) {
        std::cout << "GREEN: The vehicle " << reg << " need not stop to wait" << std::endl;
    } else if (first_ == nullptr) {
        first_ = new_vehicle;
        last_ = new_vehicle;
    } else {
        last_->next = new_vehicle;
        last_ = new_vehicle;
    }
}

void Queue::switch_light()
{
    if (first_ == nullptr) {

        std::string light_clr = "";
        if (is_green_) {
            light_clr = "RED";
            is_green_ = false;
        } else {
            light_clr = "GREEN";
            is_green_ = true;
        }
        std::cout << light_clr << ": No vehicles waiting in traffic lights" << std::endl;

    } else {

    std::cout << "GREEN: " << "Vehicle(s) ";

    while (cars_gone_ < cycle_) {
        Vehicle* car_to_go = first_;
        first_ = car_to_go->next;
        std::cout << car_to_go->reg_num << " ";
        dequeue(car_to_go);
        ++cars_gone_;

        if (first_ == nullptr)
            break;
    }
    std::cout << "can go on" << std::endl;
    is_green_ = false;
    cars_gone_ = 0;
    }
}

void Queue::reset_cycle(unsigned int cycle)
{
    cycle_ = cycle;
}

void Queue::print()
{
    if (first_ == nullptr) {

        std::string light_clr = "";
        if (is_green_) {
            light_clr = "GREEN";
        } else {
            light_clr = "RED";
        }
        std::cout << light_clr << ": No vehicles waiting in traffic lights" << std::endl;
    } else {
    Vehicle* vehicle = first_;

    std::string light_clr = "";
    if (is_green_)
        light_clr = "GREEN";
    else
        light_clr = "RED";

    std::cout << light_clr << ":" << " Vehicle(s) ";

    while (vehicle != nullptr) {
        std::cout << vehicle->reg_num << " ";
        vehicle = vehicle->next;
    }
    std::cout << "waiting in traffic lights" << std::endl;
    }
}
