# using the newton's method to solve nonlinear eq.

def f(x):
    return x**2

def df(x):
    return 2*x

x=100
err=1
tol=1e-6
it=1

while True:
    it+=1
    p=df(x)
    x_new=x-f(x)/p
    print(x_new)
    if abs(err)<tol:
        break
    else:
        err=x_new-x
        x=x_new

print(f'{it} iterations')
print(x_new)