#plot the function of f(z), where z is complex
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,101)
y=x.copy()
X,Y=np.meshgrid(x,y)

Rez=X**2-Y**2
Imz=2*X*Y

fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.contour(X,Y,Rez)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Rez')
ax2.contour(X,Y,Imz)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Imz')
plt.show()