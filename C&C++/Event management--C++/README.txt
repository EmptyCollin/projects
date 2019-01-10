/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                             */
/*  Program:  Simple Event Management System                   */
/*  Author:   Weihang Chen                                     */
/*            101084865                                        */
/*  Date:     03-Dec-2018                                      */
/*                                                             */
/*  Purpose:  Practice the basic skills of OOP                 */
/*            program development.                             */
/*                                                             */
/*  Revisions: 1.5                                             */
/*                                                             */
/*  Addition: The code of this program is based on             */
/*            the code provided by Laurendeau, C..             */
/*                                                             */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                             */
/*  File list:                                                 */
/*              main.c                                         */
/*              Control.h                                      */
/*              Control.cc                                     */
/*              View.h                                         */
/*              View.cc                                        */
/*              Calendar.h                                     */
/*              Calendar.cc                                    */
/*              List.h                                         */
/*              Event.h                                        */
/*              Event.cc                                       */
/*              SchoolEvent.h                                  */
/*              SchoolEvent.cc                                 */
/*              WorkEvent.h                                    */
/*              WorkEvent.cc                                   */
/*              Date.h                                         */
/*              Date.cc                                        */
/*              Time.h                                         */
/*              Time.cc                                        */
/*              Array.h                                        */
/*              Array.o                                        */
/*              EventServer.h                                  */
/*              EventServer.o                                  */
/*              Makefile                                       */
/*              in.txt                                         */
/*              README.txt                                     */
/*                                                             */
/*                                                             */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                             */
/*  Compilation command:                                       */
/*                                                             */
/*                              make                           */
/*                                                             */
/*  Launching command:                                         */
/*                                                             */
/*       (with pipelining)      ./cal<in.txt                   */
/*                                                             */
/*       (with pipelining and valgrind)                        */
/*                              valgrind ./cal<in.txt          */
/*                                                             */
/*       (without pipelining)   ./cal                          */
/*                                                             */
/*                              In this case, make a selection */
/*                              first and type in the          */
/*                              corresponding number in the    */
/*                              shell.                         */
/*                                                             */
/*                              1 to add an event into calendar*/
/*                                   and type in the detail    */
/*                                   information then          */
/*                                                             */
/*                              0 to terminate the program     */
/*                                   and the calendar you had  */
/*                                   built would be printed    */
/*                                   on screen                 */
/*                                                             */
/*                              any others selection are       */
/*                                   illegal, you need to retry*/
/*                                   to continue or to exit.   */
/*                                                             */
/*                                                             */
/*                              If you want to add event(s)    */
/*                                   into calendar(s), you need*/
/*                                   to provide formalized     */
/*                                   information based on the  */
/*                                   hints. Alhough the basic  */
/*                                   error checking has been   */
/*                                   done, the information with*/
/*                                   incorrect data type may   */
/*                                   cause unexpected errors.  */
/*                                                             */
/*                                                             */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
