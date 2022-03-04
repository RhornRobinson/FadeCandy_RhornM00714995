# FadeCandy_RhornM00714995
README
RHORN’S AUTOMOTIVE DEALERSHIP
The aim of this dealership is to not only sell you a car or service your vehicle but also help educate you on the origins and development of your vehicle. 
Majority of the times, individuals purchase a vehicle with no prior knowledge of the car or the country it originated from.
This is a more personal and involved service where you get to experience and be part of the entire process. At our dealership, we will take you through 
a little journey based upon the car of your choice.
Firstly, you will be presented with 5 options.

Option 1- Mercedes. Here we will take you through your car of your choice and a little about the badge. We will enlighten you on the country the Mercedes car originated
from which is Germany and finally present your car.

Option 2- Lexus.  In this option, jut like above we will take you through the Lexus car and the badge followed by the country it originated from which is Japan.
Afterwards your Lexus car will be presented to you.

Option 3- Chevrolet. Again, it’s a presentation of the car and its badge followed by the country it came from. In this case it is the USA. Then the car will be shown to you.

Option 4- This is the option for service department. Here you can visualise the service being carried out on your car. Any faults, tyre changes or results from the service
will be displayed.

Option 5- Exit. This option exits the online/virtual showroom.

RUNNING THE SHOWROOM:
After all the software has been successfully installed, we run python and upload the code which was downloaded from the link above followed by the LED simulator. 
After running python, you should be greeted with an introductory menu with 5 options.

RHORN'S AUTOMOTIVE DEALERSHIP
                	 To pick a car option type the number of your choice and press Enter.
                	 1. Mercedes
                	 2. Lexus
                	 3. Chevrolet
                	 4. Service
                	 5. Exit
After being presented with this screen you type the number which corresponds to the option you would like to select. For example, if you would like to choose Lexus,
you type the number 2 then press ENTER. This will then run you through the series of animations which are programmed under the Lexus. When the animations are complete you 
will be redirected to the options menu to select another option or EXIT the menu. 
To exit the menu, just enter the number 5 and press ENTER. This will log you out of the showroom.     
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
REQUIREMENTS
To run the online/virtual showroom you need to have the following:
1.	Python Software
This is the program which will enable you to run the code. This can be downloaded here; https://www.python.org/downloads/

2.	The LED simulator which is needed to observe the animations. The simulator provided has 360 LEDs arranged in a grid pattern of 6 rows with 60 LEDs each.
 The simulator together with the opc file can be found in folder labelled “Files needed For FadeCandy”

3.	Code The code can be copied from GitHub file labelled “Rhorn’s Automotive Showroom”




ABOUT FADECANDY SIMULATOR
 The simulator provided has 360 LEDs arranged in a grid pattern of 6 rows with 60 LEDs each.
Explanation of some of the basic commands necessary in Fadecandy code:

opc. Client() - sets up a client object that will establish communication between Python and a fadecandy server.
Required argument: an IP or localhost with correct port for the server.

. put_pixels(list) - places a list of tuples with rgb values to the fadecandy server to be displayed.
Format: [(R_value, G_value, B_value)] Each tuple element in the list represents a single led.

To connect to the simulator, use localhost with port 7890 when setting up your fadecandy instance in Python: 
client = opc.Client('localhost:7890')

When not using a loop, perform .put_pixels) twice to avoid interpolation issues
client.put_pixels(list)
client.put_pixels(list)



