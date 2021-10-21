import numpy as np
import matplotlib.pyplot as plt


n = 100000
t = np.linspace(0, 5, n)

T = 1  
A1 = 1
A2 = 2

phi = np.pi

def signal(t, A, T, phi):
    S = A*np.cos((2*np.pi*t/T) + phi)
    return(S)

s1 = signal(t, A1, T, 0)
s2 = signal(t, A2, T, 0)
S = []


for i in range(n):
    S.append(s1[i] + s2[i])

plt.plot(t, s1, color='red', label='signal 1')
plt.plot(t, s2, color='blue', label='signal 2')
plt.plot(t, S, color='green', label='signal 1 + signal 2')
plt.xlabel('temps')
plt.ylabel('amplitude')
plt.legend()
plt.show()
