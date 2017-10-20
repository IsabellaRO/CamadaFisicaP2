import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fftpack import fft
from scipy import signal as sg
import sounddevice as sd
from itertools import zip_longest

def LPF(signal, cutoff_hz, fs):
        # Filtro passa baixa
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, corte/nyq_rate, window=('kaiser', beta))
        
        return(sg.lfilter(taps, 1.0, signal))

def calcFFT(signal, fs):
        # Calcula Fourier

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

# Frequencia de corte do passa-baixa
corte = 3400

# Le os audios
m1, fs1 = sf.read('m1.wav')
m2,fs2 = sf.read('m2.wav')

# Filtra com passa-baixa
filtrom1 = LPF(m1[:,0], corte, fs1)
filtrom2 = LPF(m2[:,0], corte, fs2)

# Fourier da mensagem filtrada
f1, Y1 = calcFFT(filtrom1, fs1)
f2, Y2 = calcFFT(filtrom2, fs2)

# Frequencia das portadoras
fp1 = 7000
fp2 = 14000

t1 = np.linspace(0, len(filtrom1)/fs1, len(filtrom1))
t2 = np.linspace(0, len(filtrom2)/fs2, len(filtrom2))

# Portadoras
p1 = np.sin(fp1*t1*2*math.pi)
p2 = np.sin(fp2*t2*2*math.pi)

# Fourier das portadoras
p1fourier, Y1p = calcFFT(p1, fs1)
p2fourier, Y2p = calcFFT(p2, fs2)

# Modulando
am1 = filtrom1 * p1
am2 = filtrom2 *p2

# Fourier do sinal modulado
amfourier1, Y1f = calcFFT(am1, fs1)
amfourier2, Y2f = calcFFT(am2, fs2)

# Soma os dois sinais em um só com a função zip_longest
sfinal = [x + y for x, y in zip_longest(am1, am2, fillvalue=0)]

# Fourier da soma dos sinais
fouriersoma, Yr = calcFFT(sfinal, fs1)
plt.plot(fouriersoma, np.abs(Yr))
plt.title('Fourier das duas mensagens moduladas')
plt.show()

# Reproduz e salva o sinal final
sd.play(sfinal,fs1)
sd.wait()
sf.write("modulado.wav", sfinal, fs1)
print("Audio modulado foi salvo!")