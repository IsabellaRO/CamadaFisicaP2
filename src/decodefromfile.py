# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:12:17 2017

@author: Vitoria
"""

import numpy as np
import matplotlib.pyplot as plt
import peakutils
from peakutils.plot import plot as pplot

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
    import soundfile as sf
    y, fs = sf.read('./arquivos/ton2.wav')

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
