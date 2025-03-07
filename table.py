from state import State
from time import time

orangy = (255, 127, 20)

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
        self.lit_at = time() - 60
        self.led_state = "off"

    def is_night(self):
        return self.ldr.read_u16() > 10000

    def debug(self, *strs):
        print(self.name, ":", *strs)

    def debugState(self, state):
        self.debug(
            self.ldr.read_u16(),
            str(state),
            self.led.brightness,
            self.led_state,
        )

    def pirloop(self, state):
        if not self.is_night:
            self.led.fill(0)
            return

        t = time()
        diff = t - self.lit_at

        if state.motion and not self.prevstate.motion:
            self.lit_at = t

        if diff < 2:
            self.led_state = "fade in"
        elif diff < 10:
            self.led_state = "lit"
            self.led.fill(orangy)
        elif diff < 12:
            self.led_state = "fade out"
        else:
            self.led_state = "off"
            self.led.fill(0)

    def loop(self):
        state = State(self)
        self.debugState(state)

        if state.switch_led_down:
            self.led.fill(orangy)
        elif state.switch_pir_down:
            self.pirloop(state)
        else:
            self.led.fill(0)

        if state.btn_down and not self.prevstate.btn_down:
            self.led.change_brightness()

        self.prevstate = state
