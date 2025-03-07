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
            led (Neopixel): LED strip controller
        """
        self.name = name
        self.ldr = ldr
        self.btn = btn
        self.switch_pir = switch_pir
        self.switch_led = switch_led
        self.pir = pir
        self.led = led

    def loop(self):
        print(
            self.ldr.read_u16(),
            self.btn.value(),
            self.switch_pir.value(),
            self.switch_led.value(),
            self.pir.value()
        )
        if self.switch_led.value() == 0:
            self.led.fill(orangy)
        else:
            self.led.fill(0)
