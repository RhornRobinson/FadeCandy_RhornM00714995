import opc
from time import sleep
import colorsys
import time
import random
import winsound
#import gui



leds = [(0,0,0)]*360   # list of 360 tuples, each containing R,G,B values.
LexusName = []
LexusBadge = []
Blank = []
JapanName = []
JapanFlag = []
CarBody = []
CarWheel = []
CarWindow = []
LightBeam = []


client = opc.Client('localhost:7890')
client.put_pixels(leds)

##------------------------->>> Function for Mercedes displays <<<----------------------------------------------##
def func1 ():
    rand_colour = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    MercedesName = [3,7,10,11,12,13,16,17,18,19,22,23,24,25,28,29,30,31,34,35,40,41,42,43,46,47,48,49,63,64,66,67,70,76,79,82,88,94,96,100,106,123,125,127,130,131,136,138,142,148,148,154,157,160,161,167,183,187,190,191,196,197,202,208,209,214,217,220,221,228,243,247,250,256,259,262,268,274,276,280,289,303,307,310,311,312,313,316,319,322,323,324,325,328,329,330,331,334,335,340,341,342,343,346,347,348,349]
    Blank = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,
             158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,
             289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359]
    MercedesBadge = [25,26,27,28,29,30,31,32,33,84,85,89,93,94,143,144,149,154,155,203,204,208,210,214,215,264,265,267,271,273,274,325,326,327,328,329,330,331,332,333]
    GermanyName = [3,4,5,6,7,10,11,12,13,14,17,18,19,20,21,24,28,33,38,42,45,49,63,70,77,81,84,85,87,88,92,94,98,99,102,105,109,123,130,131,137,140,141,144,146,148,151,155,158,159,160,162,166,168,183,185,186,187,190,191,197,198,199,204,208,211,212,213,214,215,218,220,221,222,227,243,247,250,257,260,264,268,271,275,278,281,282,287,303,304,305,306,307,310,311,312,313,314,317,321,324,328,331,335,338,342,347]
    GermanFlagBackground = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,
                            191,192,193,194,195,196,197,198,199,200,201,202,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359]
    GermanFlagBlack = [23,24,25,26,27,28,29,30,31,32,33,34,35,36,83,84,85,86,87,88,89,90,91,92,93,94,95,96]
    GermanFlagRed = [143,144,145,146,147,148,149,150,151,152,153,154,155,156,203,204,205,206,207,208,209,210,211,212,213,214,215,216]
    GermanFlagYellow = [263,264,265,266,267,268,269,270,271,272,273,274,275,276,323,324,325,326,327,328,329,330,331,332,333,334,335,336]
    CarBody = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,66,72,73,79,80,120,121,122,123,124,125,126,132,133,140,141,142,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,240,241,242,247,248,249,250,251,252,253,254,259,260,261,262,263]
    CarWheels = [244,245,256,257,304,305,316,317]
    CarWindows = [67,68,69,70,71,74,75,76,77,78,127,128,129,130,131,134,135,136,137,138,139,203,]
    LightBeam = [89,90,91,148,149,150,151,205,206,207,208,209,210,211,267,268,269,270,271,329,330,331]
    #for i in Blank:                 # Always starts with a blank so that it wipes previous screen..Calls up every led in the list Blank to be lit
     #   #leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
      #  client.put_pixels(leds)
       # sleep(.01)
    ##----------------------- MOVING CAR ANIMATION -----------------------------------
           
    led = 0
    while led<27:                 
        for led in range(28):   
                leds = [(0,0,0)]*360           #--Below are the LEDs and what part of the car they correspond to ------
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
                
##--------------------------------- Wiping Out the Car before next animation ----------------------------
    led = 28                                   # from LEDs 28 onwards
    while led<60:                              # move LEDs from 28 towards 60
        for rows in range (6):                 # and for every 6 rows
            leds [led + rows*60] = (0,0,0)     # set every LEDs black 
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1
        
          

##------------------------------>> Displays Mercedes Name <<---------------------------------------------------------##       
    for i in MercedesName:             # calls up every led in the list MercedesName to be lit   
        leds[i] = (0,230,191)         #for leds in list MercedesName set led colour as Robin Egg Blue
        client.put_pixels(leds)
        sleep(.1)

               
        
    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
##------------------------------->> Mercedes Badge image <<-----------------------------------------------------------##        
    for i in MercedesBadge:            # calls up every led in the list MercedesBadge to be lit
        leds[i] = (0,0,255)         #for leds in list MercedesBadge set led colour as 
        client.put_pixels(leds)
        sleep(.03)
        
    for i in Blank:                 # calls up every led in the list |Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
        
    for i in GermanyName:             # calls up every led in the list GermanName to be lit   
        leds[i] = (0,230,191)         #for leds in list GermanName set led colour as 
        client.put_pixels(leds)
        sleep(.03)
        
    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
 ##--------------------------------->> German Flag <<-------------------------------------------------------------##       
    for i in GermanFlagBackground:            # calls up every led in the list GermanFlagBackground to be lit
        leds[i] = (67,70,75)         #for leds in list GermanFlagBackground set led colour as white
        client.put_pixels(leds)
        sleep(.01)
    for i in GermanFlagBlack:            # calls up every led in the list GermanFlagBlack to be lit
        leds[i] = (0,0,0)         #for leds in list GermanFlagBlack set led colour as black
        client.put_pixels(leds)
        sleep(.01)
    for i in GermanFlagRed:            # calls up every led in the list GermanFlagRed to be lit
        leds[i] = (255,0,0)         #for leds in list GermanFlagRed set led colour as black
        client.put_pixels(leds)
        sleep(.01)
    for i in GermanFlagYellow:            # calls up every led in the list GermanFlagYellow to be lit
        leds[i] = (255,255,0)         #for leds in list GermanFlagYellow set led colour as black
        client.put_pixels(leds)
        sleep(.01)
    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
##------------------------ Flashing Wrench -------------------------------
    led = 12
    while led<347:                         #do this forever:
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for led in range(1):
            leds = [(0,0,0)]*360    #set everything black,
            rand_color = (random.randint(rand_color[0]-5, rand_color[0]+5),random.randint(rand_color[1]-5, rand_color[1]+5),random.randint(rand_color[2]-2, rand_color[2]+2)) 
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
            
            ##--------------------------------- Wiping Out the Car before next animation ----------------------------
led = 28                                   # from LEDs 28 onwards
while led<60:                              # move LEDs from 28 towards 60
    for rows in range (6):                 # and for every 6 rows
        leds [led + rows*60] = (0,0,0)     # set every LEDs black 
    client.put_pixels(leds)
    time.sleep(.1)
    led = led+1
   
 
        
    
    
##--------------------------->>>  FUNCTION FOR LEXUS DISPLAYS <<<---------------------------------------------------##
       
def func2 ():
    
    rand_colour = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    LexusName = [1,9,10,11,12,13,14,17,22,25,30,33,34,35,36,37,38,61,69,78,81,85,90,93,121,129,130,131,139,140,145,150,154,155,181,189,190,191,199,200,205,210,216,217,241,249,258,261,265,270,278,301,302,303,304,305,306,309,310,311,312,313,314,317,322,325,326,327,328,329,330,333,334,335,336,337,338]
    Blank = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,
             158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,
             289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359]
    LexusBadge = [27,28,29,30,31,32,33,86,89,94,145,148,155,205,208,209,210,211,212,215,266,274,327,328,329,330,331,332,333]
    JapanName = [4,5,6,7,8,13,19,20,21,22,23,29,35,39,66,72,74,79,83,88,90,95,96,99,126,131,135,139,143,147,151,155,156,157,159,186,191,192,193,194,195,199,200,201,202,203,207,208,209,210,211,215,217,218,219,244,246,251,255,259,267,271,275,278,279,305,306,311,315,319,327,331,335,339]
    JapanFlagWhite = [13,14,15,16,17,18,19,24,25,26,27,28,29,30,73,74,75,76,77,86,87,88,89,90,133,134,135,136,147,148,149,150,193,194,195,196,207,208,209,210,253,254,255,256,257,266,267,268,269,270,313,314,315,316,317,318,319,324,325,326,327,328,329,330]
    JapanFlagRed = [20,21,22,23,78,79,80,81,82,83,84,85,137,138,139,140,141,142,143,144,145,146,197,198,199,200,201,202,203,204,205,206,258,259,260,261,262,263,264,265,320,321,322,323]

     ##----------------------- MOVING CAR ANIMATION -----------------------------------
           
    led = 0
    while led<27:                 
        for led in range(28):   
                leds = [(0,0,0)]*360           #--Below are the LEDs and what part of the car they correspond to ------
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
                
##--------------------------------- Wiping Out the Car before next animation ----------------------------
    led = 28                                   # from LEDs 28 onwards
    while led<60:                              # move LEDs from 28 towards 60
        for rows in range (6):                 # and for every 6 rows
            leds [led + rows*60] = (0,0,0)     # set every LEDs black 
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1
        
          


    for i in Blank:                 # Always starts with a blank so that it wipes previous screen..Calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
        
    for i in LexusName:             # calls up every led in the list LexusName to be lit   
        leds[i] = (255,0,0)         #for leds in list LexusName set led colour as red
        client.put_pixels(leds)
        sleep(.01)
        
    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
        
    for i in LexusBadge:            # calls up every led in the list LexusBadge to be lit
        leds[i] = (0,0,255)         #for leds in list LexusBadge set led colour as Blue
        client.put_pixels(leds)
        sleep(.01)

    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)

    for i in JapanFlagWhite:
        leds[i] = (255,255,255)
    for i in JapanFlagRed:
        leds[i] = (255,0,0)
        client.put_pixels(leds)
        sleep(0.03)

    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)

    for i in JapanName:
        leds[i] = (255,0,0)
        client.put_pixels(leds)
        sleep(0.03)


        
 

##------------------------------------------>>  ANIMATIONS FOR CHEVROLET <<---------------------------------------------------------------##
def func3 ():
    rand_colour = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    ChevroletName = [2,3,4,5,8,11,14,15,16,17,20,24,27,28,29,30,33,34,35,36,39,45,46,47,48,51,52,53,54,55,62,68,71,74,80,84,87,90,93,96,99,105,113,122,128,129,130,131,134,135,141,143,147,149,153,156,159,165,166,173,182,188,189,190,191,194,195,201,203,207,208,213,216,219,225,226,233,242,248,251,254,262,267,269,273,276,279,285,293,302,303,304,305,308,311,314,315,316,322,327,330,333,334,335,336,339,340,341,342,345,346,347,348,353]
    Blank = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,
             158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,
             289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359]
    ChevroletBadgeSilver = [27,31,83,84,85,86,87,91,92,93,94,95,96,97,98,142,157,201,216,260,261,262,263,264,265,266,267,271,272,273,274,275,327,331]
    ChevroletBadgeGold = [28,29,30,88,89,90,143,144,145,146,147,148,149,150,151,152,153,154,155,156,202,203,204,205,206,207,208,209,210,211,212,213,214,215,268,269,270,328,329,330]
    USAname = [9,13,17,18,19,20,21,27,69,73,77,78,86,88,129,133,138,145,149,189,193,199,205,206,207,208,209,249,253,260,261,265,269,309,310,311,312,313,317,318,319,320,321,325,329]
    USAflagBlue =[21,23,25,27,82,84,86,141,143,145,147]
    USAflagRed =[88,89,90,91,92,93,94,95,96,97,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337]
    USAflagWhite =[22,24,26,28,29,30,31,32,33,34,35,36,37,81,83,85,87,142,144,146,148,149,150,151,152,153,154,155,156,157,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277]
                          
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

    led = 28
    while led<60:
        for rows in range (6):
            leds [led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1
##-------------------------- chevrolet name ----------------------------
    for i in ChevroletName:             # calls up every led in the list ChevroletName to be lit   
        leds[i] = (255,215,0)         #for leds in list ChevroletName set led colour as gold
        client.put_pixels(leds)
        sleep(.1)
##---------------------------clear animation --------------------------------
    #for i in Blank:                 # calls up every led in the list Blank to be lit
     #   leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
      #  client.put_pixels(leds)
       # sleep(.01)
    led = 0
    while led<60:
        for rows in range (6):
            leds [led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1
##-----------------------wheel ---------------------------------------
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

  ##------------------------ clear wheel     -------------------------------------------
    led = 50
    while led<60:
        for rows in range (6):
            leds [led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1

##-------------------- ---------------------- -----------------------

    for i in ChevroletBadgeSilver:                 # calls up every led in the list ChevroletBadgeSilver to be lit
        leds[i] = (192,192,192)           #for leds in list ChevroletBadgeSilver set led colour as silver
    for i in ChevroletBadgeGold:                 # calls up every led in the list ChevroletBadgeGold to be lit
        leds[i] = (255,215,0)           #for leds in list ChevroletBadgeGold set led colour as gold
        client.put_pixels(leds)
        sleep(.1)

    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)

    for i in USAname:                 # calls up every led in the list USAname to be lit
        leds[i] = (255,0,0)           #for leds in list USAname set led colour as red
        client.put_pixels(leds)
        sleep(.1)

    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)

    for i in USAflagBlue:                 # calls up every led in the list to be lit
        leds[i] = (0,0,255)           #for leds in list 
    for i in USAflagWhite:                 # calls up every led in the list  to be lit
        leds[i] = (255,255,255)           #for leds in list
    for i in USAflagRed:                 # calls up every led in the list  to be lit
        leds[i] = (255,0,0)
        client.put_pixels(leds)
        sleep(.1)
    
##--------------------------------- Wiping Out the animation to black screen----------------------------
    led = 0                                   # from LEDs 0 onwards
    while led<60:                              # move LEDs from 0 towards 60
        for rows in range (6):                 # and for every 6 rows
            leds [led + rows*60] = (0,0,0)     # set every LEDs black 
        client.put_pixels(leds)
        time.sleep(.1)
        led = led+1
        


    
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
            

