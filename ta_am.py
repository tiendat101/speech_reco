import scipy as scp
from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

rate_ta, data_ta = read("ta.wav")
rate_am, data_am = read("am.wav")

# Ts_ta = 1/fs_ta 
# Ts_am = 1/fs_am 

# xs_ta = np.arange(0,fs_ta, 1)
# xs_am = np.arange(0,fs_am, 1)
# x = np.arange(1500,2000)
# for i in range(1600, 2200, 1):
#     if(data_ta[i] > 5000):
#         print(i, data_ta[i])


# for i in range(1000, 2000, 1):
#     if(data_am[i] > 5000):
#         print(i, data_am[i])

plt.subplot(2,1,1)
# plt.figure(figsize=(7,4))
plt.plot(data_ta, linewidth=.5)

plt.subplot(2,1,2)
# plt.figure(figsize=(7,4))
plt.plot(data_am, linewidth=.5)
plt.savefig("ta_am.png")
# plt.show()

data_ta_1 = data_ta[:3500]
data_am_1 = data_am[1783:]

fs_1 = rate_ta
fs_2 = rate_am

write("tam.wav", fs_1, data_ta_1)
write("tam.wav", fs_2, data_am_1)


