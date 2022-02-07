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

##------------------------------>> Replace with Animation <<---------------------------------------------------------##
    for i in Blank:                 # Always starts with a blank so that it wipes previous screen..Calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)
##------------------------------>> Displays Mercedes Name <<---------------------------------------------------------##       
    for i in MercedesName:             # calls up every led in the list MercedesName to be lit   
        leds[i] = (0,230,191)         #for leds in list MercedesName set led colour as Robin Egg Blue
        client.put_pixels(leds)
        sleep(.03)
        
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
        leds[i] = (204,238,255)         #for leds in list GermanFlagBackground set led colour as white
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
    
#------------INSERT CAR ANIMATION HERE ----------------------------------------------------------------------------##
    for i in CarBody:                 # calls up every led in the list Blank to be lit
        leds[i] = (153,0,26)           #for leds in list Blank set led colour as burgandy
    for i in CarWheels:                 # calls up every led in the list Blank to be lit
        leds[i] = (131,152,163)     #for leds in list Blank set led colour as grey
    for i in CarWindows:                 # 
        leds[i] = (255,255,77)
    for i in LightBeam:                 # 
        leds[i] = (255,255,25)
        client.put_pixels(leds)
        sleep(.01)

while  leds in CarBody< 359:
       leds [i+1]= (153,0,26)
       CarWheels [i+1] = (131,152,163)
       CarWindow [i+1] = (255,255,77)
       LightBeam [i+1] = (255,255,25)
       client.put_pixels(leds)
       sleep(.01) 
        
    
    
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
                          
    for i in Blank:                 # Always starts with a blank so that it wipes previous screen..Calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)

    for i in ChevroletName:             # calls up every led in the list ChevroletName to be lit   
        leds[i] = (255,215,0)         #for leds in list ChevroletName set led colour as gold
        client.put_pixels(leds)
        sleep(.1)

    for i in Blank:                 # calls up every led in the list Blank to be lit
        leds[i] = (0,0,0)           #for leds in list Blank set led colour as black
        client.put_pixels(leds)
        sleep(.01)

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
    
    
        


    
while True:
    value = input ( ''' RHORN'S CAR SHOWROOM
                \t To pick a car option type the number of your choice and press Enter.
                \t 1. Mercedes
                \t 2. Lexus
                \t 3. Chevrolet
                \t 4. Exit
                 ''')
    choice = int(value)
    if value.isdigit() == True: # .isdigit() 
        if choice == 1 :
            func1()
        elif choice ==2 :
            func2()
        elif choice ==3 :
            func3()
        elif choice ==4 :
            print (" You have now EXITED the online showroom...Thank You")
            break
        else:
            print("Invalid input, please provide an number from the list of cars above:")
    else:
        print("Invalid input, please provide a number from 1 to 3.")
        break

