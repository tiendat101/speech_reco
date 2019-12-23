from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# f,data = wavfile.read("Xe.wav")
f,data = wavfile.read("xe.wav")
# print(f)
# print(len(data))
num_window_size = 1000
# time = [(1.0/f)*i*20 for i in range(len(data))]
# print(num_window_size)


w = []
r = []

# for i in range(0,len(data)-int(num_window_size),int(num_window_size/2)):
# for i in range(5000,5001,int(num_window_size/2)):

# def calc_T(a):
#     for i in range()
# data1 = np.zeros(len(data))
# ## Han che
# for i in range(len(data1)):
#     if abs(data[i])>10000:
#         data1[i] = data[i]

data2 = data[5000:5000+int(num_window_size)]
## tinh r
for k in range(1000):
    rk = 0
    for j in range(len(data2)-1-k):
        rk += data2[j]*data2[j+k]
        # print(data[j])
    r.append(rk)

plt.plot(data2)
# print(r)
plt.show()
#
# print(data)