#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

#include "SchoolEvent.h"


SchoolEvent::SchoolEvent(string name, int priority) : Event(name, priority)
{ 

}

bool SchoolEvent::operator<(Event* another)
{
    return (getDate()<(another->getDate()));
}

SchoolEvent::~SchoolEvent(){
}
