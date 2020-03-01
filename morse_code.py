
import argparse
import time

import numpy as np
import pyaudio

FREQ = 523.251
RATE = 44100

MORSE = {'a' : [0, 1],
         'b' : [1, 0, 0, 0],
         'c' : [1, 0, 1, 0],
         'd' : [1, 0, 0],
         'e' : [0],
         'f' : [0, 0, 1, 0],
         'g' : [1, 1, 0],
         'h' : [0, 0, 0, 0],
         'i' : [0, 0],
         'j' : [0, 1, 1, 1],
         'k' : [1, 0, 1],
         'l' : [0, 1, 0, 0],
         'm' : [1, 1],
         'n' : [1, 0],
         'o' : [1, 1, 1],
         'p' : [0, 1, 1, 0],
         'q' : [1, 1, 0, 1],
         'r' : [0, 1, 0],
         's' : [0, 0, 0],
         't' : [1],
         'u' : [0, 0, 1],
         'v' : [0, 0, 0, 1],
         'w' : [0, 1, 1],
         'x' : [1, 0, 0, 1],
         'y' : [1, 0, 1, 1],
         'z' : [1, 1, 0, 0],
         '1' : [0, 1, 1, 1, 1],
         '2' : [0, 0, 1, 1, 1],
         '3' : [0, 0, 0, 1, 1],
         '4' : [0, 0, 0, 0, 1],
         '5' : [0, 0, 0, 0, 0],
         '6' : [1, 0, 0, 0, 0],
         '7' : [1, 1, 0, 0, 0],
         '8' : [1, 1, 1, 0, 0],
         '9' : [1, 1, 1, 1, 0],
         '0' : [1, 1, 1, 1, 1],
         '.' : [0, 1, 0, 1, 0, 1],
         ',' : [1, 1, 0, 0, 1, 1],
         '?' : [0, 0, 1, 1, 0, 0],
         '-' : [1, 0, 0, 0, 0, 1],
         '/' : [1, 0, 0, 1, 0],
         ' ' : [],
        }

def make_sin(length):
    length = int(length * RATE)
    factor = FREQ * np.pi * 2 / RATE
    return np.sin(np.arange(length) * factor)

def play_tone(length):
    stream.write(make_sin(length).astype(np.float32).tostring())

def define_length(char):
    if char == ' ':
        time.sleep(0.4)
    for code in MORSE[char]:
        if code == 0:
            play_tone(0.2)
        elif code == 1:
            play_tone(0.4)
        time.sleep(0.2)
    time.sleep(0.2)

def encode(words):
    words_list = list(words)
    for char in words_list:
        if char in MORSE:
            define_length(char)


if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--words', '-w', type=str, default='')
#     args = parser.parse_args()

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=RATE, output=1)

    while True:
        words = input()
        encode(words)

    stream.close()
    p.terminate()

