/*
 * Control class takes on the main functions of the program and separates user 
 *   interaction from data processing.
 * 
 * outStr: a single string storing the information of the calendar
 * 
 * selection: the selection of user make
 * 
 * launch(): executing the program until the user opts out
 * 
 */


#ifndef CONTROL_H
#define CONTROL_H

#include <string>
#include "View.h"
#include "Calendar.h"
#include "Array.h"
#include "EventServer.h"


class Control
{
  public:
    Control();
    ~Control();
    void launch();
    

  private:
    View view;
    Calendar school;
    Calendar work;
    EventServer server;
};

#endif
