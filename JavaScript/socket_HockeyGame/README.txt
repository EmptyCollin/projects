====================================================================
Assignment3:
	
	Weihang Chen
	101084865
	weihangchen@cmail.carleton.ca

	no partners

====================================================================
Test environment:
	
	node.js:	V8.11.4
	OS:		Window 10

====================================================================
Install:
	
	uncompressing the .zip file in a single folder and make sure 
all the files have been placed in the correct directories.

	file list:	________________________________________________
			|
			|	./
			|		server.js
			|		package-lock.json
			|		README.text
			|
			|		html/
			|			Assignment3.html
			|			hockey.js
			|			favicon.ico
			|		
			|		node_modules/
			|				.
			|				.
			|				.
			|________________________________________________

====================================================================
Launch the server:
	
	starting a shell at the root directory and typing in the command:

		1: npm install socket.io
			-- to install socket moudel
	
		2: node ./server.js

			-- to launch the server

====================================================================
To test:
	
	using a chrome browser to visit the address:

		http://localhost:3000/
	or
		http://localhost:3000/assignment3.html

	There are three pairs of built-in user-password used for test:
		Arbor	123,
    		Bob	456,
    		Cate	789 

	Signing up a new account to test is also supported;

====================================================================
Attention:
	
	1.Make sure to run the server at first then load the webpage.
	
	2.If the server has been restart, refreshing the page before log in is must.
			-- Or the records on client will interrupt the application.

====================================================================
Others:
	Restart function may work incorrectly sometimes. A possible reason is that the confirm
		dialog is not load on the page correctly. Restart the server to fix the problem.