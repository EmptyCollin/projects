#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

#include "WorkEvent.h"


bool WorkEvent::operator<(Event* another)
{
    return(getPriority()<(another->getPriority()));
}

WorkEvent::WorkEvent(string name, int priority):Event(name,priority)
{
}
WorkEvent::~WorkEvent()
{
}


