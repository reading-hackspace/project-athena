# Test the pots and switches on the Project Athena keyboard
import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

pot0 = AnalogIn(board.GP26)
pot1 = AnalogIn(board.GP27)


switch1 = DigitalInOut(board.GP7)
switch2 = DigitalInOut(board.GP14)
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switch1.direction = Direction.INPUT
switch1.pull = Pull.UP
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP


def get_voltage(pin):
    return (pin.value / 65535)  * 3.3 

def get_percent(pin):
    return (1 - (pin.value / 65535)) * 100 

while True:
    if switch1.value:
        led.value = False
    else:
        led.value = True
        
    if switch2.value is False:
        print((get_voltage(pot0),get_voltage(pot1)) )
        print((get_percent(pot0),get_percent(pot1)) )
    time.sleep(0.1)
