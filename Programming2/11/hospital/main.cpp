/*
 * COMP.CS.110 SPRING 2021
 * ----------
 * Program that consists of multiple classes. Hospital class is the main class
 * that contains the the appearances of the person and careperiod classes. CLI,
 * Utils and Date contain the helpfull command reading, utility functions like
 * split and checking if something is a number. Date class contains the date
 * and the methods for it. Hospital has all the functions that the user can
 * input for the program. It also has all the data structures that contain all
 * the other appearances of the other classes as pointers to them for easy
 * access. Hospital class then calls the other classess for their methods if
 * necessary. Person class is a class for both the patients and the staff, it
 * also contains the medication assigned for the patient.
 * Careperiod contains the dates of the start of the care, the end of the care
 * and if any staff were assigned for the patient on this hospital visit.
 * The program can also read inputs from a file if needed.
 * When the program ends it frees all the assigned memory from the pointers,
 * before it ends its run.
 * ----------
 * Writer of the program:
 * Name: Valtteri Nikkanen
 * Student number: 282688
 * User id's: nikkanev
 * E-mail: valtteri.nikkanen@tuni.fi
*/

#include "cli.hh"
#include "hospital.hh"
#include <string>

const std::string PROMPT = "Hosp> ";


int main()
{
    Hospital* hospital = new Hospital();
    Cli cli(hospital, PROMPT);
    while ( cli.exec() ){}

    delete hospital;
    return EXIT_SUCCESS;
}
