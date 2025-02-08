import array
import rp2

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

class Neopixel:
    def __init__(self, pin, num, brightness = 1):
        self.num = num
        self.brightness = brightness
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=pin)
        self.sm.active(1)

    def fill(self, color):
        if type(color) is tuple:
            color = self.from_rgb(color, self.brightness)
        self.sm.put(array.array("I", [color] * self.num), 8)

    def from_rgb(self, rgb: tuple, bright=1):
        r = int(bright * rgb[0])
        g = int(bright * rgb[1])
        b = int(bright * rgb[2])
        return (g<<16) | (r<<8) | b
