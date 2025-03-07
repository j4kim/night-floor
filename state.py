class State:
    def __init__(self, table):
        self.btn_down = table.btn.value() == 0
        self.switch_pir_down = table.switch_pir.value() == 0
        self.switch_led_down = table.switch_led.value() == 0
        self.motion = table.pir.value() == 1

    def __str__(self):
        return "%d|%d|%d|%d" %(self.btn_down, self.switch_pir_down, self.switch_led_down, self.motion)