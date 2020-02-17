from pynput import keyboard
import simpleaudio 
import threading, time 
import sys

mapping = {}
cur_key = ""

def set_params():
    f = open(sys.argv[1])
    c = f.read().split("\n")
    for kv in c:
        if "=" in kv:
            print("Mapping "+ kv.split("=")[0] + " to " + kv.split("=")[1])
            mapping[kv.split("=")[0]] = kv.split("=")[1]


def on_press(key):
    global cur_key
    key =str(key).replace("'", "")
    cur_key = key
    if key in mapping.keys():
        cur_key = key
        #p = simpleaudio.WaveObject.from_wave_file(mapping[key]).play() 


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def t():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


set_params()


my_thread = threading.Thread(target=t)
my_thread.start() # Run the keyboard listener on separate thread 

while cur_key != "y": 
    if(cur_key in mapping.keys()):
        p = simpleaudio.WaveObject.from_wave_file(mapping[cur_key]).play() 
        p.wait_done()
    time.sleep(0.01)
        





    
