
import matplotlib.pyplot as plt 
import numpy as np
import skimage.io

img=skimage.io.imread('tiger.png', as_gray=True)
rows,cols=img.shape
mar=int (rows/10)
lar=int (cols/10)
img_new=np.zeros((mar,lar))

for i in range(mar):
  for j in range(lar):
        img_new[i][j]=img[10*i][10*j]

plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

plt.figure(2)
plt.imshow(img_new, cmap='gray', vmin=0, vmax=255)

plt.show()
