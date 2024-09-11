from machine import Pin, I2C, PWM
from time import sleep
from mpr121 import MPR121

# define the pin to use for buzzing
buzzer = PWM(Pin(15))
# the duty cycle to use when the note is on
volume = 2512

# frequency - plays until stopped
def note_on(frequency):
    buzzer.duty_u16(volume)
    buzzer.freq(frequency)

# stop the noise
def note_off():
    buzzer.duty_u16(0)

def bit_length(n):
    bits = 0
    while n >> bits: bits += 1
    return bits

i2c=I2C(0,sda=Pin(4), scl=Pin(5))
cap = MPR121(i2c)
# C C# D D# E F F# G G# A A# B
notes = [262,277,294,311,329,349,370,392,415,440,466,493
         
         ]

last = -2
while True:
    x = cap.touched()
    # play note from leftmost press only
    leftmost = bit_length(x&-x) - 1
    if leftmost != last:
        if leftmost==-1:
            note_off()            
        else:
            note_on(notes[leftmost])
    last = leftmost 





