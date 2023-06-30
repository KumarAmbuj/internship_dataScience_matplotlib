import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y=x**2

fig,axes=plt.subplots(nrows=1,ncols=2)
for curax in axes:
    curax.plot(x,y)
    curax.set_xlabel('xlabel')
    curax.set_ylabel('ylabel')
    curax.set_title('Title')
plt.show()

