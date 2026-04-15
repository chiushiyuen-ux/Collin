#use the jacobi method to calculate the root of sys of lin eq
#works iff A is diag. dominant

import numpy as np

def jacobi(A,x,f):
    A=A.copy()
    x=x.copy()
    f=f.copy()
    dim=A.shape[0]
    D=np.zeros([dim,dim])
    invD=D.copy()
    for i in range(dim):
        D[i,i]=A[i,i]
        invD[i,i]=1/A[i,i]
    inter=f-np.dot(A,x)
    x_new=x+np.dot(invD,inter)
    return x_new

A=np.array([[4,-1,1],[4,-8,1],[-2,1,5]],
           dtype=float)#eg matrix checking the code is running
f=np.array([7,-21,15],dtype=float)
dim=A.shape[0]
x=np.array([1,2,2])
it=0
maxit=100

while True:
    it+=1
    x_new=jacobi(A,x,f)
    # use the maximum absolute change as the convergence criterion
    if np.max(np.abs(x_new-x))<1e-4 or it==maxit:
        print(f'{it} iterations')
        break
    x=x_new

print(x)
print(np.dot(A,x))