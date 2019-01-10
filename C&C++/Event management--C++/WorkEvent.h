/*
 * Class WorkEvent is the subclass of Event
 * 
 * It overrides the function lessthan(), which will return the value 
 *      of a bool according to the comparison of prioritiy of two events
 * 
 */


#ifndef WORKEVENT_H
#define WORKEVENT_H

#include <string>
#include "Event.h"
using namespace std;

class WorkEvent:public Event
{
  public:
    WorkEvent(string="Unknown",int=0);
    ~WorkEvent();
    bool operator<(Event*);

};

#endif

