import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

n = int(sys.argv[1])

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

e = 0.3
m = 128
ns = 64

x,w = np.polynomial.legendre.leggauss(ns)

c = np.zeros([n])
d = np.zeros([n])

for i in range(n):
    d[:] = 0.0 ; d[i] = 1.0
    p = np.polynomial.legendre.legval(x,d)
    c[i] = (i+0.5)*np.sum(w[:]*y(x[:],e)*p[:])

ym = np.zeros([m])

xm = np.linspace(-1.0,1.0,m)
ym = np.polynomial.legendre.legval(xm,c)

ax.plot(xm,y(xm,e),'-k',linewidth=1)
ax.plot(xm,ym,'-r',linewidth=1,label=r'$N='+str(n)+'$')

ax.set_ylim([0,1.1*y(0,e)])
ax.set_xlim([-1,1])
ax.legend(loc=1)

print('-> fit_leg_spectral {:d}'.format(n))

plt.tight_layout()
plt.savefig('fit_leg_spec'+str(n)+'.pdf')
