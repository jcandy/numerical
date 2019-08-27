import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

mode = sys.argv[1]
n    = int(sys.argv[2])

rc('text',usetex=True)
rc('font',size=18)

#======================================
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
#=====================================

def y(x,e):
    y = 1.0/(x**2+e**2)
    return y

#mode = 'equal'
#mode = 'leg'
#mode = 'cheb'
#n = 11

e = 0.3
m = 128

if mode == 'leg':
    x,w = np.polynomial.legendre.leggauss(n)
elif mode == 'equal':
    x = np.linspace(-1.0,1.0,n)
elif mode == 'cheb':
    x = np.cos((2*np.arange(n)+1)/(2.0*n)*np.pi)

a = np.zeros([n,n])
b = np.zeros([n])
ym = np.zeros([m])

for i in range(n):
    b[i] = y(x[i],e)
    for j in range(n):
        a[i,j] = x[i]**j
    
c = np.linalg.solve(a,b)

print('-> fit_poly {:d}'.format(n))

xm=np.linspace(-1.0,1.0,m)

for j in range(n):
    ym[:] = ym[:]+c[j]*xm[:]**j

ax.plot(xm,y(xm,e),'-k',linewidth=1)
ax.plot(x,y(x,e),'o',color='k')
ax.plot(xm,ym,'--r',linewidth=1,label=r'$N='+str(n)+'$')

ax.set_ylim([0,1.1*y(0,e)])
ax.set_xlim([-1,1])
ax.legend(loc=1)

plt.tight_layout()
plt.savefig('fit_'+mode+str(n)+'.pdf')

