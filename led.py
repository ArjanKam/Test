from machine import Pin
from time import sleep

led = Pin(28, Pin.OUT)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)


