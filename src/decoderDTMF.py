# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:11:43 2017

@author: Isabella
"""

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf # Para instalar ele: https://pysoundfile.readthedocs.io/en/0.9.0/
import peakutils
from peakutils.plot import plot as pplot

t = 1
fs = 44100
duration = 1
lista_tempo = np.linspace(0, t, fs * t)    
   
#def Record(duration, fs):
#    print("Gravando som")
#    audio = sd.rec(int(duration*fs), fs, channels=1)
#    sd.wait()
#    print("Fim da gravação")
#    y = audio[:,0]
#    return y
#    
#def Play(y, fs):
#    print("Reproduzindo som") 
#    # reproduz o som   
#    sd.play(y, fs)
#    # aguarda fim da reprodução
#    sd.wait()
#    print("Fim da reprodução")
#
#contador = 0
#while contador <= 11:
#    y = Record(duration, fs)
#    Play(y, fs)
#    
#    plt.xlabel('Tempo')
#    plt.ylabel('Valor')
#    plt.plot(lista_tempo[0:1000], y[0:1000], color="#FF00D4")
#    plt.show()
#    
#    audio = "./arquivos/audio"
#    audio = audio + str(contador) + ".wav"
#    sf.write(audio, y, fs)
#    contador += 1
#    
# Calculate de FFT from a signal
# https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
def calcFFT(signal, fs):
        from scipy.fftpack import fft
        from scipy import signal as window

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

def main():

    # Import sound as file
    y, fs = sf.read('./arquivos/audio7.wav')

    # Cacula a trasformada de Fourier do sinal
    X, Y = calcFFT(y, fs)

    ## Exibe modulo 
    plt.figure("abs(Y[k])")
    #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.plot(X,np.abs(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')
    

    ## Exibe fase
    plt.figure("Fase(Y[k])")
    plt.plot(X,np.angle(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')

    indexes = peakutils.indexes(Y, thres=0.9, min_dist=268)
    print("Frequencias principais: " , X[indexes] , "Hz")
    pplot(X, Y, indexes)

    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
    

y, fs = sf.read('./arquivos/audio11.wav')

    # Cacula a trasformada de Fourier do sinal
X, Y = calcFFT(y, fs)


db = 10 * np.log10(np.abs(Y)/20000)

plt.plot(X, db)
plt.grid(True)
plt.ylabel("Decibéis (dB)")
plt.xlabel("Frequência (Hz)")
plt.title("Frequência x Decibéis")
plt.show()    