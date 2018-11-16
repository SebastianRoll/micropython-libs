from machine import Pin, ADC, SPI
import pin_definitions as pd
import components
from encoder import Encoder
from ssd1351 import Display, color565


class ControllerBox:
    def __init__(self):
        self.button_left = Pin(pd.BUTTON_LEFT, Pin.IN, Pin.PULL_UP)
        self.button_right= Pin(pd.BUTTON_RIGHT, Pin.IN, Pin.PULL_UP)

        self.mic = ADC(pd.MIC)
        self.mic.atten(ADC.ATTN_11DB)

        self.joystick = components.Joystick()

        self.encoder = Encoder(pin_clk=pd.ENCODER_CLK, pin_dt=pd.ENCODER_DT, clicks=4)

        self.spi = SPI()

        self.display = Display(self.spi, rst=Pin(pd.SSD1351_RST), dc=Pin(pd.SSD1351_DC), cs=Pin(pd.SSD1351_CS))
