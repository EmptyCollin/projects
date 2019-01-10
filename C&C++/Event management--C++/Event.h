/*
 * Class Event records the event and the time it is going to take place 
 *                                            --(or had took place).
 * setDate() function user set the date by pass 5 integers as parameter
 *
 * getDate() function will return the date of the event
 * 
 * format() function provides a way to translate the information of the event
 *   and add it to a single string.
 * 
 */
#ifndef EVENT_H
#define EVENT_H


#include "Date.h"


class Event
{
  public:
    Event(string="Default",int=0);
    virtual ~Event();
    void  setDate(int=0, int=0, int=0, int=0, int=0);
    Date& getDate();
    void  format(string&);
    void  print();
    int   getPriority();
    virtual bool operator<(Event*)=0;
  protected:
    string name;
    Date   date;
    int  priority;
};

#endif
