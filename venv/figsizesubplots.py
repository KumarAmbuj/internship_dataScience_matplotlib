import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y=x**2

fig,axes= plt.subplots(nrows=2,ncols=1, figsize=(8,2))
axes[0].plot(x,y)
axes[0].set_xlabel('xlabel')
axes[0].set_ylabel('ylabel') 
axes[0].set_title('TITLE')

axes[1].plot(y,x)
axes[1].set_xlabel('xlabel')
axes[1].set_ylabel('ylabel')
axes[1].set_title('TITLE')


plt.show()