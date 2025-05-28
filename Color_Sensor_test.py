import tcs34725
from machine import I2C, Pin
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = tcs34725.TCS34725(i2c)

def colors(r, g, b):
    if r >= 255 and g >= 255 and b >= 255:
        return "white"
    elif r <= 0 and g <= 0 and b <= 0:
        return "black"
    elif r > g and r > b:
        return "close to red"
    elif g > r and g > b:
        return "close to green"
    elif b > r and b > g:
        return "close to blue"
    else:
        return "undefined"


while True:
    r, g, b, c = sensor.read(raw=True) #The clear channel (C) measures overall light intensity without any color filtering. It captures total ambient light and is used as a reference to normalize the RGB values.

    if c == 0:
        r_norm = g_norm = b_norm = 0
    else:
        r_norm = int((r / c) * 255)
        g_norm = int((g / c) * 255)
        b_norm = int((b / c) * 255)

    # Set to 0–255
    r_norm = max(0, min(255, r_norm))
    g_norm = max(0, min(255, g_norm))
    b_norm = max(0, min(255, b_norm))

    color_name = colors(r_norm, g_norm, b_norm)

    print("RGB: ({}, {}, {}) = {}".format(r_norm, g_norm, b_norm, color_name))

    time.sleep(1)
    