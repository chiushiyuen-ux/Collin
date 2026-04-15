#use the householder method to transform matrices into tridiag

import numpy as np 
from copy import deepcopy

def householder(A):
    A1=deepcopy(A)
    dim=A1.shape[0]
    if (A1.T!=A1).all():
        print('A is not symetric, cannot perform householder method')
        flag=1
    else:
        flag=0
    if flag==0:
        for i in range(dim-1):
            P=np.eye(dim,dtype=complex)
            x=A[i+1:,i]
            xnorm=np.linalg.norm(x)
            u=x-xnorm*P[:dim-i-1,i]
            u/=np.linalg.norm(u) #normalize u
            P[i+1:,i+1:]-=2*np.outer(u,u)
            A=P.dot(A).dot(P)
    return A

A=np.array([[2,1,3,4],[1,5,2,6],[3,2,7,1],[4,6,1,8]],dtype=complex)
dim=A.shape[0]

A1=householder(A)


P=np.eye(4,dtype=complex)
x=A[1:,0]
xnorm=np.linalg.norm(x)
u=x-xnorm*P[:3,0]
u/=np.linalg.norm(u) #u normalized
P[1:,1:]-=2*np.outer(u,u)
A=P.dot(A).dot(P)

print(A1)