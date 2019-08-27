import sys
import numpy as np
import numpy.polynomial as poly
import matplotlib.pyplot as plt
from matplotlib import rc

n = int(sys.argv[1])

rc('text',usetex=True)
rc('font',size=18)

#======================================
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
#=====================================

m = 256
c = np.zeros(n)
c[-1] = 1.0

xm = np.linspace(-1.0,1.0,m)

ym = poly.legendre.legval(xm,c)
ax.plot(xm,ym,'-b',linewidth=2,label=r'$P_{'+str(n-1)+'}$')

ym = poly.chebyshev.chebval(xm,c)
ax.plot(xm,ym,'-r',linewidth=2,label=r'$T_{'+str(n-1)+'}$')
    
ax.plot(xm,0*ym,'--k',linewidth=1)

ax.set_xlim([-1,1])
ax.set_ylim([-1.01,1.01])
ax.legend()

plt.tight_layout()
plt.savefig('poly'+str(n)+'.pdf')
