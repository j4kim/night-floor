from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

pir = Pin(3, Pin.IN)

print("Running")

while True:
    led.toggle()
    if pir.value():
        sleep(0.1)
    else:
        sleep(0.5)
