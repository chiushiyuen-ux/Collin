#estimate the eigenvalues and eigenvectors
#of the matrix A by power method,then checck the answers
#by calculating P^-1*D*P=A

import numpy as np

def pow_method(A,x):
    x=np.dot(A,x)
    x/=np.linalg.norm(x)
    lam=np.dot(x,np.dot(A,x))/np.dot(x,x)
    return lam,x


def Gram_Schmit(v1,v2):
    v1=v1.copy()
    v2=v2.copy()
    v1/=np.linalg.norm(v1)
    v2-=np.dot(v1,v2)*v1
    v2/=np.linalg.norm(v2)
    return v1,v2

def find_eigen(A,x,tol=1e-6):
    lam,x=pow_method(A,x)
    while not np.linalg.norm(np.dot(A,x)-lam*x,2)<tol:
        lam,x=pow_method(A,x)
    return lam,x


A=np.array([[100,2,3,3,20],[2,21,6,7,8],[3,6,31,11,12],[4,8,12,41,16],[5,10,15,20,51]],
            dtype=float)
dim=A.shape[0]
x=np.array([1,0,0,0,0],dtype=float)
lam=np.zeros(dim)
V=np.zeros((dim,dim))
for i in range(dim):
    lam_i, x_i = find_eigen(A, x)
    lam[i] = lam_i
    V[:,i] = x_i
    x_i=x_i.reshape(-1,1)
    A -= lam_i * np.outer(x_i, x_i)
print("Eigenvalues:", lam)
print("Eigenvectors:")
print(V)

print(np.dot(A,V[:,4])-lam[4]*V[:,4])