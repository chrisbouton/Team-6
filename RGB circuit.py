import sys, time
import RPi.GPIO as GPIO
from time import sleep
redPin = 12
greenPin = 13
bluePin = 6


def blink(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
blink(bluePin)
sleep(10)
turnOff(bluePin)

blink(greenPin)
sleep(10)
turnOff(greenPin)

blink(redPin)
sleep(10)
turnOff(redPin)

    

