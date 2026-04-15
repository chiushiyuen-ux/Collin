#solves equation using secant method
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**-3+x*np.exp(-x**2)

x0=-5
it=1
err=1
tol=1e-6
maxit=100

while abs(err)>tol or it<maxit:
    p=(f(x0+1e-5)-f(x0))/(1e-5)
    x_new=x0-f(x0)/p
    it+=1
    err=f(x_new)
    x0=x_new
    print(x_new)

print(f'{it} iterations')
print(x_new,err)