import opc
from time import sleep
import colorsys
import time
import random
import winsound
#import gui
led = 0


leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


def func1 ():
##--------------------buliding wrench -------------------------
    led = 0
    while led<60:
        for leds in range (29):
            leds = [(0,0,0)]*360
            leds[0+led] = (219,226,223)
            leds[60+led] = (219,226,223)
            leds[120+led] = (219,226,223)
            leds[180+led] = (219,226,223)
            leds[240+led] = (219,226,223)
            leds[300+led] = (219,226,223)
            client.put_pixels(leds)
            time.sleep(0.1)
            led=led+1
        while True:
            for leds in range(29):
                leds = [(0,0,0)]*360
                leds[59-led] = (219,226,223)
                leds[119-led] = (219,226,223)
                leds[179-led] = (219,226,223)
                leds[239-led] = (219,226,223)
                leds[299-led] = (219,226,223)
                leds[359-led] = (219,226,223)
                client.put_pixels(leds)
                time.sleep(0.1)
                led=led-1
       
    
           
            
       
                   
            
                    
while True:
    value = input ( ''' RHORN'S CAR SHOWROOM
                \t To pick a car option type the number of your choice and press Enter.
                \t 1. Mercedes
                \t 2. Lexus
                \t 3. Chevrolet
                \t 4. Exit
                 ''')
    
    if value.isdigit() == True: # .isdigit()
        choice = int(value)
        if choice == 1 :   # Run animations for Mercedes
            func1()
        elif choice ==2 :  # Run animations for Lexus
            func2()
        elif choice ==3 :  # Run animations for Chevrolet
            func3()
        elif choice ==4 :  # Display text to exit showroom
            print (" You have now EXITED the online showroom...Thank You")
            break
        else:
            print("Invalid input, please provide an number from the list of cars above:")
    else:
        value=input("Invalid input, please provide a number from 1 to 3.")
        break
