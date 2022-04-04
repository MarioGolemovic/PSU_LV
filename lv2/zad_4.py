

import matplotlib.pyplot as plt 
import numpy as np
import skimage.io

img=skimage.io.imread('tiger.png', as_gray=True)
img_new=img.copy()
rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
         if img[i][j]>220:
            img_new[i][j]=255
         else: 
            img_new[i][j]+=25


plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.figure(2)
plt.imshow(img_new, cmap='gray', vmin=0, vmax=255)
plt.show()
