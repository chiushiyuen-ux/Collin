#same ODE as 'rk4 without err', but introduce adaptive method
#ddphi=-g*sin(phi)/R
import numpy as np
import matplotlib.pyplot as plt#2y''+18y=6tan(3t)

gamma=2

def u(r,t):
    u,du=r
    du=r[1]
    ddu=(-np.sqrt(10)*r[0]**2-1.5*r[0]+2*7.3*r[1])/(1-7.3)
    return np.array([du,ddu])

def rk4(r,t,h):
    k1=h*u(r,t)
    k2=h*u(r+0.5*k1,t+0.5*h)
    k3=h*u(r+0.5*k2,t+0.5*h)
    k4=h*u(r+k3,t+h)
    rk=r+(k1+2*k2+2*k3+k4)/6
    return rk

alpha,beta,niu=1.5,np.sqrt(10),7.3
a,b=0,10
h=10
r=np.array([2,5])
rtol=1e-6
t=a
tpts=[t]
upts,dupts=[r[0]],[r[1]]
ctr=0
vlinelist=[]

while t < b:
    ctr += 1
    while True:
        r0 = rk4(r,t,h)
        r1 = rk4(r0,t+h,h)
        r2 = rk4(r,t,2*h)
        if np.isclose(r1[0], r2[0], rtol=0) == 0:
            rho = 30*h*rtol/abs(r1[0] - r2[0])
        else:
            rho = 10000
        if rho >= 1:
            tpts.extend([t+h, t+2*h])
            upts.extend([r0[0], r1[0]])
            dupts.extend([r0[1], r1[1]])
            t += 2*h
            r = r1
            h *= min(rho**0.25, 2.0)
            break
        h *= rho**0.25
    if (ctr % 10) == 0:
         vlinelist.append(t)
    
   
fig,ax=plt.subplots()
ax.plot(upts,dupts)
ax.set_xlabel('u')
ax.set_ylabel('v')
plt.show()
