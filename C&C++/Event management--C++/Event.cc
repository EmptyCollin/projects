#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

#include "Event.h"

Event::Event(string n, int p)
{
  name = n;
  priority = p;
}

Event::~Event(){}

void Event::setDate(int y, int m, int d, int h, int min)
{
  date.set(y, m, d, h, min);
}

Date& Event::getDate()
{
  return date;
}

int Event::getPriority()
{
  return priority;
}

void Event::format(string& outStr)
{
  stringstream ss;
  ss << setfill(' ') << setw(20) << name << setw(16)<<"priority = "<<setw(4)<<priority<<setw(8);
  outStr += ss.str();
  date.format(outStr);
}

void Event::print()
{
    cout<<setfill(' ') << setw(20) << name << setw(16)<<"priority = "<<setw(4)<<priority<<setw(8);
    date.printLong();
}

