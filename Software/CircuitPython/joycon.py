# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

analog_in0 = AnalogIn(board.GP26)
analog_in1 = AnalogIn(board.GP27)


switch = DigitalInOut(board.GP22)
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT



switch.direction = Direction.INPUT
switch.pull = Pull.UP

def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    if switch.value:
        led.value = False
    else:
        led.value = True
    print((get_voltage(analog_in0),get_voltage(analog_in1)) )
    time.sleep(0.1)
