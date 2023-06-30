import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
ax= fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label=' x squared')
ax.plot(x,x)