import scipy as scp
from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

rate, data = read('kho.wav')

N = 300
K = 150

#Ham tu tuong quan
def R(dat):
	kq = []
	data1 = np.arange(len(dat))
	for i in range(len(dat)):
		if abs(dat[i]) < 3000:
			data1[i] = 0
		else:
			data1[i] = dat[i]
	for i in range(0, K, 1):
		x = 0
		for j in range(0, N - i, 1):
			x = x + data1[j] * data1[j + i]
		kq.append(x)
	return kq

#Ham vi sai bien do trung binh 
def AMDF(dat):
	kq = []
	data1 = np.arange(len(dat))
	for i in range(len(dat)):
		#loc cac gia tri cuc dai nho (lam nhieu)
		if abs(dat[i]) < 3000:
			data1[i] = 0
		else:
			data1[i] = dat[i]
	for i in range(0, N, 1):
		x = 0.0
		for j in range(0, N - i, 1):
			x = x + abs(data1[j] - data1[j + i])
		kq.append(x / (N-i-1))
	return kq

# def findT(dat):


fig, (ax1, ax2, ax3, ax4, ax5) = pl.subplots(5 , 1 , sharex=False)

xplot = np.arange(len(data)) / rate
ax1.plot(xplot, data)
ax1.set_xlim([0, 6])

F0 = []

start = 8000

ax2.plot(data[start: start+N])
ax3.plot(R(data[start: start+N]))
ax4.plot(AMDF(data[start: start+N]))

xplot4 = []

for i in range(0, len(data) - N, N ):
	win = data[i:i+N]
	rr = R(win)
	T0 = 0
	for j in range(20, len(rr), 1):
		if rr[j] == max(rr[20:100]):
			T0 = j
	f = rate / T0
	if f > 150:
		F0.append(f)
		xplot4.append(i / rate)

print(F0)
print(xplot4)
ax5.scatter(xplot4 ,F0)
ax5.set_xlim([0, 6])
ax5.set_ylim([0, max(F0)])

pl.show()