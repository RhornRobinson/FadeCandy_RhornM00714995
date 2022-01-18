import opc
from time import sleep
import colorsys
import time
import random



leds = [(255,255,255)]*360   # list of 360 tuples, each containing R,G,B values.

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def func1 ():
    print ( " Mercedes")
    
def func2 ():
    print (" Lexus")


def func3 ():
    print (" Chevrolet")
        


    
while True:
    value = input ( ''' Welcome to The Car Showroom. Pick a car option below: 
                \t Type the number of your choice and press Enter.
                \t 1. Mercedes
                \t 2. Lexus
                \t 3. Chevrolet
                 ''')
    choice = int(value)
    if value.isdigit() == True: # .isdigit() 
        if choice == 1 :
            func1()
        elif choice ==2 :
            func2()
        elif choice ==3 :
            func3()           
        else:
            print("Invalid input, please provide an number from the list of cars above:")
    else:
        print("Invalid input, please provide an number.")
        break

