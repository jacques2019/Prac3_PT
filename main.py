import RPI.GPIO as GPIO
import time

def main():
    while(true):
        pinIN = 11
        pinLED = 13
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinIN, GPIO.IN, pullup_down=GPIO.PUD_DOWN)
        GPIO.setup(pinLED, GPIO.OUT)

        if (GPIO.input(pinIN)):
            GPIO.output(pinLED, GPIO.HIGH)
        else:
            GPIO.output(pinLED, GPIO.LOW)
        
        time.sleep(0.01)

            
    