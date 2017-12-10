#/usr/bin/python

import RPi.GPIO as GPIO
import time
#import logging

#logging.basicConfig(format='%(levelname)s-%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,filename='/App/gpio.log')

mpin = 14
tpin = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(mpin, GPIO.IN)
GPIO.setup(tpin, GPIO.OUT)

cap = 0.000001
adj = 2.130620985

inter = 0
adder = 0
nopts = 2

# Set GPIO mode: GPIO.BCM or GPIO.BOARD

lapsetime_1=time.time()
while inter<nopts:
  GPIO.output(tpin, False)
  time.sleep(3)
  GPIO.output(tpin, True)
  starttime=time.time()
  endtime=time.time()
  while (GPIO.input(mpin) == GPIO.LOW):
    endtime=time.time()
  measureresistance=endtime-starttime
  res=(measureresistance/cap)*adj
  inter=inter+1
  adder=adder+res
  
lapsetime_2=time.time()
timelapse=lapsetime_2-lapsetime_1

print(inter)
print(adder/nopts)
print(timelapse)

# Reset all gpio pin
GPIO.cleanup()
