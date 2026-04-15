#solves equation by bisection method
import numpy as np

def f(x):
    return -1/x**3+x*np.exp(-x**2)

xu,xd=-100,100.5
it=0
err=1

def bisection(xu,xd):
    it=0
    err=1
    while True:
        it+=1
        xm=xd+(xu-xd)/2
        if f(xu)*f(xm)>0:
            xu=xm
        elif f(xd)*f(xm)>0:
                xd=xm
        err=xu-xd
        if abs(err)<1e-6:
            break
    return xm,it

xm,it=bisection(xu,xd)
print(f'{it} iterations')
print(xm)