# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:12:17 2017

@author: Vitoria
"""

import numpy as np
import matplotlib.pyplot as plt
import peakutils
from peakutils.plot import plot as pplot
import math
import encoderDTMF
from itertools import combinations

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
            
    # Cacula a trasformada de Fourier do sinal transmitido
    
    tom = encoderDTMF.Tons(6)
    y = encoderDTMF.geraOnda(tom)
    fs = 44100
    X, Y = calcFFT(y, fs)
    db = 10 * np.log10(np.abs(Y)/20000)
    plt.grid(True)
    plt.ylabel("Decibéis (dB)")
    plt.xlabel("Frequência (Hz)")
    plt.title("Sinal transmitido")
    #plt.plot(X, db)

    # Cacula a trasformada de Fourier do sinal recebido
    import soundfile as sf
    y, fs = sf.read('./arquivos/audio0.wav')
    X, Y = calcFFT(y, fs)
    db = 10 * np.log10(np.abs(Y)/20000)
    indexes = peakutils.indexes(Y, thres=0.4, min_dist=268)
    print(indexes)

    
    picos = []
    pontos = []
    count = 0
    
    while len(picos) < 2 and count < len(indexes):
        pontos.append(indexes[count])
        if indexes[count] < 680:
            pontos.remove(indexes[count])  
            count+=1  
        else:
            picos.append(indexes[count])
            pontos.remove(indexes[count])
            count+=1
                
                
                
                
    print(picos)
    print("Frequencias principais: " , X[indexes] , "Hz")
    plt.grid(True)
    plt.ylabel("Decibéis (dB)")
    plt.xlabel("Frequência (Hz)")
    plt.title("Sinal Recebido")
    plt.plot(X, db)

    #pplot(X, Y, indexes)

    plt.show()
    
    
    ## Exibe fase
    #plt.title('Modulo Fourier audio')    
    #db2 = 10 * np.log10(np.angle(Y)/20000) 
    #plt.figure("Fase(Y[k])")
    #plt.grid()
    #plt.plot(X,db2)
    #plt.show()

 ## Descobre tom com +/- 10Hz para cada valor de frequencias que formam um tom 
    tons = []
    low = picos[0]
    high = picos[1]
    low = int(low)
    high = int(high)
    print(low)
    print(high)
    if (687 <= low <= 707):
        if (1199 <= high <= 1219):
           tons.append("1")
        elif (1326 <= high <= 1346):
            tons.append("2")
        elif (1467 <= high <= 1487):
            tons.append("3")
        elif (1623 < high < 1643):
            tons.append("A")
        else:
            print("Erro, frequência não reconhecida")      
        

    elif (760 < low < 780):
        if (1199 < high < 1219):
            tons.append("4")
        elif (1326 < high < 1346):
            tons.append("5")
        elif (1467 < high < 1487):
            tons.append("6")
        elif (1623 < high < 1643):
            tons.append("B")
        else:
            print("Erro, frequência não reconhecida")
            
    elif (842 < low < 862):
        if (1199 < high < 1219):
            tons.append("7" )               
        elif (1326 < high < 1346):
            tons.append("8")
        elif (1467 < high < 1487):
            tons.append("9")
        elif (1623 < high < 1643):
            tons.append("C")
        else:
            print("Erro, frequência não reconhecida") 
            
    elif (931 < low < 951):
        if (1199 < high < 1219):
            tons.append("X")
        elif (1326 < high < 1346):
            tons.append("0")
        elif (1467 < high < 1487):
            tons.append("#")
        elif (1623 < high < 1643):
            tons.append("D")
        else:
            print("Erro, frequência não reconhecida")
            
    
    else:
        print("Erro, frequência não reconhecida")
    
    print(tons)
  
if __name__ == "__main__":
    main()
    
    
