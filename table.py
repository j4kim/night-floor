from state import State
from time import ticks_diff, ticks_ms

class Table:
    def __init__(self, name, ldr, btn, switch_pir, switch_led, pir, led):
        """Initialize a Table object with sensors and controls.
        
        Args:
            name (str): Name identifier for the table
            ldr (ADC): Light Dependent Resistor analog input
            btn (Pin): Button input pin
            switch_pir (Pin): PIR enable/disable switch
            switch_led (Pin): LED enable/disable switch
            pir (Pin): PIR motion sensor input
            led (Led): Neopixel LED strip controller
        """
        self.name = name
        self.ldr = ldr
        self.btn = btn
        self.switch_pir = switch_pir
        self.switch_led = switch_led
        self.pir = pir
        self.led = led
        self.prevstate = State(self)
        self.lit_at = 0
        self.led_state = "off"
        self.fade_duration = 2000
        self.lit_duration = 10000
        self.prev_debug_parts = ''

    def is_night(self):
        return self.ldr.read_u16() > 10000

    def debug(self, *strs):
        print(self.name, ":", *strs)

    def debugState(self, state):
        parts = [str(state), self.led.brightness, self.led_state]
        str_parts = str(parts)
        if str_parts != self.prev_debug_parts:
            self.debug(self.ldr.read_u16(), *parts)
            self.prev_debug_parts = str_parts

    def pirloop(self, state):
        if not self.is_night():
            self.led.tune(0)
            return

        t = ticks_ms()
        diff = ticks_diff(t, self.lit_at)

        if diff < self.fade_duration:
            self.led_state = "fade-in"
            self.led.tune(diff / self.fade_duration)
        elif diff < self.lit_duration:
            self.led_state = "lit"
            self.led.tune(1)
        elif diff < (self.lit_duration + self.fade_duration):
            self.led_state = "fade-out"
            self.led.tune(1 - (diff - self.lit_duration) / self.fade_duration)
        else:
            self.led_state = "off"
            self.led.tune(0)

        if state.motion and not self.prevstate.motion:
            if self.led_state != "off":
                t = t - self.fade_duration
            self.lit_at = t

    def loop(self):
        state = State(self)
        self.debugState(state)

        if state.switch_led_down:
            self.led.tune(1)
        elif state.switch_pir_down:
            self.pirloop(state)
        else:
            self.led.tune(0)

        if state.btn_down and not self.prevstate.btn_down:
            self.led.change_brightness()

        self.prevstate = state
