import RPi.GPIO as GPIO  
import time
import sys  
# blinking function  
def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return  
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(11, GPIO.OUT)  
# blinks forever (until Ctrl+C)
while True:
        try:
                blink(11)
        except KeyboardInterrupt:
                print "exit..."
                GPIO.cleanup()