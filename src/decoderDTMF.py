# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:11:43 2017

@author: Isabella
"""

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

t = 1
fs = 44100
duration = 1
lista_tempo = np.linspace(0, t, fs * t)    
   
def Record(duration, fs):
    print("Gravando som")
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    print("Fim da gravação")
    y = audio[:,0]
    return y
    
def Play(y, fs):
    print("Reproduzindo som") 
    # reproduz o som   
    sd.play(y, fs)
    # aguarda fim da reprodução
    sd.wait()
    print("Fim da reprodução")
    
y = Record(duration, fs)
Play(y, fs)

plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.plot(lista_tempo[0:1000], y[0:1000], color="#FF00D4")
plt.show()
    
