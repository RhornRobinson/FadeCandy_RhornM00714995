import opc
from time import sleep
import colorsys
import time
import random
import winsound
#import gui
led = 0
endpoint1 = 149

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


def func1 ():
##--------------------buliding wrench -------------------------
    led = 0
    while led<15:
        for leds in range (59):
            leds = [(0,0,0)]*360
            leds[179-led] = (219,226,223)
            leds[120+led] = (219,226,223)
            leds[239-led] = (219,226,223)
            leds[180+led] = (219,226,223)
            leds[178-led] = (219,226,223)
            leds[121+led] = (219,226,223)
            leds[238-led] = (219,226,223)
            leds[181+led] = (219,226,223)
        for leds in  range (35):
            leds[177-led] = (201,212,238)
            leds[122+led] = (201,212,238)
            leds[237-led] = (201,212,238)
            leds[182+led] = (201,212,238)
            
            if led == endpoint1: 
                sleep (.1)
            

                        
            time.sleep(.1)
            client.put_pixels(leds)
            led = led + 1 #or reverse if you want
            
##--------------------MERCEDES NAME -------------------------------------
#    led = 0
#    while led<352:
#        for led in range (359):
#            leds = [(0,0,0)]*360
#            leds[0+led] = (255,255,0)
#            leds[1+led] = (255,255,0)
#            leds[60+led+60] = (255,255,0)
#            leds[61+led+60] = (255,255,0)
#            leds[120+led+60] = (255,255,0)
#            leds[121+led+60] = (255,255,0)
#            leds[180+led+60] = (255,255,0)
#            leds[181+led+60] = (255,255,0)
#            client.put_pixels(leds)
#            time.sleep(.1)
#        break

#    client.put_pixels(leds)
            

##--------------------MOVING B ANIMATION --------------------------------
    led = 0
    while led<60:                 
        for led in range(32):   
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
#---------------------M--------------------------
    while True:                         #do this forever:
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for led in range(360):
            leds = [(255,255,255)]*360  #white  #set everything white,
            rand_color = (random.randint(rand_color[0]-50, rand_color[0]+50),random.randint(rand_color[1]-50, rand_color[1]+50),random.randint(rand_color[2]-20, rand_color[2]+20))
            leds[355-led] = rand_color       #set 5 leds another colour, incrementing position each frame
            leds[355-led+1] = rand_color
            leds[355-led+2] = rand_color
            leds[355-led+3] = rand_color
            leds[355-led+4] = rand_color
            if led == 355:              #if we reach the end go back;
                led = 0
            client.put_pixels(leds)     #place the latest frame on screen.
        time.sleep(0.1)            #delay the frame a bit
#-----------------------E------------------------
    led = 0
    while led<7:                 
            for led in range(59):   
                leds = [(0,0,0)]*360    
                leds[10-led-3] = (255,0,0)
                leds[11-led-3] = (255,0,0)
                leds[12-led-3] = (255,0,0)
                leds[13-led-3] = (255,0,0)
                leds[70-led-3] = (255,0,0)
                leds[130-led-3] = (255,0,0)
                leds[131-led-3] = (255,0,0)
                leds[190-led-3] = (255,0,0)
                leds[191-led-3] = (255,0,0)
                leds[250-led-3] = (255,0,0)
                leds[310-led-3] = (255,0,0)
                leds[311-led-3] = (255,0,0)
                leds[312-led-3] = (255,0,0)
                leds[313-led-3] = (255,0,0)
                client.put_pixels(leds)
                time.sleep(.1)
            break
     
        
    
    
##--------------------------->>>  FUNCTION FOR LEXUS DISPLAYS <<<---------------------------------------------------##
       

    
    


        
 

#------------->>  ANIMATIONS FOR FLASHING FAULT SIGNS ( BATTERY & ENGINE WARNING LIGHT <<---------------------------------------------------------------##
def func3 ():
    
##--------------------FLASHING BATTERY ANIMATION --------------------------------
    t = 1
    led = 0
    while t<50:
        rand_color = (random.randint(255,255),random.randint(99,215),random.randint(0,80))
        for led in range(1):   
            leds = [(0,0,0)]*360    
            leds[4-led] = (255,165,0)
            leds[5-led] = (255,165,0)
            leds[11-led] = (255,165,0)
            leds[12-led] = (255,165,0)
            leds[62-led] = (255,165,0)
            leds[63-led] = (255,165,0)
            leds[64-led] = (255,165,0)
            leds[65-led] = (255,165,0)
            leds[66-led] = (255,165,0)
            leds[67-led] = (255,165,0)
            leds[68-led] = (255,165,0)
            leds[69-led] = (255,165,0)
            leds[70-led] = (255,165,0)
            leds[71-led] = (255,165,0)
            leds[72-led] = (255,165,0)
            leds[73-led] = (255,165,0)
            leds[74-led] = (255,165,0)
            leds[122-led] = (255,165,0)
            leds[131-led] = rand_color
            leds[134-led] = (255,165,0)
            leds[182-led] = (255,165,0)
            leds[184-led] = rand_color
            leds[185-led] = rand_color
            leds[186-led] = rand_color
            leds[190-led] = rand_color
            leds[191-led] = rand_color
            leds[192-led] = rand_color
            leds[194-led] = (255,165,0)
            leds[242-led] = (255,165,0)
            leds[251-led] = rand_color
            leds[254-led] = (255,165,0)
            leds[302-led] = (255,165,0)
            leds[303-led] = (255,165,0)
            leds[304-led] = (255,165,0)
            leds[305-led] = (255,165,0)
            leds[306-led] = (255,165,0)
            leds[307-led] = (255,165,0)
            leds[308-led] = (255,165,0)
            leds[309-led] = (255,165,0)
            leds[310-led] = (255,165,0)
            leds[311-led] = (255,165,0)
            leds[312-led] = (255,165,0)
            leds[313-led] = (255,165,0)
            leds[314-led] = (255,165,0)
            

       ##---------ENGINE WARNING LIGHT --------------##
        rand_color = (random.randint(255,255),random.randint(99,215),random.randint(0,80))
        for led in range(1):   
            leds[48-led] = rand_color
            leds[49-led] = rand_color
            leds[50-led] = rand_color
            leds[51-led] = rand_color
            leds[52-led] = rand_color
            leds[110-led] = rand_color
            leds[165-led] = rand_color
            leds[167-led] = rand_color
            leds[168-led] = rand_color
            leds[169-led] = rand_color
            leds[170-led] = rand_color
            leds[171-led] = rand_color
            leds[172-led] = rand_color
            leds[173-led] = rand_color
            leds[174-led] = rand_color
            leds[175-led] = rand_color
            leds[177-led] = rand_color
            leds[225-led] = rand_color
            leds[226-led] = rand_color
            leds[235-led] = rand_color
            leds[236-led] = rand_color
            leds[237-led] = rand_color
            leds[285-led] = rand_color
            leds[287-led] = rand_color
            leds[295-led] = rand_color
            leds[296-led] = rand_color
            leds[297-led] = rand_color
            leds[348-led] = rand_color
            leds[349-led] = rand_color
            leds[350-led] = rand_color
            leds[351-led] = rand_color
            leds[352-led] = rand_color
            leds[353-led] = rand_color
            leds[354-led] = rand_color
            leds[355-led] = rand_color
            leds[357-led] = rand_color
                        
     ##-----------------FAULT ---------------------------------##      
            
        rand_color = (random.randint(220,255),random.randint(0,69),random.randint(0,60))
        for led in range(1):
            
            leds[19-led] = rand_color
            leds[20-led] = rand_color
            leds[21-led] = rand_color
            leds[78-led] = rand_color
            leds[81-led] = rand_color
            leds[137-led] = rand_color
            leds[138-led] = rand_color
            leds[139-led] = rand_color
            leds[143-led] = rand_color
            leds[144-led] = rand_color
            leds[147-led] = rand_color
            leds[150-led] = rand_color
            leds[152-led] = rand_color
            leds[157-led] = rand_color
            leds[158-led] = rand_color
            leds[159-led] = rand_color
            leds[160-led] = rand_color
            leds[161-led] = rand_color
            leds[198-led] = rand_color
            leds[202-led] = rand_color
            leds[205-led] = rand_color
            leds[207-led] = rand_color
            leds[210-led] = rand_color
            leds[212-led] = rand_color
            leds[219-led] = rand_color
            leds[258-led] = rand_color
            leds[262-led] = rand_color
            leds[263-led] = rand_color
            leds[264-led] = rand_color
            leds[265-led] = rand_color
            leds[267-led] = rand_color
            leds[270-led] = rand_color
            leds[272-led] = rand_color
            leds[279-led] = rand_color
            leds[318-led] = rand_color
            leds[322-led] = rand_color
            leds[325-led] = rand_color
            leds[327-led] = rand_color
            leds[328-led] = rand_color
            leds[329-led] = rand_color
            leds[330-led] = rand_color
            leds[332-led] = rand_color
            leds[333-led] = rand_color
            leds[334-led] = rand_color
            leds[335-led] = rand_color
            leds[339-led] = rand_color
            client.put_pixels(leds)
            time.sleep(.1)
            t=t+1

        client.put_pixels(leds)   
        


    
while True:
    value = input ( ''' RHORN'S AUTOMOTIVE DEALERSHIP
                \t To pick a car option type the number of your choice and press Enter.
                \t 1. Mercedes
                \t 2. Lexus
                \t 3. Chevrolet
                \t 4. Service
                \t 5. Exit
                 ''')
    
    if value.isdigit() == True: # .isdigit()
        choice = int(value)
        if choice == 1 :   # Run animations for Mercedes
            func1()
        elif choice ==2 :  # Run animations for Lexus
            func2()
        elif choice ==3 :  # Run animations for Chevrolet
            func3()
        elif choice ==4 :  # Run animations for Service
            func3()
        elif choice ==5 :  # Display text to exit showroom
            print (" You have now EXITED the online showroom...Thank You")
            break
        else:
            print("Invalid input, please provide an number from the list of cars above:")
            if value== chr:
                print("Invalid input, please provide a number from 1 to 3.")
            
