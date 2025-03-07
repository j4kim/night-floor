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
    def __init__(self, pin, num):
        self.num = num
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=pin)
        self.sm.active(1)
        self.brgen = bight_gen()
        self.brightness = next(self.brgen)
        self.color = None

    def fill(self, color):
        if type(color) is tuple:
            color = self.from_rgb(color, self.brightness)
        if color != self.color:
            self.sm.put(array.array("I", [color] * self.num), 8)
            self.color = color

    def from_rgb(self, rgb: tuple, bright=1):
        r = int(bright * rgb[0])
        g = int(bright * rgb[1])
        b = int(bright * rgb[2])
        return (g<<16) | (r<<8) | b

    def fade(self, target_color: tuple, br_from=0, br_to=1, seconds=3):
        fps = 10
        steps = int(seconds * fps)
        bright_step = (br_to - br_from) / steps
        bright = br_from
        for i in range(steps):
            bright = bright + bright_step
            color = self.from_rgb(target_color, bright)
            self.fill(color)
            sleep(1/fps)

    def fade_in(self, target_color, seconds=3):
        print("start fade in")
        self.fade(target_color, 0, self.brightness, seconds)
        print("end fade in")

    def fade_out(self, source_color, seconds=3):
        print("start fade out")
        self.fade(source_color, self.brightness, 0, seconds)
        print("end fade out")

    def change_brightness(self):
        self.brightness = next(self.brgen)
