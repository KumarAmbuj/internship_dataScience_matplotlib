import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
fig=plt.figure()
def create_plot():
    xs=[]
    ys=[]
    for i in range(10):
        x=i
        y=random.randrange(10)
        xs.append(x)
        ys.append(y)
        return xs,ys
ax1=fig.add_subplots(211)
ax2=fig.add_subplots(212)
plt.show()