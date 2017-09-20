# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:12:56 2017

@author: Vitoria
"""
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import math

t = 1
fs = 44100
lista_tempo = np.linspace(0, t, fs * t)

def Tons(data):

    dic_tons = {
            0: (941, 1336),
            1: (697, 1209),
            2: (697, 1336),
            3: (697, 1477),
            4: (770, 1209),
            5: (770, 1336),
            6: (770, 1477),
            7: (852, 1209),
            8: (852, 1336),
            9: (852, 1477),
            "ast": (941, 1209),
            "hash": (941, 1477),
            }
    
    return(dic_tons.get(data))

def geraOnda(data):

    lowf, highf = data
    ondas = np.sin(2 * math.pi * lista_tempo * lowf) + np.sin(2 * math.pi * lista_tempo * highf) 
    return ondas    
    
def grafico(data):

    plt.xlabel('Tempo')
    plt.ylabel('Valor')
    plt.plot(lista_tempo[0:100], data[0:100], color="#FF00D4")
    plt.show()
    
        
        
def Onda(data):
    
    tom = geraOnda(Tons(data))

    sd.play(tom, fs)
    sd.wait()
    grafico(tom)
    
    
Onda(0)
Onda(1)
Onda(2)
Onda(3)
Onda(4)
Onda(5)
Onda(6)
Onda(7)
Onda(8)
Onda(9)
Onda("ast")
Onda("hash")