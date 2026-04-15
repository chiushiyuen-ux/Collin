# using the laplace formula o find the determinant of a n*n matrix
import numpy as np
from copy import deepcopy

#example matrix
A=np.array([[1,2,3],[4,11,6],[7,8,10]])

def lapl(A):
    A=deepcopy(A)
    dim=A.shape[0]
    det=0
    for i in range(dim):
        mask=np.ones(A.shape[1],dtype=bool)
        mask[i]=False
        minor=A[1:,mask]
        det+=A[0,i]*lapl(minor)
    return det

A_det=lapl(A)
print(np.linalg.det(A))
print(A_det)