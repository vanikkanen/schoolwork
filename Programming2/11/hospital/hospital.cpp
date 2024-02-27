#include "hospital.hh"
#include "utils.hh"
#include <iostream>
#include <set>
#include <memory>
#include <vector>
#include <algorithm>
Hospital::Hospital()
{
}

Hospital::~Hospital()
{
    // Deallocating staff
    for( std::map<std::string, Person*>::iterator
         iter = staff_.begin();
         iter != staff_.end();
         ++iter )
    {
        delete iter->second;
    }

    // Deallocating patients
    for( std::map<std::string, Person*>::iterator
         iter = patients_.begin();
         iter != patients_.end();
         ++iter )
    {
        delete iter->second;
    }
    // Deallocating careperiods
    for (auto patient : careperiods_)
    {
    std::string patient_id = patient.first;
    for( std::vector<CarePeriod*>::iterator
         iter = careperiods_.at(patient_id).begin();
         iter != careperiods_.at(patient_id).end();
         ++iter )
    {
        delete *iter;
    }
    }
}

void Hospital::recruit(Params params)
{
    std::string specialist_id = params.at(0);
    if( staff_.find(specialist_id) != staff_.end() )
    {
        std::cout << ALREADY_EXISTS << specialist_id << std::endl;
        return;
    }
    Person* new_specialist = new Person(specialist_id);
    staff_.insert({specialist_id, new_specialist});
    staff_careperiods_[specialist_id];
    std::cout << STAFF_RECRUITED << std::endl;
}

void Hospital::enter(Params params)
{
    std::string patient_id = params.at(0);
    if (current_patients_.find(patient_id) != current_patients_.end())
    {
        std::cout << ALREADY_EXISTS << patient_id << std::endl;
        return;
    }
    // Check if the petient has already been in the hospital
    Person* new_patient = new Person(patient_id);
    if (patients_.find(patient_id) == patients_.end())
    {
        current_patients_.insert({patient_id, new_patient});
        patients_.insert({patient_id, new_patient});
    }
    else
    {
        delete new_patient;
        new_patient = patients_.at(patient_id);
        current_patients_.insert({patient_id, new_patient});
    }

    //Make a new Care period
    CarePeriod* new_careperiod = new CarePeriod(utils::today, new_patient);
    careperiods_[patient_id];
    careperiods_[patient_id].push_back(new_careperiod);

    std::cout << PATIENT_ENTERED << std::endl;
}

void Hospital::leave(Params params)
{
     std::string patient_id = params.at(0);
     if (current_patients_.find(patient_id) == current_patients_.end())
     {
         std::cout << CANT_FIND << patient_id << std::endl;
         return;
     }
     current_patients_.erase(patient_id);
     // Ending the ongoing careperiod
     for (auto careperiod : careperiods_.at(patient_id))
     {
         if (!careperiod->is_on_going())
             careperiod->end_careperiod(utils::today);
     }
     std::cout << PATIENT_LEFT << std::endl;
}

void Hospital::assign_staff(Params params)
{
    std::string staff_id = params.at(0);
    std::string patient_id = params.at(1);

    if (staff_.find(staff_id) == staff_.end())
    {
        std::cout << CANT_FIND << staff_id << std::endl;
        return;
    }
    if (current_patients_.find(patient_id) == current_patients_.end())
    {
        std::cout << CANT_FIND << patient_id << std::endl;
        return;
    }

    for (auto careperiod : careperiods_.at(patient_id))
    {
        if (!careperiod->is_on_going())
        {
            careperiod->add_staff(staff_.at(staff_id));
            staff_careperiods_[staff_id];
            staff_careperiods_[staff_id].push_back(careperiod);
        }
    }
    std::cout << STAFF_ASSIGNED << patient_id << std::endl;
}

void Hospital::add_medicine(Params params)
{
    std::string medicine = params.at(0);
    std::string strength = params.at(1);
    std::string dosage = params.at(2);
    std::string patient = params.at(3);
    if( not utils::is_numeric(strength, true) or
        not utils::is_numeric(dosage, true) )
    {
        std::cout << NOT_NUMERIC << std::endl;
        return;
    }
    std::map<std::string, Person*>::const_iterator
            patient_iter = current_patients_.find(patient);
    if( patient_iter == current_patients_.end() )
    {
        std::cout << CANT_FIND << patient << std::endl;
        return;
    }
    patient_iter->second->add_medicine(medicine, stoi(strength), stoi(dosage));
    medicines_[medicine];
    medicines_[medicine].push_back(patient_iter->second);
    std::cout << MEDICINE_ADDED << patient << std::endl;
}

void Hospital::remove_medicine(Params params)
{
    std::string medicine = params.at(0);
    std::string patient = params.at(1);
    std::map<std::string, Person*>::const_iterator
            patient_iter = current_patients_.find(patient);
    if( patient_iter == current_patients_.end() )
    {
        std::cout << CANT_FIND << patient << std::endl;
        return;
    }
    patient_iter->second->remove_medicine(medicine);

    medicines_.at(medicine).erase(
                        remove(medicines_.at(medicine).begin(),
                        medicines_.at(medicine).end(), patient_iter->second),
                    medicines_.at(medicine).end());

    if (medicines_.at(medicine).empty())
        medicines_.erase(medicine);

    std::cout << MEDICINE_REMOVED << patient << std::endl;
}

void Hospital::print_patient_info(Params params)
{
    std::string patient_id = params.at(0);
    if (patients_.find(patient_id) == patients_.end())
    {
        std::cout << CANT_FIND << patient_id << std::endl;
        return;
    }
    Person* patient_ptr = patients_.at(patient_id);
    print_patient_info(patient_ptr);
}

void Hospital::print_care_periods_per_staff(Params params)
{
    std::string staff_id = params.at(0);
    if (staff_.find(staff_id) == staff_.end())
    {
        std::cout << CANT_FIND << staff_id << std::endl;
        return;
    }
    if (staff_careperiods_.at(staff_id).empty())
    {
        std::cout << NONE << std::endl;
        return;
    }
    for (auto careperiod : staff_careperiods_.at(staff_id))
        careperiod->print_staff();
}

void Hospital::print_all_medicines(Params)
{
    if( medicines_.empty() )
    {
        std::cout << "None" << std::endl;
        return;
    }
    for (auto medicine : medicines_)
    {
        std::vector<std::string> patient_ids;
        std::cout << medicine.first << " prescribed for" << std::endl;
        for (const auto patient : medicine.second)
        {
            patient_ids.push_back(patient->get_id());
        }
        sort(patient_ids.begin(),patient_ids.end());
        for (const auto patient_id : patient_ids)
        {
            std::cout << "* " << patient_id << std::endl;
        }
    }
}

void Hospital::print_all_staff(Params)
{
    if( staff_.empty() )
    {
        std::cout << "None" << std::endl;
        return;
    }
    for( std::map<std::string, Person*>::const_iterator iter = staff_.begin();
         iter != staff_.end();
         ++iter )
    {
        std::cout << iter->first << std::endl;
    }
}

void Hospital::print_all_patients(Params)
{
    if(patients_.empty()){
        std::cout << NONE << std::endl;
    } else {
        for (auto patient : patients_) {
            std::cout << patient.second->get_id() << std::endl;
            print_patient_info(patient.second);
        }
    }
}

void Hospital::print_current_patients(Params)
{
    if(current_patients_.empty()){
        std::cout << NONE << std::endl;
    } else {
        for (auto patient : current_patients_) {
            std::cout << patient.second->get_id() << std::endl;
            print_patient_info(patient.second);
        }
    }
}


void Hospital::set_date(Params params)
{
    std::string day = params.at(0);
    std::string month = params.at(1);
    std::string year = params.at(2);
    if( not utils::is_numeric(day, false) or
        not utils::is_numeric(month, false) or
        not utils::is_numeric(year, false) )
    {
        std::cout << NOT_NUMERIC << std::endl;
        return;
    }
    utils::today.set(stoi(day), stoi(month), stoi(year));
    std::cout << "Date has been set to ";
    utils::today.print();
    std::cout << std::endl;
}

void Hospital::advance_date(Params params)
{
    std::string amount = params.at(0);
    if( not utils::is_numeric(amount, true) )
    {
        std::cout << NOT_NUMERIC << std::endl;
        return;
    }
    utils::today.advance(stoi(amount));
    std::cout << "New date is ";
    utils::today.print();
    std::cout << std::endl;
}
