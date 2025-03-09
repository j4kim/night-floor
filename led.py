import array
import rp2
from time import sleep

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

def bight_gen():
    while True:
        yield 0.2
        yield 0.5
        yield 1

class Led:
    def __init__(self, table_id, pin, num, target_color: tuple):
        self.num = num
        self.sm = rp2.StateMachine(table_id, ws2812, freq=8_000_000, sideset_base=pin)
        self.sm.active(1)
        self.target_color = target_color
        self.brgen = bight_gen()
        self.brightness = next(self.brgen)
        self.color = None

    def tune(self, b = 1):
        color = self.from_rgb(self.target_color, self.brightness * b)
        self.fill(color)

    def fill(self, color):
        if color != self.color:
            self.sm.put(array.array("I", [color] * self.num), 8)
            self.color = color

    def from_rgb(self, rgb: tuple, bright=1):
        r = int(bright * rgb[0])
        g = int(bright * rgb[1])
        b = int(bright * rgb[2])
        return (g<<16) | (r<<8) | b

    def change_brightness(self):
        self.brightness = next(self.brgen)
