import numpy as np
import matplotlib.pyplot as plt

f = np.poly1d([2,3])
print ("f = ",f)

#p = np.poly1d([1,2,3], variable='z')
#print(p)

p = np.poly1d([-1, 7, -7])
x = np.linspce(-50:50:1)
y = p(x)
plt.plot(x, y)
plt.show()