#sor, empty sqr potential

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from mpl_toolkits.mplot3d import Axes3D


def sor(V,rho,omega):
    V1=deepcopy(V)
    rho=deepcopy(rho)
    row,col=V.shape
    for i in range(1,row-1):
        for j in range(1,col-1):
            V1[i,j]=(1-omega)*V[i,j]+1.8*(rho[i,j]/4+0.25*(V1[i+1,j]+V1[i-1,j]+V1[i,j+1]+V1[i,j-1]))
    return V1

i=100
V=np.zeros([2*i+1,2*i+1])
rho=np.zeros(V.shape)
rho[(int(0.5*i),int(1.5*i)),int(0.5*i):int(1.5*i)]=10*np.ones([2,i])
rho[int(0.5*i):int(1.5*i),(int(0.5*i),int(1.5*i))]=10*np.ones([2,i]).T
it=0
omega=1.8
while True:
    V1=sor(V,rho,omega)
    it+=1
    print(it)
    if np.max(np.abs(V1-V))<1e-5:
        break
    V=V1
    
x=np.linspace(0,i,2*i+1)
y=np.linspace(0,i,2*i+1)
X,Y=np.meshgrid(x,y)
fig=plt.figure()
ax=fig.add_subplot(121,projection='3d')
ax.plot_surface(X,Y,V,cmap='viridis')
ax.set_title(f'grid size: {i}x{i}, iterations: {it}')
ax1=fig.add_subplot(122,projection='3d')
ax1.plot_surface(X,Y,rho,cmap='viridis')
ax1.set_title('rho')
plt.show()