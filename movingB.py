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

##--------------------MOVING B ANIMATION --------------------------------
    led = 0
    while led<60:                 
        for led in range(52):   
            leds = [(0,0,0)]*360    
            leds[351-led] = (255,0,0)
            leds[351-led+2] = (255,0,0)
            leds[351-led+4] = (255,0,0)
            leds[291-led] = (255,0,0)
            leds[291-led+6] = (255,0,0)
            leds[231-led] = (255,0,0)
            leds[231-led+4] = (255,0,0)
            leds[231-led+3] = (255,0,0)
            leds[231-led+2] = (255,0,0)
            leds[171-led] = (255,0,0)
            leds[171-led+6] = (255,0,0)
            leds[111-led] = (255,0,0)
            leds[111-led+2] = (255,0,0)
            leds[111-led+4] = (255,0,0)
            client.put_pixels(leds)
            time.sleep(.1)
        break

    client.put_pixels(leds)
##--------------------- MOVING WHEEL ANIMATION ------------------------
    led = 0
    while led<50:                 
        for led in range(52):   
            leds = [(0,0,0)]*360    
            leds[2+led] = (255,0,0)
            leds[2+led+1] = (255,0,0)
            leds[3+led+1] = (255,0,0)
            leds[4+led+1] = (255,0,0)
            leds[5+led+1] = (255,0,0)
            leds[60+led+1] = (255,0,0)
            leds[61+led+1] = (255,0,0)
            leds[65+led+1] = (255,0,0)
            leds[66+led+1] = (255,0,0)
            leds[119+led+1] = (255,0,0)
            leds[120+led+1] = (255,0,0)
            leds[126+led+1] = (255,0,0)
            leds[127+led+1] = (255,0,0)
            leds[179+led+1] = (255,0,0)
            leds[180+led+1] = (255,0,0)
            leds[186+led+1] = (255,0,0)
            leds[187+led+1] = (255,0,0)
            leds[240+led+1] = (255,0,0)
            leds[241+led+1] = (255,0,0)
            leds[245+led+1] = (255,0,0)
            leds[246+led+1] = (255,0,0)
            leds[301+led+1] = (255,0,0)
            leds[302+led+1] = (255,0,0)
            leds[303+led+1] = (255,0,0)
            leds[304+led+1] = (255,0,0)
            leds[305+led+1] = (255,0,0)
            client.put_pixels(leds)
            time.sleep(0.1)
    ##----------------------- DELETES WHEEL ------------------------------------
    led = 51
    while led<60:
        for rows in range (6):
            leds [led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1

    ##----------------------- MOVING CAR ANIMATION -----------------------------------
    led = 0
    while led<27:                 
        for led in range(28):   
            leds = [(0,0,0)]*360
            leds[6+led+1] = (153,0,26)     #--------
            leds[7+led+1] = (153,0,26)     #
            leds[8+led+1] = (153,0,26)     #
            leds[9+led+1] = (153,0,26)     #
            leds[10+led+1] = (153,0,26)    #
            leds[11+led+1] = (153,0,26)    #
            leds[12+led+1] = (153,0,26)    #
            leds[13+led+1] = (153,0,26)    #CAR BODY
            leds[14+led+1] = (153,0,26)    #
            leds[15+led+1] = (153,0,26)    #
            leds[16+led+1] = (153,0,26)    #
            leds[17+led+1] = (153,0,26)    #
            leds[18+led+1] = (153,0,26)    #
            leds[19+led+1] = (153,0,26)    #
            leds[66+led+1] = (153,0,26)    #---------
            leds[67+led+1] = (255,255,77)  #
            leds[68+led+1] = (255,255,77)  #CAR WINDOW
            leds[69+led+1] = (255,255,77)  #
            leds[70+led+1] = (255,255,77)  #
            leds[71+led+1] = (255,255,77)  #---------
            leds[72+led+1] = (153,0,26)    #CAR BODY
            leds[73+led+1] = (153,0,26)    #---------
            leds[74+led+1] = (255,255,77)  #
            leds[75+led+1] = (255,255,77)  #CAR WINDOW
            leds[76+led+1] = (255,255,77)  #
            leds[77+led+1] = (255,255,77)  #
            leds[78+led+1] = (255,255,77)  #---------
            leds[79+led+1] = (153,0,26)    #CAR BODY
            leds[80+led+1] = (153,0,26)    #---------
            leds[89+led+1] = (255,255,25)  #---------
            leds[90+led+1] = (255,255,25)  #LIGHT BEAM
            leds[91+led+1] = (255,255,25)  #---------
            leds[120+led+1] = (153,0,26)   #
            leds[121+led+1] = (153,0,26)   #
            leds[122+led+1] = (153,0,26)   #CAR BODY
            leds[123+led+1] = (153,0,26)   #
            leds[124+led+1] = (153,0,26)   #
            leds[125+led+1] = (153,0,26)   # 
            leds[126+led+1] = (153,0,26)   #---------
            leds[127+led+1] = (255,255,77) #
            leds[128+led+1] = (255,255,77) #
            leds[129+led+1] = (255,255,77) #WINDOW
            leds[130+led+1] = (255,255,77) #
            leds[131+led+1] = (255,255,77) #--------
            leds[132+led+1] = (153,0,26)   #CAR BODY
            leds[133+led+1] = (153,0,26)   #--------
            leds[134+led+1] = (255,255,77) #
            leds[135+led+1] = (255,255,77) #
            leds[136+led+1] = (255,255,77) #CAR WINDOW
            leds[137+led+1] = (255,255,77) #
            leds[138+led+1] = (255,255,77) #
            leds[139+led+1] = (255,255,77) #--------
            leds[140+led+1] = (153,0,26)   #
            leds[141+led+1] = (153,0,26)   #CAR BODY
            leds[142+led+1] = (153,0,26)   #--------
            leds[148+led+1] = (255,255,25) #LIGHTBEAM
            leds[149+led+1] = (255,255,25) #--------
            leds[150+led+1] = (255,255,77) #WINDOW
            leds[151+led+1] = (255,255,77) #--------
            leds[180+led+1] = (153,0,26)   #
            leds[181+led+1] = (153,0,26)   #
            leds[182+led+1] = (153,0,26)   #
            leds[183+led+1] = (153,0,26)   #
            leds[184+led+1] = (153,0,26)   #
            leds[185+led+1] = (153,0,26)   #
            leds[186+led+1] = (153,0,26)   #
            leds[187+led+1] = (153,0,26)   #
            leds[188+led+1] = (153,0,26)   #
            leds[189+led+1] = (153,0,26)   #CAR BODY
            leds[190+led+1] = (153,0,26)   #
            leds[191+led+1] = (153,0,26)   #
            leds[192+led+1] = (153,0,26)   #
            leds[193+led+1] = (153,0,26)   #
            leds[194+led+1] = (153,0,26)   #
            leds[195+led+1] = (153,0,26)   #
            leds[196+led+1] = (153,0,26)   #
            leds[197+led+1] = (153,0,26)   # 
            leds[198+led+1] = (153,0,26)   #
            leds[199+led+1] = (153,0,26)   # 
            leds[200+led+1] = (153,0,26)   #
            leds[201+led+1] = (153,0,26)   #
            leds[202+led+1] = (153,0,26)   #--------
            leds[203+led+1] = (255,255,77) #WINDOW
            leds[205+led+1] = (255,255,25) #------
            leds[206+led+1] = (255,255,25) #
            leds[207+led+1] = (255,255,25) #LIGHT BEAM
            leds[208+led+1] = (255,255,25) #
            leds[209+led+1] = (255,255,25) #
            leds[210+led+1] = (255,255,25) #
            leds[211+led+1] = (255,255,25) #------
            leds[240+led+1] = (153,0,26)   # 
            leds[241+led+1] = (153,0,26)   #CAR BODY 
            leds[242+led+1] = (153,0,26)   # 
            leds[243+led+1] = (153,0,26)   #------
            leds[244+led+1] = (131,152,163)#
            leds[245+led+1] = (131,152,163)#WHEEL
            leds[246+led+1] = (131,152,163)#-----
            leds[247+led+1] = (153,0,26)   # 
            leds[248+led+1] = (153,0,26)   # 
            leds[249+led+1] = (153,0,26)   # 
            leds[250+led+1] = (153,0,26)   #CAR BODY
            leds[251+led+1] = (153,0,26)   # 
            leds[252+led+1] = (153,0,26)   # 
            leds[253+led+1] = (153,0,26)   # 
            leds[254+led+1] = (153,0,26)   # 
            leds[255+led+1] = (153,0,26)   #-----
            leds[256+led+1] = (131,152,163)# 
            leds[257+led+1] = (131,152,163)#WHEEL
            leds[258+led+1] = (131,152,163)#-----
            leds[259+led+1] = (153,0,26)   # 
            leds[260+led+1] = (153,0,26)   #BODY
            leds[261+led+1] = (153,0,26)   # 
            leds[262+led+1] = (153,0,26)   # 
            leds[263+led+1] = (153,0,26)   #------
            leds[267+led+1] = (255,255,25) # 
            leds[268+led+1] = (255,255,25) # 
            leds[269+led+1] = (255,255,25) #LIGHT BEAM
            leds[270+led+1] = (255,255,25) # 
            leds[271+led+1] = (255,255,25) #-----
            leds[304+led+1] = (131,152,163)# 
            leds[305+led+1] = (131,152,163)# 
            leds[306+led+1] = (131,152,163)#WHEEL
            leds[316+led+1] = (131,152,163)# 
            leds[317+led+1] = (131,152,163)# 
            leds[318+led+1] = (131,152,163)#------
            leds[329+led+1] = (255,255,25) # 
            leds[330+led+1] = (255,255,25) #LIGHT BEAM
            leds[331+led+1] = (255,255,25) #------
            client.put_pixels(leds)
            time.sleep(0.1)

    led = 51
    while led<52:
        for rows in range (6):
            leds [led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1

    led = 0
    while led<60:                 
            for led in range(52):   
                leds = [(0,0,0)]*360    
                leds[351-led] = (255,0,0)
                leds[351-led+2] = (255,0,0)
                leds[351-led+4] = (255,0,0)
                leds[291-led] = (255,0,0)
                leds[291-led+6] = (255,0,0)
                leds[231-led] = (255,0,0)
                leds[231-led+4] = (255,0,0)
                leds[231-led+3] = (255,0,0)
                leds[231-led+2] = (255,0,0)
                leds[171-led] = (255,0,0)
                leds[171-led+6] = (255,0,0)
                leds[111-led] = (255,0,0)
                leds[111-led+2] = (255,0,0)
                leds[111-led+4] = (255,0,0)
                client.put_pixels(leds)
                time.sleep(.1)
            break
        

        
        
def func2 ():

    led = 0
    while led<60:                 
            for led in range(52):   
                leds = [(0,0,0)]*360    
                leds[351-led] = (255,0,0)
                leds[351-led+2] = (255,0,0)
                leds[351-led+4] = (255,0,0)
                leds[291-led] = (255,0,0)
                leds[291-led+6] = (255,0,0)
                leds[231-led] = (255,0,0)
                leds[231-led+4] = (255,0,0)
                leds[231-led+3] = (255,0,0)
                leds[231-led+2] = (255,0,0)
                leds[171-led] = (255,0,0)
                leds[171-led+6] = (255,0,0)
                leds[111-led] = (255,0,0)
                leds[111-led+2] = (255,0,0)
                leds[111-led+4] = (255,0,0)
                client.put_pixels(leds)
                time.sleep(.1)
            break


     
        
    
    
##--------------------------->>>  FUNCTION FOR LEXUS DISPLAYS <<<---------------------------------------------------##
       

    
    


        
 

##------------------------------------------>>  ANIMATIONS FOR CHEVROLET <<---------------------------------------------------------------##
def func3 ():
    
##--------------------MOVING B ANIMATION --------------------------------
    led = 0
    while led<60:                 
        for led in range(52):   
            leds = [(0,0,0)]*360    
            leds[351-led] = (255,0,0)
            leds[351-led+2] = (255,0,0)
            leds[351-led+4] = (255,0,0)
            leds[291-led] = (255,0,0)
            leds[291-led+6] = (255,0,0)
            leds[231-led] = (255,0,0)
            leds[231-led+4] = (255,0,0)
            leds[231-led+3] = (255,0,0)
            leds[231-led+2] = (255,0,0)
            leds[171-led] = (255,0,0)
            leds[171-led+6] = (255,0,0)
            leds[111-led] = (255,0,0)
            leds[111-led+2] = (255,0,0)
            leds[111-led+4] = (255,0,0)
            client.put_pixels(leds)
            time.sleep(.1)
        break

    client.put_pixels(leds)   
        


    
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
