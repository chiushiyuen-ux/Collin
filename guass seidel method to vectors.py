#uses the guass-seidel method to solve system of linear equations
#start with a 4*4 matrix
#works iff A is +ve def

import numpy as np
def GS(A,x,f):#in the form Ax=f
    A=A.copy()
    x=x.copy()
    f=f.copy()
    dim=A.shape[0]
    for i in range(dim):
        ans=0 #ans=A[i,j]*x[j] so it should renew when starting a new row
        for j in range(dim):
            if i!=j:
                ans+=np.dot(A[i,j],x[j])#if x and f have shapes (dim,>1)
        x[i]=(f[i]-ans)/A[i,i] #replace index [i] with [:,i], [j] with [:,j]
    return x

A=np.array([[1,0,0,0,0],[1/2,1,0,0,0],[1/4,1/2,1,0,0],[1/8,1/4,1/2,1,0],[1/16,1/8,1/4,1/2,1]],
            dtype=float)#eg matrix checking the code is running
f=np.array([1,1,1,1,1],dtype=float)
dim=A.shape[0]
x=np.zeros(5,dtype=float)

it=0
maxit=100

while True:
    x_new=GS(A,x,f)
    it+=1
    if np.allclose(x_new,x,atol=1e-6) or it==maxit:
        print(f"{it} iterations")
        break
    x=x_new
print(x)

print(np.dot(A,x))