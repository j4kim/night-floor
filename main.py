from machine import Pin, ADC
from time import sleep_ms
from led import Led
from table import Table

ldr = ADC(Pin(27))

table_1 = Table(
    name = "Table 1",
    ldr = ldr,
    btn = Pin(29, Pin.IN, Pin.PULL_UP),
    switch_pir = Pin(9, Pin.IN, Pin.PULL_UP),
    switch_led = Pin(10, Pin.IN, Pin.PULL_UP),
    pir = Pin(12, Pin.IN),
    led = Led(0, Pin(11), 7, (255, 127, 20))
)

table_2 = Table(
    name = "Table 2",
    ldr = ldr,
    btn = Pin(28, Pin.IN, Pin.PULL_UP),
    switch_pir = Pin(13, Pin.IN, Pin.PULL_UP),
    switch_led = Pin(14, Pin.IN, Pin.PULL_UP),
    pir = Pin(26, Pin.IN),
    led = Led(1, Pin(15), 7, (255, 127, 20))
)

while True:
    table_1.loop()
    table_2.loop()
    sleep_ms(50)
