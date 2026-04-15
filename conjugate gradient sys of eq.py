#solves system of equations by conjugate gradient
#warning: this method can only be used for symmetric matrices
#or for positive-definite matrices

import numpy as np

X=np.array([[4,100,3],[4,-1,3],[-2,1,2]],
           dtype=float)
A=np.dot(X.T,X)
x=np.array([0,0,0],dtype=float)
f=np.array([7,-21,19],dtype=float)
r=f-(X.T@(X@x))
p=r.copy()
it=0
maxit=100

while True:
    it+=1
    inter=X@p #these 2 intermediate steps are used to accelerate
    inter2=X.T@inter #the code and reduce memory use if A is too large
    a=np.inner(r,r)/(np.dot(p,inter2))
    x+=a*p
    r_new=r-a*inter2
    if np.max(abs(r_new))<1e-4:
        break
    else:
        b=np.inner(r_new,r_new)/np.inner(r,r)
        p=r_new+b*p
        r=r_new

print(it)
print(x)
print(np.dot(A,x))