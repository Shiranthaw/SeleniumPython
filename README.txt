
Automation Exercise – Trip Planner Installation Instructions (ver 1.0)
======================================================================
Please read and follow these instructions to install and run the automation solution.

* ASSUMPTIONS:
Python (version 3.4.0) and Selenium (version 4.3.4) are installed & configured in the PATH.
Firefox browser is installed
Windows 10 Operating System
Firefox geckodriver.exe driver is installed. It is advisable to place geckodriver.exe in a central location and add to the system PATH. If geckodriver.exe is not in your system, please download and install from: https://github.com/mozilla/geckodriver/releases
  

* This package consists of following files:
	README.txt				: Installation instructions (this file)
	TripPlanner_UnitTest.py	: Python code
	
* Make sure to configure Python, Selenium and geckodriver as per the assumptions

* To run the solution in command line:
	Open a command prompt (type "cmd" in Windows serch box)
	Run the solution as:  "python TripPlanner_UnitTest.py"
	It will automatically open a Firefox browser and run the test. Upon finishing the test, the browser will automatically close.
	The output similar to below will be shown in the command prompt.
	
				4 Trips found From: North Sydney Station, North Sydney TO: Wynyard Station, Sydney

				Trip number 1
				Departure Time:  22:25
				Arrival Time  :  22:31
				=======================
				Trip number 2
				Departure Time:  22:33
				Arrival Time  :  22:39
				=======================
				Trip number 3
				Departure Time:  22:40
				Arrival Time  :  22:46
				=======================
				Trip number 4
				Departure Time:  22:48
				Arrival Time  :  22:54
				=======================
				.
				----------------------------------------------------------------------
				Ran 1 test in 21.170s

				OK
				
