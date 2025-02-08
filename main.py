from machine import Pin, ADC
from time import sleep
from tools import Neopixel

pir = Pin(26, Pin.IN)
ldr = ADC(Pin(27))

led = Neopixel(Pin(15), 7, 0.2)

orangy = (255, 127, 20)

pir_val = 0
prev_pir_val = 0
lit = False

while True:
    ldr_value = ldr.read_u16()
    night = ldr_value > 5000
    pir_val = pir.value()

    if (pir_val != prev_pir_val):
        print("PIR state change", pir_val, night)
        if pir_val:
            if night:
                led.fade_in(orangy, 9)
                lit = True
                print("Stay lit for 5 seconds")
                sleep(5)
            else:
                print("It is not night")
        else:
            if lit:
                led.fade_out(orangy)
                lit = False

    prev_pir_val = pir_val

    sleep(0.1)
