import numpy as np 
import matplotlib.pyplot as plt 

x_max = 5
f = 10
fs = 100
muy = 255
n = np.arange(1,21,1)
x_n = x_max*np.sin(2*np.pi*n*f/fs)
V = x_max

y_n = V*np.log(1+muy*np.abs(x_n)/V)*np.sign(x_n)/np.log(1+muy)

z_n = V/muy*((1+muy)**(	np.abs(y_n)/V)-1)*np.sign(y_n)
plt.subplot(3,1,1)
plt.plot(n, x_n)

plt.subplot(3,1,2)
plt.plot(n, y_n)

plt.subplot(3,1,3)
plt.plot(n, z_n)
plt.show()