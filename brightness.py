import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

B1 = []
B2 = []
B3 = []

img = mpimg.imread('chunk-of-interference-patern.PNG')
plt.imshow(img)
plt.show()

img_lum = img[:][:][0]
plt.imshow(img_lum)
plt.show()

d = np.linspace(0, (len(img[0]) - 1) * 0.016, len(img[0]))
for i in img_lum:
    B1.append(i[0])
    B2.append(i[1])
    B3.append(i[2])

plt.plot(d, B2, color = 'black', label = "intensité lumineuse en fonction de la distance")
plt.xlabel("distance (en cm)")
plt.ylabel("intensité lumineuse")
plt.legend()
plt.show()
