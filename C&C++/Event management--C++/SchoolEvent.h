/*
 * Class SchoolEvent is the subclass of Event
 * 
 * It overrides the function lessthan(), which will return the value 
 *      of a bool according to the comparison of date of two events
 * 
 */

#ifndef SCHOOLEVENT_H
#define SCHOOLEVENT_H

#include <string>
#include "Event.h"


class SchoolEvent:public Event
{
  public:
    SchoolEvent(string="Unknown",int=0);
    ~SchoolEvent();
    bool operator<(Event*);
  
};

#endif

