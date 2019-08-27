import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

n = int(sys.argv[1])

def f(x):
    f = np.exp(-(x)**2)
    return f

rc('text',usetex=True)
rc('font',size=18)

#======================================
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
#=====================================

m = 64

x = np.linspace(-2.1,2.1,m)
for i in range(n):
    xm = np.linspace(-2.1+i,2.1+i,m)
    ax.plot(xm,f(x),'-b')

plt.tight_layout()
plt.savefig('rbf.pdf')
