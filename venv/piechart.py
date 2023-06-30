import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2

print(x)
print("y is",y)

plt.plot(x,y,'r')
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.show()