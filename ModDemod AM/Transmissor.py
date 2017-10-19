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
#duration = 
lista_tempo = np.linspace(0, duration, fs * t)

#Leitura dos áudios
m1, fs1 = sf.read('m1.wav')
#m2, fs2 = sf.read('m2.wav')
#-------------------------------------------------------
#Definir cutOff
cutOff = 4000
# Filtro passa baixa
m1F  = lowPassFilter(m1, 4000, fs1)    
#m2F = 
##################### plotar Fourier dos sinais
xf, yf = Fourier(signal, fs) #fs mesmo
#--------------------------------------------------------
fc1, c1 = portadoras(fs1, m1)
#fc2, c2 = portadoras(fs2, m2)

#Conferindo tamanhos
if len(c1) == len(m1):
    print("Sinal gerado tem mesmo tamanho de áudio lido :) ")
##################### plotar Fourier dos sinais
xf, yf = Fourier(signal, fs)
#----------------------------------------------------------    
##################### Multiplicar áudio pela portadora
#am1 =  mensagem mesmo * portadora
#am2 = 
##################### plotar Fourier dos sinais
xf, yf = Fourier(signal, fs)
#--------------------------------------------------
Soma1 = am1 + am2
##################### plotar Fourier dos sinais
xf, yf = Fourier(signal, fs)
#--------------------------------------------------
##################### transmitir isso no som com Play





#Extract Raw Audio from Wav File 0
signal0 = som0.readframes(-1)
signal0 = np.fromstring(signal0, 'Int16')

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal0)


# Transforma o gráfico do filtro mais plano matematicamente
# CutOff ponto onde para de filtrar o que interessa
# fs frequencia
def butter_lowpass(cutOff, fs, order=5):
    nyq = 0.5 * fs
    normalCutoff = cutOff / nyq
    b, a = butter(order, normalCutoff, btype='low', analog = True)
    return b, a

#lfilter filtra os dados low
def butter_lowpass_filter(data, cutOff, fs, order=4):
    b, a = butter_lowpass(cutOff, fs, order=order)
    y = lfilter(b, a, data)
    return y