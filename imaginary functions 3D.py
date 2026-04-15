#plot the function of f(z), where z is complex
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(-10,10,101)
y=x.copy()
X,Y=np.meshgrid(x,y)

Rez=X**2-Y**2
Imz=2*X*Y

fig=plt.figure()
ax1=fig.add_subplot(121,projection='3d')
ax2=fig.add_subplot(122,projection='3d')
ax1.plot_surface(X,Y,Rez)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('Rez')
ax2.plot_surface(X,Y,Imz)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('Imz')
fig.show()
