# import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, data = wavfile.read("xe.wav")
plt.specgram(data, Fs=fs)
plt.show()