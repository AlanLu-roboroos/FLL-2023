from pybricks.ev3devices import ColorSensor
from threading import Thread
from time import sleep

# Wrapper class for colorsensor
# Allows for calibration of lightsensor

class Col:
    tolerance = 4
    def __init__(self, col):
        self.r = col[0]
        self.g = col[1]
        self.b = col[2]
    def equals(self, col):
        if (abs(self.r - col.r) < self.tolerance and abs(self.g - col.g) < self.tolerance and abs(self.b - col.b) < self.tolerance):
            return True
        return False


class MenuSelector:
    def __init__(self, port, colorMenu, defaultColor, state):
        self.sensor = ColorSensor(port)
        self.colorMenu = colorMenu
        self.defaultColor = defaultColor
        self.state = state
        self.on = True

    def index(self):
        if self.on:
            # try:
            r, g, b = self.sensor.rgb()
            if self.defaultColor.equals(Col([r, g, b])):
                return None
            for color in self.colorMenu:
                if color.equals(Col([r, g, b])):
                    return self.colorMenu.index(color)
            return None
        return None

    def color(self):
        return self.sensor.rgb()

    def toggle(self):
        self.on = not self.on
