import mido 
from pynput import keyboard
import time

port = mido.open_output('2- RD-2000 2')

note_defs = {'1': -4, 'q': -3, 'a': -2, 'z': -1, 'x': 0, 'c': 1, 'f': 2, 't':3, '6':4}

note = 60
sustain = False 
def on_press(key):
    global note
    global sustain 
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        port.send(mido.Message("note_off", note=note))
    try: 
        k = key.char
    except: 
        k = key.name 
    if k == 'm':
        sustain = not sustain 
        if not sustain:
            for x in range(0, 127):
                port.send(mido.Message('note_off', note=x))
    if k in note_defs.keys():
        adder = note_defs[k]
        if(note + adder > 127 or note + adder < 0):
            adder = 0
        note = note + adder
        
        port.send(mido.Message('note_on', note=note))
        if not sustain:
            port.send(mido.Message('note_off', note=note - adder))
            time.sleep(0.02)
            port.send(mido.Message('note_off', note=note))
    

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()