import opc
from time import sleep
import colorsys
import time
import random
import winsound
#inport gui



leds = [(255,255,255)]*360   # list of 360 tuples, each containing R,G,B values.
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []

client = opc.Client('localhost:7890')
client.put_pixels(leds)


def func1 ():




    

    print (  " Made in GERMANY ")
    
    
def func2 ():
    print (" LEXUS ")
    rand_colour = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    row1 = [1,9,10,11,12,13,14,17,22,25,30,33,34,35,36,37,38]
    row2 = [1,9,18,21,25,30,33]
    row3 = [1,9,10,11,19,20,25,30,34,35]
    row4 = [1,9,18,21,25,30,38]
    row5 = [1,9,18,21,25,30,38]
    row6 = [1,2,3,4,5,6,9,10,11,12,13,14,17,22,25,26,27,28,29,30,33,34,35,36,37,38]

for i in row1:
    leds[i] = (120,120,120)
    client.put_pixel(leds)

for i in row2:
    leds[i] = (120,120,120)
    client.put_pixel(leds)

for i in row3:
    leds[i] = (120,120,120)
    client.put_pixel(leds)

for i in row4:
    leds[i] = (120,120,120)
    client.put_pixel(leds)

for i in row5:
    leds[i] = (120,120,120)
    client.put_pixel(leds)

for i in row6:
    leds[i] = (120,120,120)
    client.put_pixel(leds)
    

    print (" Made in JAPAN ")
    


def func3 ():
    print (" CHEVROLET")

    print (" Made in USA ")

#for leds in row (1) :
#    for L in range (
    
        


    
while True:
    value = input ( ''' RHORN'S CAR SHOWROOM
                \t To pick a car option type the number of your choice and press Enter.
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
        print("Invalid input, please provide a number from 1 to 3.")
        break

