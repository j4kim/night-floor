from machine import Pin, ADC
from time import sleep
from tools import Neopixel, from_rgb

pir = Pin(26, Pin.IN)
ldr = ADC(Pin(27))

led = Neopixel(Pin(15), 7)

# green, red, blue
orangy = from_rgb(32, 64, 5)

pir_val = 0
prev_pir_val = 0

while True:
    ldr_value = ldr.read_u16()
    night = ldr_value > 5000
    pir_val = pir.value()

    if (pir_val != prev_pir_val):
        print("PIR state change", pir_val)
        if pir_val and night:
            led.fill(orangy)
        else:
            led.fill(0)

    prev_pir_val = pir_val

    sleep(0.1)
