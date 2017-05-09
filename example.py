import scipy.optimize
import numpy as np
A = np.array([[2, 3],
             [1, 2],
             [-9, 8]])
b = np.array([7,8,9])
x = np.linalg.lstsq(A, b)[0]
print x
print (np.dot(A, x) - b)
def func(x):
    bd = np.dot(A, x) - b
    return np.dot(bd, bd)
x0=[0.0, -1.0]
res=scipy.optimize.minimize(fun=func, x0=x0, method='L-BFGS-B')
print res
