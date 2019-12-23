import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
AudioName = "xe.wav" # Audio File
fs, data = read(AudioName)
N= 3000
K= 1500
base_id = 5000
R = np.zeros((K,))
D = np.zeros((K,))
seg= data[base_id:base_id+N]
seg = seg.astype('float')
for k  in range(0, K, 1):
	for n in range(0, N-k,1):
		R[k] += seg[n]*seg[n+k]

R[abs(R)<2e10] =0
for k  in range(0, K, 1):
	for m in range(0, N-k, 1):
		D[k] += abs(seg[m]- seg[m-k])
#r = np.correlate(data, data, mode='full')
plt, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex = False)
ax1.plot(seg)
ax1.set_title("Segment")
ax2.plot(R)
ax2.set_title("R(k)")
ax3.plot(D)
ax3.set_title("D(k)")
ax4.plot(data)
ax4.set_title("Data")
plt.show()
# plt.savefig("bai4.png")

