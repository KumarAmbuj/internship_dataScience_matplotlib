import  matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y=x**2
fig,axes=plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.show()



fig,axes=plt.subplots(nrows=3,ncols=3)
plt.tight_layout()
plt.show()