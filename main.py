from machine import Pin, ADC
from time import sleep
import array
import rp2

pir = Pin(26, Pin.IN)
ldr = ADC(Pin(27))

NUM_LEDS = 7
LED_PIN = 15

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

# green, red, blue
orangy = 0x204005 

def set_led_color(color):
    sm.put(array.array("I", [color] * NUM_LEDS), 8)

while True:
    ldr_value = ldr.read_u16()
    pir_value = pir.value()
    night = ldr_value > 5000

    print(ldr_value, night, pir_value)

    if pir_value and night:
        set_led_color(orangy)
    else:
        set_led_color(0)

    sleep(0.1)
