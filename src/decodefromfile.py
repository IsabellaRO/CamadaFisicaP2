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
    
    ## Descobre tom com +/- 10Hz para cada valor de frequencias que formam um tom 
    tons = []
    for i in X:
        if (687 <= X[i] <= 707):
            if (1199 <= X[i] <= 1219):
                tons.append("1")
            elif (1326 <= X[i] <= 1346):
                tons.append("2")
            elif (1467 <= X[i] <= 1487):
                tons.append("3")
            elif (1623 < X[i] < 1643):
                tons.append("A")
            else:
                print("Erro, frequência não reconhecida")
                break                
            

        elif (760 < X[i] < 780):
            if (1199 < X[i] < 1219):
                tons.append("4")
            elif (1326 < X[i] < 1346):
                tons.append("5")
            elif (1467 < X[i] < 1487):
                tons.append("6")
            elif (1623 < X[i] < 1643):
                tons.append("B")
            else:
                print("Erro, frequência não reconhecida")
                break     
                
        elif (842 < X[i] < 862):
            if (1199 < X[i] < 1219):
                tons.append("7" )               
            elif (1326 < X[i] < 1346):
                tons.append("8")
            elif (1467 < X[i] < 1487):
                tons.append("9")
            elif (1623 < X[i] < 1643):
                tons.append("C")
            else:
                print("Erro, frequência não reconhecida")
                break     
                
        elif (931 < X[i] < 951):
            if (1199 < X[i] < 1219):
                tons.append("X")
            elif (1326 < X[i] < 1346):
                tons.append("0")
            elif (1467 < X[i] < 1487):
                tons.append("#")
            elif (1623 < X[i] < 1643):
                tons.append("D")
            else:
                print("Erro, frequência não reconhecida")
                break     
                
        elif (1199 < X[i] < 1219):
            if (687 <= X[i] <= 707):
                tons.append("1")
            elif (760 < X[i] < 780):
                tons.append("4")
            elif (842 < X[i] < 862):
                tons.append("7")
            elif (931 < X[i] < 951):
                tons.append("X")
            else:
                print("Erro, frequência não reconhecida")
                break     
        
        elif (1326 < X[i] < 1346):
            if (687 <= X[i] <= 707):
                tons.append("2")
            elif (760 < X[i] < 780):
                tons.append("5")
            elif (842 < X[i] < 862):
                tons.append("8")
            elif (931 < X[i] < 951):
                tons.append("0")
            else:
                print("Erro, frequência não reconhecida")
                break     
        
        elif (1467 < X[i] < 1487):
            if (687 <= X[i] <= 707):
                tons.append("3")
            elif (760 < X[i] < 780):
                tons.append("6")
            elif (842 < X[i] < 862):
                tons.append("9")
            elif (931 < X[i] < 951):
                tons.append("#")
            else:
                print("Erro, frequência não reconhecida")
                break     
        
        elif (1623 < X[i] < 1643):
            if (687 <= X[i] <= 707):
                tons.append("A")
            elif (760 < X[i] < 780):
                tons.append("B")
            elif (842 < X[i] < 862):
                tons.append("C")
            elif (931 < X[i] < 951):
                tons.append("D")
            else:
                print("Erro, frequência não reconhecida")
                break
        
        else:
            print("Erro, frequência não reconhecida")
            break     
        
            
    
    

if __name__ == "__main__":
    main()
