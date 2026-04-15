# do the lagrange interpolation and see if it matches the NDD

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

y=np.array([0,2,0.8,0.23,0.5,0.89,1.23,-0.23,-1.4])
n=len(y)
x=np.linspace(0,n,n)

def inter(xpts,ypts,yvalue):
    x=deepcopy(xpts)
    y=deepcopy(ypts)
    n=len(x)
    
    f=0
    for i in range(n):
        inter=1
        for j in range(n):
            if j!=i:
                inter*=(yvalue-y[j])/(x[i]-x[j])
        f+=inter*y[i]
    return f

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,y,'.')
plt.show()