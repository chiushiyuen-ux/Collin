# perform linear regression (least squares) with 8 sets of data

import numpy as np
import matplotlib.pyplot as plt

def GS(A,x,f):#in the form Ax=f
    dim=A.shape[0]
    for i in range(dim):
        ans=0 #ans=A[i,j]*x[j] so it should renew when starting a new row
        for j in range(dim):
            if i!=j:
                ans+=np.dot(A[i,j],x[j])#if x and f have shapes (dim,>1)
        x[i]=(f[i]-ans)/A[i,i]          #replace index [i] with [:,i], [j] with [:,j]
    return x

samples=np.array([[1,2,3,4,5,6,7,8],
                  [11.79,9.39,6.79,4.75,3.82,2.60,1.70,1.25]])
row,col=samples.shape

def lstsq(A):
    A=A.copy()
    row,col=A.shape
    X=np.ones([row,col+1])
    X[:,1:]=A
    f=A[:,-1]
    beta=np.ones([max(row,col+1)])
    while True:
        beta_new=GS(np.dot(X.T,X),beta,np.dot(X.T,f))
        if np.allclose(beta,beta_new,rtol=1e-6):
            break
        beta=beta_new
    return list(beta[:2])  


m,b=lstsq(samples)
xpts=np.linspace(1,8,8)
ypts=np.dot(m,xpts)+b

fig,ax=plt.subplots()
ax.plot(xpts,np.log(ypts))
for i in range(col):
    ax.plot(samples[0,i],samples[1,i])
ax.set_xlabel('independent data')
ax.set_ylabel('dependent data')
plt.show(block=True)