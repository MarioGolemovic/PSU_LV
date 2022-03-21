import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6,), delimiter=",", skiprows=1)

mpg=data[:,0]
hp=data[:,3]
wt=data[:,5]
s= [3*n for n in range(len(wt))]
print("min mpg:", np.min(mpg))
print("max mpg:", np.max(mpg))
print("mean mpg:", np.mean(mpg))
plt.scatter(wt,hp, s=s)
plt.xlabel('wt')
plt.ylabel('mpg')
plt.show()