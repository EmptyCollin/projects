#include <iostream>
#include <iomanip>
using namespace std;
#include "Control.h"


void Control::launch()
{
  Event* event;
  string eventName;
  int day,month,year,hour,minute,priority;
  string eventType;
  int selection = 1;
  string outStr;
  work.setTitle("Work Event");
  school.setTitle("School Event");
  while(selection == 0||selection == 1){
      view.displayMenu(selection);
      if(selection==1){
          view.eventType(eventType);
          view.readEvent(eventName,day,month,year,hour,minute,priority);
          if(eventType == "w" || eventType == "W"){
              event = new WorkEvent(eventName,priority);
              event->setDate(day,month,year,hour,minute);
              work.add(event);
          }else{
              event = new SchoolEvent(eventName,priority);
              event->setDate(day,month,year,hour,minute);
              school.add(event);
          }
          
      }else if(selection==0){
          view.print(school);
          view.print(work);
          break;
    }
  }
}

Control::Control(){
    Array schoolEvents, workEvents;
    server.retrieve(schoolEvents,workEvents);
    for(int i = 0; i < schoolEvents.getSize();i++){
        school.add(schoolEvents.get(i));
    }
    for(int i = 0; i < workEvents.getSize();i++){
        work.add(workEvents.get(i));
    }

}

Control::~Control(){
    Array schoolEvents, workEvents;
    school.copyEvents(schoolEvents);
    work.copyEvents(workEvents);
    server.update(schoolEvents,workEvents);
    
}


