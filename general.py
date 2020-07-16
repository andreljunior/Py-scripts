
#Calcular a FFT de um sinal

from wave import Wave_read
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
from math import pi

plt.close('all')

#a = Wave_read('slide_whistle.wav')
#print(Wave_read.getframerate(a))

#gerar um sinal
Fs = 1000
t = np.arange(0,1,1/Fs)
f = 20

x = np.sin(2*pi*f*t)

plt.subplot(2,1,1)
plt.plot(t,x); plt.title('Sinal Senoidal')
plt.xlabel('Time(s)'); plt.ylabel('Amplitude')

#calcular fft
X = fft(x)
plt.subplot(2,1,2)
plt.plot(abs(X))
print('1')
plt.show()



