import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y=x**2

fig= plt.figure()
axes = fig.add_axes([0.4, 0.4 , 0.5, 0.5])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')

plt.show()