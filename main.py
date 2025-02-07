from machine import Pin, ADC
from time import sleep

led = Pin(25, Pin.OUT)

pir = Pin(3, Pin.IN)

ldr = ADC(Pin(26))

print(dir(ldr))

print("Running")

while True:
    led.toggle()
    if pir.value():
        sleep(0.1)
    else:
        sleep(0.5)
    print(ldr.read_u16())
