#performs interpoltion with NDD table

import numpy as np
import matplotlib.pyplot as plt

def inter(x,xpts,ypts):
    #uses interpolation to find the value of f(x)
    xpts=xpts.copy()
    ypts=ypts.copy()
    dim=len(xpts)

    NDD=np.zeros([dim,dim+1]) #set up the NDD table
    NDD[:,0]=xpts
    NDD[:,1]=ypts
    for j in range(1,dim+1): #1 to 4
        for i in range(dim-j): # 2 to 0
            NDD[i,j+1]=(NDD[i+1,j]-NDD[i,j])/(xpts[j+i]-xpts[i])

    in_coef=NDD[0,1:] #NDD coefficients
    ans=in_coef[0] #output the interpolated value p(x)
    term=1
    for k in range(1,dim):
        term*=(x-xpts[k-1])
        ans+=in_coef[k]*term
    return ans,in_coef,NDD

xpts,ypts=[0,1,3,6,8,10],[0,2,0.23,1.23,-1.4,0]
xplot=np.linspace(0,6,101)
yplot,in_coef,NDD=inter(xplot,xpts,ypts) #plot graph
print(in_coef)
print(NDD)

def f(x): #extra: find x where p(x)=100
    global xpts,ypts
    return inter(x,xpts,ypts)[0]

d,u=0,10
err=1
tol=1e-6
while abs(err)>tol:
    m=(d+u)/2
    if f(m)*f(u)>0:
        u=m
    else:
        d=m
    err=(u-d)

print(inter(4.2,xpts,ypts)[0])

fig,ax=plt.subplots() #plot graph of p(x)
ax.plot(xplot,yplot)
ax.plot(xpts,ypts,'kx')
plt.show()