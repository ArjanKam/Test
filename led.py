from machine import Pin
from time import sleep

# set the leds
led = Pin(28, Pin.OUT)

# main code
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)


