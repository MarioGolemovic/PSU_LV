
import matplotlib.pyplot as plt 
import numpy as np
import skimage.io

img=skimage.io.imread('tiger.png', as_gray=True)
rows,cols=img.shape

img_new=np.zeros((rows,cols))
x=int(cols/4)

for i in range(rows):
  for j in range(x, 2*x):
      img_new[i][j]=img[i][j]
        

plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

plt.figure(2)
plt.imshow(img_new, cmap='gray', vmin=0, vmax=255)

plt.show()
