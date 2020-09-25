import RPi.GPIO as GPIO
import time

def main():
        pinIN = 11
        pinLED = 13
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinIN, GPIO.IN, pullup_down=GPIO.PUD_DOWN)
        GPIO.setup(pinLED, GPIO.OUT)

        lastIN = GPIO.input(pinIN)

    while(true):

        if (GPIO.input(pinIN) != lastIN):
            if (lastIN == 1):
                GPIO.output(pinLED, GPIO.LOW)
                lastIN = 0;
            else:
                GPIO.output(pinLED, GPIO.HIGH)
                lastIN = 1;
        
        time.sleep(0.001)