#solves the BVP y''+2y'+y=0, y(0)=1,y(1)=0
#compare with exact sol y=(1-x)*exp(-x)

import numpy as np
import matplotlib.pyplot as plt

def tridiag(up,mid,down,dim):
    D=np.zeros([dim,dim])
    for i in range(dim):
        for j in range(dim):
            if i==j:
                D[i,j]=mid
            elif i-1==j:
                D[i,j]=down
            elif i+1==j:
                D[i,j]=up
    return D

def GS(A,x,f):#in the form of Ax=f
    dim=A.shape[0]
    for i in range(dim):
        ans=0
        for j in range(dim):
            if i!=j:
                ans+=np.dot(A[i,j],x[j])
        x[i]=(f[i]-ans)/A[i,i]
    return x
N=100
h=1/N

x=np.linspace(0,1,N+1)#exact sol
yexact=(1-x)*np.exp(-x)

y=np.zeros([N+1,1])#approx sol first trial
f=np.zeros([N+1,1])
f[0],f[-1]=1,0
D2=tridiag(1,-2,1,N+1)/h**2
D1=tridiag(-1,0,1,N+1)/(2*h)
I=np.eye(N+1)
while True:
    y_new=GS(D2-2*D1,y,f)
    if np.allclose(y,y_new,rtol=1e-2):
        break
    y=y_new

fig,ax=plt.subplots()
ax.plot(x,y,label='approx sol')
ax.plot(x,yexact,label='exact sol')
fig.legend()
fig.show()
