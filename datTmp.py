import numpy as np
import matplotlib.pyplot as plt

points = np.array([(1, 2), (2, 4), (3, 6), (4, 8)])
# get x and y vectors
x = points[:,0]
y = points[:,1]

print ("x = ",x)
print ("y = ",y)

trend = np.polyfit(x, y, 1)
f = np.poly1d(trend)

# Adding Sangam
print ("trend = ",trend)
print ("f = ",f)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

print ("x_new = ",x_new)
print ("y_new = ",y_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()

#points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])
## get x and y vectors
#x = points[:,0]
#y = points[:,1]
#
## calculate polynomial
#z = np.polyfit(x, y, 3)
#f = np.poly1d(z)
#
## calculate new x's and y's
#x_new = np.linspace(x[0], x[-1], 50)
#y_new = f(x_new)
#
#plt.plot(x,y,'o', x_new, y_new)
#plt.xlim([x[0]-1, x[-1] + 1 ])
#plt.show()
