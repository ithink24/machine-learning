#beta is given to be 1. (in the differentiation step, beta gets cancelled)
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3])
y = np.array([1.2,1.9,3.2])

def parameters(x,y):
    P = x.sum()
    Q = y.sum()
    R = (x*x).sum()
    S = (x*y).sum()
    T = len(x)
    
    w0 = (R*Q - P*S)/(R*T - P*P)
    w1 = (Q - (T*w0))/P
    return w1,w0 
#slp is slope and  intr is intercept
slp, intr = parameters(x,y)

abline_values = [slp * i + intr for i in x]
plt.scatter(x,y)
plt.plot(x, y)
plt.plot(x, abline_values, 'g')
plt.show()
