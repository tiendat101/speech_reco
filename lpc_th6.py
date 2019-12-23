from scikits.talkbox.linpred.levinson_lpc import lpc 
from scipy.io import wavfile
import matplotlib.pyplot as plt  
import numpy as np 

p = 15
start = 5500
rate , data = wavfile.read("xe.wav")

data_1 = data[5000:5256]
a, e ,k = lpc(data_1, p, -1)
# print a

a_1 = np.zeros(256,)

# for i in range(len(a)):
# 	a_1[i] = a[i]
a_1[:len(a)] = a

# print a_1
a_1_fft = np.fft.fft(a_1)
a_1_abs = np.abs(a_1_fft)
a_1_final = -np.log10(a_1_abs)	


plt.plot(a_1_final[:len(a_1_final)//2])
plt.grid()
plt.savefig("xe.png")

for i in range(1, len(a_1_final)/2-1):
	if(a_1_final[i]>a_1_final[i-1] and a_1_final[i]>a_1_final[i+1]):
		f_k = i*1*rate/256
		print f_k

plt.show()

			
