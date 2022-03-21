import numpy as np
import matplotlib.pyplot as plt
x=[1.0, 2.0, 3.0, 3.0, 1.0]
y=[1.0, 2.0, 2.0, 1.0, 1.0]
plt.plot(x, y, 'b.-', linewidth=1)
plt.xlabel('x-os')
plt.ylabel('y os')
plt.title('primjer 1')
plt.xlim(0,4)
plt.ylim(0,4)
plt.show()
