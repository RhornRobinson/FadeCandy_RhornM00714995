import opc
import time
#import coloursys
import random

leds_colour = [(255,255,255)]*360 #white

led = 0
colour = []
client = opc.Client('localhost:7890')
client.put_pixels(leds_colour)
client.put_pixels(leds_colour)      
while led<60:
    leds_colour[led] = (0,0,255) #row 1 - 0-60
    leds_colour[led+60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
    leds_colour[led+120] = (0,0,255)
    leds_colour[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
    leds_colour[led+240] = (0,0,255)
    leds_colour[led+300] = (0,0,255)
    client.put_pixels(leds_colour)
    time.sleep(.1)
    led = led + 1
    for led in range (0,0,360):
        leds_colour = [(0,0,0)]*360;

    
#-----------Name Lexus ----------------------
#  Letter  L
#    leds_colour[0]=(0,0,0);        leds_colour[1]=(255,255,255);          leds_colour[9,15]=(255,255,255);
#    leds_colour[2,8]=(0,0,0);      leds_colour[17]=(255,255,255);         leds_colour[22]=(255,255,255);
#   leds_colour[15,16]=(0,0,0);    leds_colour[25]=(255,255,255);         leds_colour[30]=(255,255,255);    
#    leds_colour[18,21]=(0,0,0);    leds_colour[33,38]=(255,255,255);      leds_colour[23,24]=(0,0,0);
#    leds_colour[26,29]=(0,0,0);    leds_colour[31,32]=(0,0,0);

client.put_pixels(leds_colour)
time.sleep(.1)
led = led + 1
