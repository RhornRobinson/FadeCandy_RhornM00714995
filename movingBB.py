import opc
from time import sleep
import colorsys
import time
import random
import winsound
#import gui



leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

### heart ####
led = 0
while True:
    for led in range(360,0):   
        leds[led+7] = (255,0,0)
        leds[led+8] = (255,0,0)
        leds[led+9] = (255,0,0)
    
        #leds[7+led+60] = (255,0,0)
       # leds[8+led+60] = (255,0,0)
       # leds[9+led+60] = (255,0,0)
    
        #leds[131-led+60] = (255,0,0)
        #leds[184-led+60] = (255,0,0)
        #leds[188-led+60] = (255,0,0)
        #leds[192-led+60] = (255,0,0)
        #leds[244-led+60] = (255,0,0)
        #leds[247-led+60] = (255,0,0)
        #leds[249-led+60] = (255,0,0)
        #leds[252-led+60] = (255,0,0)
        #leds[305-led+0] = (255,0,0)
        #leds[306-led+0] = (255,0,0)
        #leds[310-led+0] = (255,0,0)
        #leds[311-led+0] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break
        

###   B   #####
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
