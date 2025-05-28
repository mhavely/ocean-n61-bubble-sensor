import urtc
from machine import Pin, I2C

i2c = I2C(scl = Pin(5), sda = Pin(4))
rtc = urtc.DS3231(i2c)
rtc.datetime((2025, 5, 21, 4, 13, 05, 0))
print(rtc.datetime())