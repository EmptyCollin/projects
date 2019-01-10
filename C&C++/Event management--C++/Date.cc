#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

#include "Date.h"

Date::Date(int d, int m, int y, int h, int min)
{
  set(d, m, y, h, min);
}

Date::~Date()
{
}

void Date::set(int d, int m, int y, int h, int min)
{
  year  = ( ( y > 0) ? y : 0 );
  month = ( ( m > 0 && m <= 12) ? m : 0 );
  day   = ( ( d > 0 && d <= lastDayInMonth() ) ? d : 0 );
  time.set(h, min, 0);
}

bool Date::operator<(Date& d)
{
  if (year < d.year)
    return true;
  else if (year > d.year)
    return false;
  else if (month < d.month)
    return true;
  else if (month > d.month)
    return false;
  else if (day < d.day)
    return true;
  else if (day > d.day)
    return false;
  else 
    return time<(d.time);
}

void Date::printShort()
{
  cout<<setfill('0')<<setw(2)<<day<<"/"
      <<setfill('0')<<setw(2)<<month<<"/"
      <<setfill('0')<<setw(4)<<year<<"  ";
  time.print();
}

void Date::printLong() 
{
  cout<<setfill(' ') <<setw(10)<<getMonthStr()<<" "
      <<setfill('0') <<setw(2)<<day<<", "<<setw(4)<<year<<"  ";
  time.print();
}

void Date::format(string& outStr){
    stringstream ss;
    ss<<setfill('0')<<setw(2)<<day<<"/"
      <<setfill('0')<<setw(2)<<month<<"/"
      <<setfill('0')<<setw(4)<<year<<"  ";
    outStr += ss.str();
    time.format(outStr);
}

int Date::lastDayInMonth()
{
  switch(month)
  {
    case 2:
      if (leapYear())
        return 29;
      else
        return 28;
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      return 31;
    default:
      return 30;
  }
}

bool Date::leapYear()
{
  if ( year%400 == 0 ||
       (year%4 == 0 && year%100 != 0) )
    return true;
  else
    return false;
}

string Date::getMonthStr() 
{
  string monthStrings[] = { 
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December" };

  if ( month >= 1 && month <= 12 )
    return monthStrings[month-1];
  else
    return "Unknown";
}

