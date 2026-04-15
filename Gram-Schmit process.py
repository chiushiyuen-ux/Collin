#given a matrix, orthonomalize the column vectors
#this is also part of the QR factorisation

import numpy as np

#Gram-Schmit process

P=np.eye(4)
P[1,1]=P[2,2]=0.6
P[1,2]=0.8
P[2,1]=-0.8

def orthonormal(A):
    A=A.copy()
    dim=A.shape[0]
    A[:,0]/=np.linalg.norm(A[:,0])
    for i in range(1,dim):
        for j in range(i):
            A[:,i]-=np.dot(A[:,j],A[:,i])*A[:,j]
        A[:,i]/=np.linalg.norm(A[:,i])
    return A

def Gram_Schmit(v1,v2):
    v1=v1.copy()
    v2=v2.copy()
    v1/=np.linalg.norm(v1)
    v2-=np.dot(v1,v2)*v1
    v2/=np.linalg.norm(v2)
    return v1,v2

Q=orthonormal(P)
R=Q.T #Q is unitary, such that np.dot(Q.T,Q)=np.eye
print(np.allclose(Q,P))