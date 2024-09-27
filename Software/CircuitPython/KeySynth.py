# Project Athena
# Test polyphonic MPR121 keyboard with Synthio


import board
import busio
import synthio
import digitalio
import ulab.numpy as np

# Import MPR121 module.
import adafruit_mpr121


# for PWM audio with an RC filter
#import audiopwmio
#audio = audiopwmio.PWMAudioOut(board.GP15)

# if PWM not used mute audio
PWM = digitalio.DigitalInOut(board.GP15)
PWM.direction = digitalio.Direction.OUTPUT
PWM.value = False

# for I2S audio with external I2S DAC board
import audiobusio

i2s_bck_pin = board.GP16 # PCM5102 BCK pin
i2s_lck_pin = board.GP17 # PCM5102 LCK pin
i2s_dat_pin = board.GP18  # PCM5102 DIN pin
audio = audiobusio.I2SOut(bit_clock=i2s_bck_pin, word_select=i2s_lck_pin,data=i2s_dat_pin)
MIDI_NOTES = [60,61,62,63,64,65,66,67,68,69,70,71,]

SAMPLE_SIZE = 512
SAMPLE_VOLUME = 32000  # 0-32767
envelope = synthio.Envelope(attack_time=0.1, decay_time = 0.1, release_time=0.1, attack_level=1, sustain_level=0.05)
wave_sine = np.array(np.sin(np.linspace(0, 2*np.pi, SAMPLE_SIZE, endpoint=False)) * SAMPLE_VOLUME, dtype=np.int16)

synth = synthio.Synthesizer(sample_rate=44100)
audio.play(synth)

# Create I2C bus.
i2c = busio.I2C(board.GP5, board.GP4)

# Create MPR121 class.
mpr121 = adafruit_mpr121.MPR121(i2c)


last_pads = 0
note_on_sequence = []
note_off_sequence = []
while True:
    # Get touched state for all pads
    pads = mpr121.touched()
    # Any pads touched
    if( pads != last_pads):
        changed = last_pads ^ pads
        #print(pads, changed)
        note_on_sequence.clear()
        note_off_sequence.clear()
        for note in range(12):
            if (changed & (1 << note)):
                if(pads & (1 << note)):
                    note_on_sequence.append(MIDI_NOTES[note])    
                    
                else:
                    note_off_sequence.append(MIDI_NOTES[note])  
            
            
        last_pads = pads
        #print(note_on_sequence)
        #print(note_off_sequence)
        synth.press(note_on_sequence)
        synth.release(note_off_sequence)
        
   

