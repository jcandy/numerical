import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

n = int(sys.argv[1])

rc('text',usetex=True)
rc('font',size=18)

#======================================
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
#=====================================

def y(x,e):
    y = 1.0/(x**2+e**2)
    return y

e = 0.3
m = 256

for mode in ['equal','legendre','chebyshev']:
    if mode == 'legendre':
        x,w = np.polynomial.legendre.leggauss(n)
        color = 'blue'
    elif mode == 'equal':
        x = np.linspace(-1.0,1.0,n)
        color = 'red' 
    elif mode == 'chebyshev':
        x = np.cos((2*np.arange(n)+1)/(2.0*n)*np.pi)
        color = 'magenta'
        
    a = np.zeros([n,n])
    b = np.zeros([n])
    ym = np.zeros([m])

    for i in range(n):
        b[i] = y(x[i],e)
        for j in range(n):
            a[i,j] = x[i]**j
    
    c = np.linalg.solve(a,b)

    xm=np.linspace(-1.0,1.0,m)

    for j in range(n):
        ym[:] = ym[:]+c[j]*xm[:]**j

    ax.plot(xm,ym,linewidth=1,label=r'$N='+str(n)+'\\mathrm{~'+mode+'}$',color=color)

ax.plot(xm,y(xm,e),'-k',linewidth=1)
ax.plot(x,y(x,e),'o',color='k')

ax.set_ylim([0,1.1*y(0,e)])
ax.set_xlim([-1,1])
ax.legend()

plt.tight_layout()
plt.savefig('fit3_'+str(n)+'.pdf')

