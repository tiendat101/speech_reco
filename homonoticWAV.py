import scipy as scp
from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read


def configFilter(data):
    out = []
    for i in range(1, len(data), 1):
        out.append(data[i] - 0.98 * data[i - 1])
    return out


fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = pl.subplots(7, 1, sharex=False)

rate, data = read('Xe.wav')

sizecut = 512
start = int(0.4 * rate)
# start = 100

sg = data[start:start + sizecut]

ax1.plot(sg)
ax1.set_title('Original')

sg = configFilter(sg)

ax2.plot(sg)
ax2.set_title('After Adjust Filter')

sg = sg * signal.hamming(sizecut - 1)

ax3.plot(sg)
ax3.set_title('After Hamming')

sg1 = np.abs(fft(sg))
sg1 = sg1[0:int(sizecut / 2)]
sg1 = ifft(sg1)
ax6.plot(sg1)
ax6.set_title('Inverse fft without log')

ax4.plot(fft(sg))
ax4.set_title('fft')

sg = np.abs(fft(sg))
maxS = max(sg)
sg = np.log10(sg / maxS) * (- 20)
sg = sg[0:int(sizecut / 2)]

sg = ifft(sg)

ax5.plot(sg)
ax5.set_title('Inverse log fft')

ax7.specgram(data, Fs=rate)
ax7.set_title('Spectrogram')

xplot = np.arange(len(data)) / rate

pl.show()
