# mostly used to find the inverse of matrix

import numpy as np

def GS(A,X,F):#in the form AX=F
    A=A.copy()
    X=X.copy()
    F=F.copy()
    dim=A.shape[0]
    for i in range(dim):
        for j in range(F.shape[1]): #to solve for multiple vectors
            ans=0 #ans=A[i,j]*X[j] so it should renew when starting a new row
            for k in range(dim):
                if i!=k:
                    ans+=np.dot(A[i,k],X[k,j])#if X and F have shapes (dim,>1)
            X[i,j]=(F[i,j]-ans)/A[i,i] #replace index [i] with [:,i], [j] with [:,j]
    return X

A=np.array([[3,0,1,2],[2,3,0,1],[1,2,3,0],[0,1,2,3]],
           dtype=float)#eg matrix checking the code is running
F=np.eye(4,dtype=float)
X=np.zeros(A.shape)

err,tol=1,1e-6
i=0
while err>tol:
    X_new=GS(A,X,F)
    err=abs(np.max(X_new-X))
    i+=1
    X=X_new
    
print('A=',A)
print('Ainv=',X*3)
print(f'{i} iterations')