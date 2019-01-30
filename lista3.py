import numpy as np
import scipy as sp
from scipy.fftpack import fft
from scipy import signal
import matplotlib.pyplot as plt

# ilosc sampli
N = 1000
# rozklad sampli
time = 1.0 / 800.0
x = np.linspace(0.0, N * time, N)
y = np.sin(40.0 * 2.0 * np.pi * x) + np.sin(80.0 * 2.0 * np.pi * x) + np.sin(120 * 2.0 * np.pi * x)
widmo = yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * time), N // 2)

plt.figure(1)
plt.plot(x, y)
plt.title = "test"
plt.legend(['Signal'])
plt.xlabel('Signal in time domain')

plt.figure(2)
plt.plot(x[:len(x) // 5], y[:len(y) // 5])
plt.legend(['Zoomed signal'])
plt.xlabel('Zoomed signal in time domain')

plt.figure(3)
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.legend(['FFT'])
plt.xlabel('FFT of the sum of 3 sines')

winRect = np.ones(N)
winGauss = sp.signal.windows.gaussian(N, std=140)
winHamming = sp.signal.windows.hamming(N)
winHanning = sp.signal.windows.hann(N)
winBartlet = sp.signal.windows.bartlett(N)

plt.figure(4)
plt.plot(winRect)
plt.plot(winGauss)
plt.plot(winHamming)
plt.plot(winHanning)
plt.plot(winBartlet)
plt.legend(['Rectangular', 'Gauss', 'Hamming', 'Hanning', 'Bartlet'])

plt.figure(5)
yr = winRect * y
plt.plot(yr)
plt.legend(['Rectangular'])

plt.figure(6)
yg = winGauss * y
plt.plot(yg)
plt.legend(['Gauss'])

plt.figure(7)
yham = winHamming * y
plt.plot(yham)
plt.legend(['Hamming'])

plt.figure(8)
yhan = winHanning * y
plt.plot(yhan)
plt.legend(['Hanning'])

plt.figure(9)
yb = winBartlet * y
plt.plot(yb)
plt.legend(['Bartlet'])

plt.figure(10)
plt.plot(xf, 2.0 / N * np.abs(fft(yr)[0:N // 2]))
plt.legend(['Rectangular'])

plt.figure(11)
plt.plot(xf, 2.0 / N * np.abs(fft(yg)[0:N // 2]))
plt.legend(['Gauss'])

plt.figure(12)
plt.plot(xf, 2.0 / N * np.abs(fft(yham)[0:N // 2]))
plt.legend(['Hamming'])

plt.figure(13)
plt.plot(xf, 2.0 / N * np.abs(fft(yhan)[0:N // 2]))
plt.legend(['Hanning'])

plt.figure(14)
plt.plot(xf, 2.0 / N * np.abs(fft(yb)[0:N // 2]))
plt.legend(['Bartlet'])

plt.grid()
plt.show()