#solves the advective equation with boundary conditions by finite difference
#PDE: 4ut-3ux=0-->ut=(3/4)*ux, u(0,x)=x**3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#exact sol
v=3/4
a,b=0,30
delt=1
delx=abs(v)*2*delt
tN=int((b-a)/delt)
xN=int((b-a)/delx)
tpts=np.linspace(a,b,tN)
xpts=np.linspace(a,b,xN)
T,X=np.meshgrid(tpts,xpts)
U=(3*T+4*X)**3/64

#approx sol
def Lax(F,v,delt,delx):
    F = F.copy()
    F_new = F.copy()
    xN, tN = F.shape
    for n in range(tN-1):
        for i in range(1, xN-1):
            F_new[i,n+1]=-v*delt*(F[i+1,n]+F[i-1,n])/(2*delx)-(F[i+1,n]-2*F[i,n]+F[i-1, n])/2+delt*F[i,n]
        F[:, n+1] = F_new[:, n+1]
    return F_new

F=np.zeros([xN,tN])
F[:,0]=xpts**3
for t in tpts[:-1]:
    F=Lax(F,v,delt,delx)

fig=plt.figure()
ax1=fig.add_subplot(121,projection='3d')
ax1.plot_surface(T,X,F)
ax1.set_xlabel('t')
ax1.set_ylabel('x')
ax1.set_zlabel('F(t,x)')
ax1.set_title('approx')
ax2=fig.add_subplot(122,projection='3d')
ax2.plot_surface(T,X,U)
ax2.set_xlabel('t')
ax2.set_ylabel('x')
ax2.set_zlabel('U(t,x)')
ax2.set_title('exact')
plt.show()