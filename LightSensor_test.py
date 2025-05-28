import tsl2591 # light sensor
from machine import Pin, I2C
from time import sleep


## Assigning pins
i2c = I2C(scl = Pin(5), sda = Pin(4))

sensor = tsl2591.TSL2591(i2c)
print(sensor.read())

## P1Q8
def LEDprint(reps):
    #LED = Pin(gpio, Pin.OUT) # assigning a pin
    datafile = open("light_test.csv", "a")
    for i in range(reps):
        #LED.value(1)
        sleep(1)
        data = sensor.read()
        raw_data = sensor.get_full_luminosity()
        print(data)
        print(raw_data)
        datafile.write(str(data) + ',' + str(raw_data) + "\n")
        #LED.value(0)
        #sleep(1)
    datafile.close()
    
#LEDprint(10)

