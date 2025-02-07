from machine import Pin, ADC
from time import sleep
import array
import rp2

led = Pin(25, Pin.OUT)

pir = Pin(3, Pin.IN)

ldr = ADC(Pin(26))

print("Running")

NUM_LEDS = 1
LED_PIN = 22

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on LED_PIN
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(LED_PIN))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

def set_led_color(color):
    sm.put(array.array("I", [color]), 8)

set_led_color(0x010101)

while True:
    led.toggle()

    if ldr.read_u16() > 2000:
        set_led_color(0x000001)
    else:
        set_led_color(0x010101)

    if pir.value():
        sleep(0.1)
    else:
        sleep(0.5)
