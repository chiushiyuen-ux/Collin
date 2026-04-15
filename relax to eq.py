#use the relaxation method (or called fix point iteration) to solve equations

import numpy as np

def f(x):
    return 0.5*np.tan(x)

x1=0.5
it=0
while True:
    it+=1
    x1_new=f(x1)
    print(x1)
    if abs(x1_new-x1)<1e-6:
        break
    x1=x1_new
print(x1_new,it)