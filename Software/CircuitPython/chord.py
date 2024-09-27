# SPDX-FileCopyrightText: 2023 John Park and @todbot / Tod Kurt
#
# SPDX-License-Identifier: MIT

import time
import board
import synthio

# for PWM audio with an RC filter
#import audiopwmio
#audio = audiopwmio.PWMAudioOut(board.GP15)

# for I2S audio with external I2S DAC board
import audiobusio

i2s_bck_pin = board.GP16 # PCM5102 BCK pin
i2s_lck_pin = board.GP17 # PCM5102 LCK pin
i2s_dat_pin = board.GP18  # PCM5102 DIN pin
audio = audiobusio.I2SOut(bit_clock=i2s_bck_pin, word_select=i2s_lck_pin,data=i2s_dat_pin)

synth = synthio.Synthesizer(sample_rate=44100)
audio.play(synth)

while True:
    synth.press((65, 69, 72))  # midi note 65 = F4
    time.sleep(1)
    synth.release((65, 69, 72))  # release the note we pressed
    time.sleep(2)
