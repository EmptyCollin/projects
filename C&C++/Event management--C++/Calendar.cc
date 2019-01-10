
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

#include "Calendar.h"


Calendar::Calendar(string calendarTitle){
    title = calendarTitle;
}

Calendar::~Calendar(){
}


void Calendar::add(Event* newEvent){
    list.add(newEvent);
}
    

void Calendar::print(){
    cout<< "\n\n"+title + ":\n";
    list.print();
    cout<<"\n";
}

void Calendar::format(string& outStr){
    outStr = "\n\nFormat function:\n"+title + ":\n";
    list.format(outStr);
}


void Calendar::setTitle(string t){
    title = t;
}

void Calendar::copyEvents(Array& arr){
    list.copy(arr);
}

