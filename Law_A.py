import numpy as np 
import matplotlib.pyplot as plt 

x_max = 5
f = 10
fs = 100
muy = 255
n = np.arange(1,51,1)
V = x_max
A = 87.56
x_n = []
y_n = []
z_n = []
for i in n:
	x_n.append(x_max*np.sin(2*np.pi*i*f/fs))
# print(x_n)
for k in range(0,50):
	if (np.abs(x_n[k]) <= V/A):
		y_n.append(A*np.abs(x_n[k])*np.sign(x_n[k])/(1+np.log(A)))
		# if(y_n[k]>=0):
		# z_n.append(np.abs(y_n[k])*(1+np.log(A))/A)
		# else:
		# 	z_n.append(-y_n[k]*(1+np.log(A))/A)
	# elif (V/A <= np.abs(x_n[k])):
	else:
		y_n.append(V*(1+np.log(A*np.abs(x_n[k])/V))*np.sign(x_n[k])/(1+np.log(A))) 
		# if(y_n[k]>=0):
		# z_n.append((np.exp(np.abs(y_n[k])*(1+np.log(A))/V-1))*V/A)
		# else:
		# 	z_n.append(-V*(np.exp(y_n[k]*(1+np.log(A))/V-1))/A)


for k in range(0,50):
	if (np.abs(y_n[k]) <= V/(1+np.log(A))):
		z_n.append(np.abs(y_n[k])*(1+np.log(A))/A)
	# elif((V/(1+np.log(A)))<=np.abs(y_n[k])):
	else:
		z_n.append((np.exp(np.abs(y_n[k])*(1+np.log(A))/V-1))*V/A)

plt.subplot(3,1,1)
plt.plot(n, x_n)

plt.subplot(3,1,2)
plt.plot(n, y_n)

plt.subplot(3,1,3)
plt.plot(n, z_n)

plt.savefig("Law_A")
plt.show()