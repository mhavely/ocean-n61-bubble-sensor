from machine import Pin, I2C
from onewire import OneWire
import tsl2591  # light sensor
import tcs34725  # color sensor
import urtc  # datetime clock
import time
from time import sleep

## Assigning Pins
i2c = I2C(scl=Pin(5), sda=Pin(4))
light_sensor = tsl2591.TSL2591(i2c)
color_sensor = tcs34725.TCS34725(i2c)
rtc = urtc.DS3231(i2c)

print("Light Sensor Initial Reading:", light_sensor.read())

# Setting DateTime
#rtc.datetime((2025, 5, 21, 4, 13, 5, 0))
print("RTC Set Time:", rtc.datetime())

p2=Pin(2,Pin.OUT)

## --- Functions ---

# Color classification
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

# Normalize RGB to 0–255 scale
def normalize_rgb(r, g, b, c):
    if c == 0:
        return 0, 0, 0
    r_norm = int((r / c) * 255)
    g_norm = int((g / c) * 255)
    b_norm = int((b / c) * 255)
    return max(0, min(255, r_norm)), max(0, min(255, g_norm)), max(0, min(255, b_norm))

# Average RGB values
def average_readings(sensor, samples=3):
    r_total = g_total = b_total = c_total = 0
    for _ in range(samples):
        r, g, b, c = sensor.read(raw=True)
        r_total += r
        g_total += g
        b_total += b
        c_total += c
        time.sleep(0.05)
    return r_total // samples, g_total // samples, b_total // samples, c_total // samples

## Sampling Loop
def sample(location="lab"):
    for _ in range(40):  # Change to 100 if desired
        p2.value(0)
        with open("test_data3.csv", "a") as datafile:
            # Timestamp
            dt = rtc.datetime()
            timeStamp = f"{dt.year}/{dt.month}/{dt.day} {dt.hour}:{dt.minute}:{dt.second}"

            # Color Raw Reading
            r_raw, g_raw, b_raw, c_raw = color_sensor.read(raw=True)
            r_norm_raw, g_norm_raw, b_norm_raw = normalize_rgb(r_raw, g_raw, b_raw, c_raw)
            color_name_raw = colors(r_norm_raw, g_norm_raw, b_norm_raw)

            # Averaged Color Reading
            r_avg, g_avg, b_avg, c_avg = average_readings(color_sensor, samples=3)
            r_norm_avg, g_norm_avg, b_norm_avg = normalize_rgb(r_avg, g_avg, b_avg, c_avg)
            color_name_avg = colors(r_norm_avg, g_norm_avg, b_norm_avg)

            # Light sensor reading
            light_data = light_sensor.read()
            raw_light = light_sensor.get_full_luminosity()
            
            # Color temp
            color_temp = color_sensor.read()

            # Output to terminal
            print(f"Time: {timeStamp}")
            print("RAW RGB:", (r_norm_raw, g_norm_raw, b_norm_raw), "=", color_name_raw)
            print("AVG RGB:", (r_norm_avg, g_norm_avg, b_norm_avg), "=", color_name_avg)
            print("Light Data:", light_data)
            print("Raw Light:", raw_light)
            print("RAW Color Temp:", color_temp)
            print()

            # Save to file
            datafile.write(
                f"Time: {timeStamp}, "
                f"Light: {light_data}, Raw Light: {raw_light}, "
                f"AVG RGB: ({r_norm_avg}, {g_norm_avg}, {b_norm_avg}) = {color_name_avg}, "
                f"Color Temp: {color_temp}\n"
            )

        time.sleep(1)
        p2.value(1)
        time.sleep(2)

## Simple Light Logging Function (P1Q8)
def LEDprint(reps):
    with open("light_test3.csv", "a") as datafile:
        for i in range(reps):
            sleep(1)
            data = light_sensor.read()
            raw_data = light_sensor.get_full_luminosity()
            print(data)
            print(raw_data)
            datafile.write(f"{data}, {raw_data}\n")

# Example usage
sample()
# LEDprint(10)  # Uncomment to log light sensor data separately
