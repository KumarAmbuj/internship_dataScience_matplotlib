import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
x=[1,2,3,4,5,6,7,8,9,10]
y=[5,6,7,8,2,5,6,3,7,2]
z=[1,2,6,3,2,7,3,3,7,2]
ax.plot_wireframe(x,y,z)
plt.show()