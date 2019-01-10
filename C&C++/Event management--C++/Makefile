OPT = -Wall

cal:	main.o Date.o Time.o Event.o Calendar.o List.h View.o Control.o WorkEvent.o SchoolEvent.o Array.o EventServer.o
	g++ $(OPT) -o cal main.o Date.o Time.o Event.o Calendar.o List.h View.o Control.o WorkEvent.o SchoolEvent.o Array.o EventServer.o

main.o:	main.cc Control.h
	g++ $(OPT) -c main.cc
	
Control.o: Control.cc Control.h View.h Calendar.h
	g++ $(OPT) -c Control.cc
	
View.o: View.cc View.h
	g++ $(OPT) -c View.cc
	
Calendar.o: Calendar.cc Calendar.h Event.h List.h
	g++ $(OPT) -c Calendar.cc
		
Event.o:Event.cc Event.h Date.h
	g++ $(OPT) -c Event.cc
	
SchoolEvent.o:SchoolEvent.cc SchoolEvent.h Event.h Date.h
	g++ $(OPT) -c SchoolEvent.cc
	
WorkEvent.o:WorkEvent.cc WorkEvent.h Event.h Date.h
	g++ $(OPT) -c WorkEvent.cc	
	
Date.o:	Date.cc Date.h Time.h
	g++ $(OPT) -c Date.cc

Time.o:	Time.cc Time.h
	g++ $(OPT) -c Time.cc

clean:
	rm -f cal
	rm -f `ls *.o|egrep -v '(Array.o|EventServer.o)'`
