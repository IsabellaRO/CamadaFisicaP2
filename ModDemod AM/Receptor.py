# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:21:22 2017

@author: Vitoria
"""
import numpy as np
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as sg
import math

fs = 48000
   
def Record(duration, fs):
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    print("Fim da gravação")
    y = audio[:,0]
    return y

def Fourier(signal, fs):

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

def Portadoras(f, audio):
    # Cria as portadoras a partir de frequencia e audio
    p1 = np.linspace(0, len(audio)/fs, len(audio))
    p2 = np.sin(p1*f*2*math.pi)
    return (p1,p2)
    
def LPF(signal, cutoff_hz, fs):
    # Filtro Passa Baixa
    # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
    nyq_rate = fs/2
    width = 5.0/nyq_rate
    ripple_db = 60.0 #dB
    N , beta = sg.kaiserord(ripple_db, width)
    taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    return(sg.lfilter(taps, 1.0, signal))
        
def main():
    duration = 5
    fs1= 7000
    fs2= 14000
    corte= 3000
    
    print("Analisando som")
    
    #y = Record(duration, fs) # Grava do ambiente
    y, fs = sf.read('modulado.wav') # Carrega audio do arquivo

    #  Calcula a trasformada de Fourier do audio escutado
    X, Y = Fourier(y, fs)
    
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.title("Fourier do sinal recebido")
    y = np.abs(Y)
    plt.plot(X, y)
    plt.show()
    
    p1x,p1y = Portadoras(fs1,y)
    p2x,p2y = Portadoras(fs2,y)
    
    # Multiplica o audio escutado pela portadora (demodula)
    final1 = y * p1y
    final2 = y * p2y
    
    
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.title("Fourier do sinal 1 demodulado")
    plt.plot(final1)
    plt.show()
    
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.title("Fourier do sinal 2 demodulado")
    plt.plot(final2)
    plt.show()
    
    fourier_final1x, fourier_final1y = Fourier(final1, fs)
    fourier_final2x, fourier_final2y = Fourier(final2, fs)
    
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.title("Fourier do sinal 1 resultante")
    plt.plot(LPF(final1, corte, fs))
    plt.show()
    
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.title("Fourier do sinal 2 resultante")
    plt.plot(LPF(final2, corte, fs))
    plt.show()

    # Filtra e reproduz o som
    sd.play(LPF(final1,corte,fs),fs)
    sd.wait()
    sd.play(LPF(final2,corte,fs),fs)
    sd.wait()
    sf.write("demodulado1.wav", LPF(final1,corte,fs), fs)
    sf.write("demodulado2.wav", LPF(final2,corte,fs), fs)
    print("Os audios foram salvos!")


main()