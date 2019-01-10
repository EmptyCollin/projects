/******************************************************************************/
/*                                                                            */
/*  purpose:                                                                  */
/*                                                                            */
/*          practices of operating of morph and process spawn in C.           */
/*                                                                            */
/*          practices of the usage of signal() and SIGNUM in C                */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*  developer:                                                                */
/*                                                                            */
/*          Weihang Chen                                                      */
/*                                                                            */
/*  Date:                                                                     */
/*          07/12/2018                                                        */
/*                                                                            */
/*                                                                            */
/*  addition:                                                                 */
/*                                                                            */
/*          the basic code is provided by Pro. Nussbaum, D.                   */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*  program organization:                                                     */
/*                                                                            */
/*          isPrime                                                           */
/*          isPrime.c  -  The basic program provides the function to test     */
/*                             whether the input number is prime or not       */
/*                                                                            */
/*          create                                                            */
/*          createBinary.c - The program provides the function to create a    */
/*                              binary file with command line parameters      */
/*                                                                            */
/*                                                                            */
/*          prime.txt                                                         */
/*          prime.bin   -  the file can be used to test the program           */
/*          Makefile1                                                         */
/*          singelMorph                                                       */
/*          singleMorph.c - This program provides the function to read the    */
/*                             first number in the file provided and          */
/*                             determine whether it is a prime or not         */
/*                                                                            */
/*          Makefile2                                                         */
/*          singleSpawn                                                       */
/*          singleSpawn.c - This program offers the function to read the first*/
/*                             number in the binary file provided and spawn   */
/*                             a child process to test it                     */
/*                                                                            */
/*          Makefile3                                                         */
/*          multiSpawn                                                        */
/*          multiSpawn.c -  This program offers the function to read all      */
/*                              available numbers in the file provided and    */
/*                              test them whether are prime or not            */
/*                                                                            */
/*          Makefile4                                                         */
/*          multiSpawnSignal                                                  */
/*          multiSpawnSignal.c - The enhance version of mutiSpawn that show   */
/*                                  the state of each child processed         */
/*                                                                            */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*  compile:                                                                  */
/*                                                                            */
/*          1.run a shell and change the directory into the root of program   */
/*                                                                            */
/*          2.compile the program by typing in:                               */
/*                                                                            */
/*                                              make -f Makefile1             */
/*                                              make -f Makefile2             */
/*                                              make -f Makefile3             */
/*                                              make -f Makefile4             */
/*          3.to create the test file(if necessary):                          */
/*                                                                            */
/*                                              gcc -o create createBinary    */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*  announcement:                                                             */
/*                                                                            */
/*          1. this program should be compiled and run on VM                  */
/*                                                                            */
/*          2. make sure to run the make file before testing the program      */
/*                 if any files have been changed                             */
/*                                                                            */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*  to test:                                                                  */
/*                                                                            */
/*         by typing in:                                                      */
/*                                                                            */
/*                    ./singleMorph prime.bin    ---to test the singleMorph   */
/*                                                                            */
/*                    ./singleSpawn prime.bin    ---to test the singleSpawn   */
/*                                                                            */
/*                    ./multiSpawn prime.bin     ---to test the multiSpawn    */
/*                                                                            */
/*                    ./multiSpawnSignal prime.bin  ---to test the            */
/*                                                        multiSpawnSignal    */
/*                                                                            */
/*         The program will automatically run and print results               */
/*                                                                            */
/*         by typing in:                                                      */
/*                     ./create [filename] [variables]  ---to create test file*/
/*                                                            with binary form*/
/*                                                                            */
/*         for examle:                                                        */
/*                    ./create test.bin 1 2 4 6 13 18                         */
/*                         and replace the prime.bin with test.bin in previous*/
/*                         test command                                       */
/******************************************************************************/
