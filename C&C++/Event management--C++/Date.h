/*
 *
 * Class Date is used to store the date of some special event.
 *
 * It contains attributes of year, month, and day, as well as a Time object
 *   which stores the hour, minutes, and seconds.
 *
 * lessThan() function enable a date to compare with another date; if it is 
 *   earlier than another date, the value of return will be ture. Otherwise 
 *   it will be false;
 * 
 * format() function takes a reference of a string and add the date with format
 *   of string to it.
 * 
 */


#ifndef DATE_H
#define DATE_H

#include "Time.h"

class Date
{
  public:
    Date(int=0, int=0, int=2000, int=0, int=0);
    ~Date();
    void set(int, int, int, int, int);
    bool operator<(Date&);
    void format(string&);
    void printShort();
    void printLong();

  private:
    int  day;
    int  month;
    int  year;
    Time time;
    int  lastDayInMonth();
    bool leapYear();
    string getMonthStr();
};

#endif
