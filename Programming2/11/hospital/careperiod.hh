/* Class CarePeriod
 * ----------
 * COMP.CS.110 SPRING 2021
 * ----------
 * Class for describing a patient's care period in hospital.
 *
 * The careperiod contains details of a patients stay at the hospital. It has
 * the information about what staff members were assigned to the patient and
 * when the patient came to the hospital and when they left. It can also print
 * out the information.
 * */
#ifndef CAREPERIOD_HH
#define CAREPERIOD_HH

#include "person.hh"
#include "date.hh"
#include <string>

class CarePeriod
{
public:
    // Constructor, start date given as a string (ddmmyyyy).
    CarePeriod(const std::string& start, Person* patient);

    // Constructor, start date given as a Date object.
    CarePeriod(const Date& start, Person* patient);

    // Destructor.
    ~CarePeriod();

    // Prints the data from the care period.
    void print();

    // Adds a staaff name to the care period
    void add_staff(Person*);

    //End careperiod
    void end_careperiod(const Date& end);

    //Check if careperiod is ongoing
    bool is_on_going();

    //Prints careperiods for staff member
    void print_staff();

private:
    Person* patient_;
    Date start_;
    Date end_;

    // More attributes and methods
    std::vector<Person*> staff_;
    bool ended_;
};

#endif // CAREPERIOD_HH
