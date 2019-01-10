/*
 * View class offers the user interface for I/O
 * 
 * displayMenu() take a reference of integer as parameter and store the selection 
 *   in this integer
 * 
 * createEvent() will read the infromation of an event and create an pointer of event
 *   based of them. This pointer will return to the Control class
 * 
 * printCalender(): this function take a string as parameter and print it out.
 * 
 */

#ifndef VIEW_H
#define VIEW_H

#include <string>
#include "Event.h"
#include "Calendar.h"

class View
{
  public:
    void displayMenu(int&);
    void readEvent(string&,int&,int&,int&,int&,int&,int&);
    void print(Calendar&) const;
    void printCalender(string outStr) const;
    void eventType(string&);

private:

};

#endif
