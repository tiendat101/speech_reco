from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# f,data = wavfile.read("Xe.wav")
f,data = wavfile.read("kho.wav")
print(f)
print(len(data))
T = 1/f
num_window_size = f*0.02
# time = [(1.0/f)*i*20 for i in range(len(data))]
print(num_window_size)


hamming = np.hamming(int(num_window_size))
w1 = []
w2 = []

xs = np.arange(0, T*len(data),T)




for i in range(0,len(data)-int(num_window_size),int(num_window_size/2)):
    data_ = data[i:i+int(num_window_size)]
    hamming_data = data_*hamming
    w_ = 0.0
    for j in hamming_data:
        w_ += j**2
    w1.append(w_)
# plt.plot(w1)
# plt.show()

def zcr(data):
    result = 0
    for i in range(len(data)-1):
        if data[i]*data[i+1] < 0:
           result+=1
    return result
for i in range(0,len(data)-int(num_window_size),int(num_window_size/2)):
    data_ = data[i:i+int(num_window_size)]
    hamming_data = data_ * hamming
    w_ = zcr(hamming_data)
    w2.append(w_)

# plt.plot(w2)
# plt.show()


plt.subplot(3,1,1)
plt.plot(xs, data, linewidth = 0.1)

plt.subplot(3,1,2)
plt.plot(w1)

plt.subplot(3,1,3)
plt.plot(w2)

plt.show()