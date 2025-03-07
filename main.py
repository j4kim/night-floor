from machine import Pin, ADC
from time import sleep
from tools import Neopixel
from table import Table

ldr = ADC(Pin(27))

table_2 = Table(
    name = "Table 2",
    ldr = ldr,
    btn = Pin(28, Pin.IN, Pin.PULL_UP),
    switch_pir = Pin(13, Pin.IN, Pin.PULL_UP),
    switch_led = Pin(14, Pin.IN, Pin.PULL_UP),
    pir = Pin(26, Pin.IN),
    led = Neopixel(Pin(15), 7, 0.2)
)

while True:
    table_2.loop()

    sleep(0.1)
