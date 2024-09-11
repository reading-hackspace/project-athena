from machine import Pin, I2C
from time import sleep
from mpr121 import MPR121


i2c=I2C(0,scl=Pin(5), sda=Pin(4))
cap = MPR121(i2c)

while True:
    a =cap.touched()
    print('{:012b}'.format(a))
    sleep(0.02)
    