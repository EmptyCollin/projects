#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

#include "View.h"

void View::displayMenu(int& selection)
{
  int numOptions = 1;
  int theSelection  = -1;

  cout << endl;
  cout << "(1) Add event" << endl;
  cout << "(0) Exit" << endl;

  while (theSelection < 0 || theSelection > numOptions) {
    cout << "Enter your selection: ";
    cin  >> theSelection;
  }
  selection = theSelection;
}


void View::readEvent(string& eventName,int& day,int& month,int& year,int& hour,int& minute,int& priority){
    cout << "Event name:";
    cin >> eventName;
    cout << "day:   ";
    cin  >> day;
    cout << "month: ";
    cin  >> month;
    cout << "year:  ";
    cin  >> year;
    cout << "hour:  ";
    cin  >> hour;
    cout << "minute:  ";
    cin  >> minute;
    cout << "priority:";
    cin  >> priority;
}

void View::print(Calendar& calendar) const
{
    calendar.print();
}


void View::printCalender(string outStr) const
{
  cout << outStr;
}

void View::eventType(string& type)
{
    type = "";
    cout << "Is this a School Event(S) or Work Event(W)? ";
    while(type.substr(0,1) != "W" &&
          type.substr(0,1) != "w" &&
          type.substr(0,1) != "S" &&
          type.substr(0,1) != "s"){
        cin  >> type;
    }
    type = type.substr(0,1);

}


