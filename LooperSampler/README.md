# LooperSampler

## Purpose

Assign various keys on your keyboard to play back (and loop) wav file splices. Great for live song performances to have a more dynamic backing track. 

## How to use it 

Create a file called `parameters.txt` and populate it as such:

[key Name]=[path to WAV file] 

so that when you hit [key name] on your keyboard, it will queue that WAV file. This file will then loop until you queue the next WAV file, at which point it will then loop that.

## Running the application 

From the command line, execute `python3 player.py /path/to/parameters.txt` 



