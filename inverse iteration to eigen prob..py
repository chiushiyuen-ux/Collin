#uses the inverse iteration with Rayleigh quotient to find an eigen pair
#of a sqr matrix.

import numpy as np

def GS(A,x,f):#in the form Ax=f
    dim=A.shape[0]
    for i in range(dim):
        ans=0 #ans=A[i,j]*x[j] so it should renew when starting a new row
        for j in range(dim):
            if i!=j:
                ans+=np.dot(A[i,j],x[j])
        x[i]=(f[i]-ans)/A[i,i]          
    return x

def inv_it(A,lam,f):
    dim=A.shape[0]
    x=np.ones(dim)
    B=A-lam*np.eye(dim)
    while True:
        x_new=GS(B,x,f)
        if np.allclose(x,x_new,rtol=1e-6):
            break
    x=x_new
    x/=np.linalg.norm(x)
    z=np.dot(A,x)
    lam=np.dot(x,z)/np.dot(x,x)
    return lam,x

#matrix in question
A=np.array([[2,1,1],[4,-6,0],[-2,7,2]],
           dtype=float)
dim=A.shape[0]

print(f'there should be {A.shape[0]} eigenvalues')
#initial guess for eigenpair
lam=-1
f=np.ones(dim)

while True:
    lam_new,f_new=inv_it(A,lam,f)
    if np.allclose(f,f_new,rtol=1e-6):
        break
    lam,f=lam_new,f_new
print(lam,f)
    
