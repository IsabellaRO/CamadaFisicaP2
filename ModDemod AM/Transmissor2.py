# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:18:25 2017

@author: isabella
"""

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
import wave
import sys
from scipy.signal import butter, lfilter
from scipy.signal import freqs
import math
from scipy.fftpack import fft
from scipy import signal as window
from scipy import signal as sg

def lowPassFilter(signal, cutoff_hz, fs):
        #####################
        # Filtro
        #####################
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))


def portadoras(f, audio):
    # Cria as portadoras a partir de frequencia e audio
    p1 = np.linspace(0, len(audio)/fs, len(audio))
    p2 = np.sin(p1 * f * 2 * math.pi)
    return (p1, p2)
    
def Play(y, fs):
    print("Reproduzindo som") 
    # reproduz o som   
    sd.play(y, fs)
    # aguarda fim da reprodução
    sd.wait()
    print("Fim da reprodução")
    
def Fourier(signal, fs):

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

fs = 44100
duration = 100 
lista_tempo = np.linspace(0, duration, fs * duration)

#Leitura dos áudios
m1, fs1 = sf.read('m1.wav')
#m2, fs2 = sf.read('m2.wav')
ym1 = m1[:,1]
amostra1 = len(ym1)
#-------------------------------------------------------
#Definir cutOff
cutOff = 4000
# Filtro passa baixa
m1F  = lowPassFilter(m1, cutOff, fs1)    
#m2F = 
