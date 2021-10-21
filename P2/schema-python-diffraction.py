import matplotlib.pyplot as plt
import numpy as np

T = 40
n = 1000

x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)

X, Y = np.meshgrid(x, y)

def func(x, y):
    S = -np.sin((T/(2*np.pi))*y)*(np.sign(y)-1)/2 +np.exp(-(x/(0.2*y))**2)*np.sin((T/(2*np.pi))*np.sqrt((x**2 + y**2)))*(np.sign(y)+1)/2
    return(S)

plt.imshow(func(X, Y), cmap='hot')
plt.show()
