#perform integration with adaptive size
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*np.sqrt(1-x**2)

def trap(f,a,b,N,rtol):
    err=1
    h=(b-a)/N
    ans=0.5*(f(a)+f(b))
    for k in range(1,N):
        ans+=f(a+k*h)
    I0=ans*h
    while abs(err)>rtol:
        N*=2
        h*=0.5
        ans=0
        for k in range(1,N,2):
            ans+=f(a+k*h)
        Ifin=0.5*I0+ans*h
        err=(Ifin-I0)/3
        I0=Ifin
    return Ifin

a,b=-1,1
rtol=1e-6
N=10
ans=[]
ans=trap(f,a,b,N,rtol)

print(ans)

xpts=np.linspace(-1,1,101)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(xpts,f(xpts))
plt.show()