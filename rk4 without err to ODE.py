#DDP
import numpy as np
import matplotlib.pyplot as plt

def f(r,t,arg):
    miu,a,w0=arg
    v=r[1]
    a=miu*(a**2-r[0]**2)*r[1]-w0**2*r[0]
    return np.array([v,a])

a,b,h=0,10,0.05
N=int((b-a)/h)
tpts=np.linspace(a,b,N)
r=[1,0]
xpts1=[r[0]]
arg1=(1,2,1)    # crtitcal damping
arg2=(3,2,2)    # underdamping
arg3=(0.5,2,2)  # overdamping`
for t in tpts[:-1]:
    k1=h*f(r,t,arg1)
    k2=h*f(r+0.5*k1,t+0.5*h,arg1)
    k3=h*f(r+0.5*k2,t+0.5*h,arg1)
    k4=h*f(r+k3,t+h,arg1)
    r+=(k1+2*k2+2*k3+k4)/6
    xpts1.append(r[0])
    
r=[1,0]
xpts2=[r[0]]
for t in tpts[:-1]:
    k1=h*f(r,t,arg2)
    k2=h*f(r+0.5*k1,t+0.5*h,arg2)
    k3=h*f(r+0.5*k2,t+0.5*h,arg2)
    k4=h*f(r+k3,t+h,arg2)
    r+=(k1+2*k2+2*k3+k4)/6
    xpts2.append(r[0])
    
r=[1,0]
xpts3=[r[0]]
for t in tpts[:-1]:
    k1=h*f(r,t,arg3)
    k2=h*f(r+0.5*k1,t+0.5*h,arg3)
    k3=h*f(r+0.5*k2,t+0.5*h,arg3)
    k4=h*f(r+k3,t+h,arg3)
    r+=(k1+2*k2+2*k3+k4)/6
    xpts3.append(r[0])

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(tpts,xpts1,'b-',label='critical damping')
ax.plot(tpts,xpts2,'r-',label='underdamping')
ax.plot(tpts,xpts3,'g-',label='overdamping')
ax.set_title('Q4')
plt.legend()
plt.show()