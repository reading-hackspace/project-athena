import board, audiobusio
import audiocore
import board
import array
import time
import math

i2s_bck_pin = board.GP16 # PCM5102 BCK pin
i2s_lck_pin = board.GP17 # PCM5102 LCK pin
i2s_dat_pin = board.GP18  # PCM5102 DIN pin
audio = audiobusio.I2SOut(bit_clock=i2s_bck_pin, 
                          word_select=i2s_lck_pin, 
                          data=i2s_dat_pin)

# Generate one period of sine wave.
length = 8000 // 440
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15) + 2 ** 15)

sine_wave = audiocore.RawSample(sine_wave, sample_rate=8000)

audio.play(sine_wave, loop=True)
time.sleep(1)
audio.stop()