from machine import Pin, ADC
from time import sleep
from tools import Neopixel

pir = Pin(26, Pin.IN)
ldr = ADC(Pin(27))

led = Neopixel(Pin(15), 7)

# green, red, blue
orangy = 0x204005

while True:
    ldr_value = ldr.read_u16()
    pir_value = pir.value()
    night = ldr_value > 5000

    print(ldr_value, night, pir_value)

    if pir_value and night:
        led.fill(orangy)
    else:
        led.fill(0)

    sleep(0.1)
