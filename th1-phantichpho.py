from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

fs, data = wavfile.read('xe.wav')
T = 1/fs
xs = np.arange(0,T*len(data), T)
plt.figure(figsize=(7,4))
plt.plot(xs, data, linewidth=.5)
plt.xlabel('s')
plt.ylabel('amplitude')
plt.title('Phổ xe')
plt.show()
plt.savefig('xe.png')
