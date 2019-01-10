/*
 * 
 * Class Time records the time of some special events on a day.
 * 
 * It consist of hour, minutes, and seconds; each attributes can be reseted by
 * calling set() function;
 * 
 * Function lessThan() takes a Time object as parameter and can compare the 
 * time between this Time and the Time passed by parameter.
 * 
 * 
 * format() function takes a reference of a string and add the time with format
 *   of string to it.
 * 
 */

#ifndef TIME_H
#define TIME_H

class Time
{
  public:
    Time(int=0, int=0, int=0);
    void set(int, int, int);
    void print();
    bool operator<(Time&);
    void format(string&);

  private:
    int hours;
    int minutes;
    int seconds;
    int convertToSecs();
};

#endif
