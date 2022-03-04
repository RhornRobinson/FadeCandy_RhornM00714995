import opc
import time
import colorsys
import random
from time import sleep


leds_colour = [(0,0,0)]*360 #white
led = [(0,0,0)]*360


colour = []
client = opc.Client('localhost:7890')
client.put_pixels(leds_colour)
client.put_pixels(leds_colour)      
#while led<60:
 #   leds_colour[led] = (0,0,255) #row 1 - 0-60
  #  leds_colour[led+60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
   # leds_colour[led+120] = (0,0,255)
    #leds_colour[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
   # leds_colour[led+240] = (0,0,255)
   # leds_colour[led+300] = (0,0,255)
   # client.put_pixels(leds_colour)
   # time.sleep(.1)
   # led = led + 1
   # for led in range (0,0,360):
   #     leds_colour = [(0,0,0)]*360;


def func1 ():
    rand_colour = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    WrenchBackground = [0,1,2,3,4,5,6,7,8,9,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,
                        164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,289,290,291,292,293,294,
                        295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,348,349,350,351,352,353,354,355,356,357,358,359]
    Wrench = [12,13,14,15,16,43,44,45,46,47,71,72,73,74,75,76,77,78,101,102,103,104,105,106,107,108,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,251,252,253,254,255,256,257,258,281,282,283,284,285,286,287,288,312,313,314,315,316,343,344,345,346,347]  
#    for i in WrenchBackground:
#        leds[i] = (0,0,0)
#        client.put_pixels(leds)
#        sleep(.01)
#    for i in Wrench:
#        leds[i] = (0,255,255)
#        client.put_pixels(leds)
#        sleep(.01)
#    for i in Wrench:
#        leds[i] = (rand_colour)
#        client.put_pixels(leds)
#        sleep(.01)
    led = 12
    while True:                         #do this forever:
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for led in range(1):
            leds = [(0,0,0)]*360  #white  #set everything white,
            #rand_color = (random.randint(rand_color[0]-50, rand_color[0]+50),random.randint(rand_color[1]-50, rand_color[1]+50),random.randint(rand_color[2]-20, rand_color[2]+20)) 
            leds[led-12] =rand_color
            leds[led-13] =rand_color
            leds[led-14] =rand_color
            leds[led-15] =rand_color
            leds[led-16] =rand_color
            leds[led-43] =rand_color
            leds[led-44] =rand_color
            leds[led-45] =rand_color
            leds[led-46] =rand_color
            leds[led-47] =rand_color
            leds[led-71] =rand_color
            leds[led-72] =rand_color
            leds[led-73] =rand_color
            leds[led-74] =rand_color
            leds[led-75] =rand_color
            leds[led-76] =rand_color
            leds[led-77] =rand_color
            leds[led-78] =rand_color
            leds[led-101] =rand_color
            leds[led-102] =rand_color
            leds[led-103] =rand_color
            leds[led-104] =rand_color
            leds[led-105] =rand_color
            leds[led-106] =rand_color
            leds[led-107] =rand_color
            leds[led-108] =rand_color
            leds[led-137] =rand_color
            leds[led-138] =rand_color
            leds[led-139] =rand_color
            leds[led-140] =rand_color
            leds[led-141] =rand_color
            leds[led-142] =rand_color
            leds[led-143] =rand_color
            leds[led-144] =rand_color
            leds[led-145] =rand_color
            leds[led-146] =rand_color
            leds[led-147] =rand_color
            leds[led-148] =rand_color
            leds[led-149] =rand_color
            leds[led-150] =rand_color
            leds[led-151] =rand_color
            leds[led-152] =rand_color
            leds[led-153] =rand_color
            leds[led-154] =rand_color
            leds[led-155] =rand_color
            leds[led-156] =rand_color
            leds[led-157] =rand_color
            leds[led-158] =rand_color
            leds[led-159] =rand_color
            leds[led-160] =rand_color
            leds[led-161] =rand_color
            leds[led-162] =rand_color
            leds[led-163] =rand_color
            leds[led-197] =rand_color
            leds[led-198] =rand_color
            leds[led-199] =rand_color
            leds[led-200] =rand_color
            leds[led-201] =rand_color
            leds[led-202] =rand_color
            leds[led-203] =rand_color
            leds[led-204] =rand_color
            leds[led-205] =rand_color
            leds[led-206] =rand_color
            leds[led-207] =rand_color
            leds[led-208] =rand_color
            leds[led-209] =rand_color
            leds[led-210] =rand_color
            leds[led-211] =rand_color
            leds[led-212] =rand_color
            leds[led-213] =rand_color
            leds[led-214] =rand_color
            leds[led-215] =rand_color
            leds[led-216] =rand_color
            leds[led-217] =rand_color
            leds[led-218] =rand_color
            leds[led-219] =rand_color
            leds[led-220] =rand_color
            leds[led-221] =rand_color
            leds[led-222] =rand_color
            leds[led-223] =rand_color
            leds[led-251] =rand_color
            leds[led-252] =rand_color
            leds[led-253] =rand_color
            leds[led-254] =rand_color
            leds[led-255] =rand_color
            leds[led-256] =rand_color
            leds[led-257] =rand_color
            leds[led-258] =rand_color
            leds[led-281] =rand_color
            leds[led-282] =rand_color
            leds[led-283] =rand_color
            leds[led-284] =rand_color
            leds[led-285] =rand_color
            leds[led-286] =rand_color
            leds[led-287] =rand_color
            leds[led-288] =rand_color
            leds[led-312] =rand_color
            leds[led-313] =rand_color
            leds[led-314] =rand_color
            leds[led-315] =rand_color
            leds[led-316] =rand_color
            leds[led-343] =rand_color
            leds[led-344] =rand_color
            leds[led-345] =rand_color
            leds[led-346] =rand_color
            leds[led-347] =rand_color
            
            if led == 347:              #if we reach the end go back;
                led = 12
            client.put_pixels(leds)     #place the latest frame on screen.
            time.sleep(0.1) 
            
        

#-----------Name Lexus ----------------------
#  Letter  L
#    leds_colour[0]=(0,0,0);        leds_colour[1]=(255,255,255);          leds_colour[9,15]=(255,255,255);
#    leds_colour[2,8]=(0,0,0);      leds_colour[17]=(255,255,255);         leds_colour[22]=(255,255,255);
#   leds_colour[15,16]=(0,0,0);    leds_colour[25]=(255,255,255);         leds_colour[30]=(255,255,255);    
#    leds_colour[18,21]=(0,0,0);    leds_colour[33,38]=(255,255,255);      leds_colour[23,24]=(0,0,0);
#    leds_colour[26,29]=(0,0,0);    leds_colour[31,32]=(0,0,0);

#client.put_pixels(leds_colour)
#time.sleep(.1)
#led = led + 1



while True:
    value = input ( ''' RHORN'S CAR SHOWROOM
                \t To pick a car type the corresponding number of your choice and press Enter.
                \t 1. Mercedes
                \t 2. Lexus
                \t 3. Chevrolet
                \t 4. Exit
                 ''')
    
    if value.isdigit() == True: # .isdigit()
        choice = int(value)
        if choice == 1 :
            func1()
        elif choice ==2 :
            func2()
        elif choice ==3 :
            func3()
        elif choice ==4 :
            print (" You have now EXITED the online showroom.    Thank You")
            break
        else:
            print("Sorry this option is incorrect, Please enter a number from the list of cars:")
        if value := chr:
            print (" Please enter a number from 1 to 3.")
            

