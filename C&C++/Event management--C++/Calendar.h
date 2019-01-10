/*
 * 
 * Class Calendar is used to record and manage the events.
 * 
 * It consists of the calendar title, a variable of eventNum, and an object of List which contains
 *   the pointers of events.
 * 
 * Function add(Event*) gets a pointer of Event object as parameter and stores
 *   it in the array with ascending order by date.
 * 
 * Function format(string&) take a reference of a string and asign it as the format string of the 
 *   events stored in the calendar.
 * 
 */


#ifndef CALENDAR_H
#define CALENDAR_H


#include "Event.h"
#include "SchoolEvent.h"
#include "WorkEvent.h"
#include "List.h"
#include <string.h>



class Calendar{
    public:
        Calendar(string="My Calendar");
        ~Calendar();
        void add(Event*);       
        void format(string& outStr);
        void setTitle(string);
        void print();
        void copyEvents(Array&);
    private:
        string title;
        List<Event*> list;

};
#endif

