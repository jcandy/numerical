import sys
import numpy as np
from numpy.polynomial import legendre
import matplotlib.pyplot as plt
from matplotlib import rc

n  = int(sys.argv[1])
nt = int(sys.argv[2])

rc('text',usetex=True)
rc('font',size=18)

#======================================
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f$')
#=====================================

nu = 0.2
dt = 0.1
nm = 128

ax.set_title(r'$\nu \Delta t = '+str(nt*dt*nu)+'$')

a = np.zeros([n,n])
ai = np.zeros([n,n])
b = np.zeros([n,n])
c = np.zeros([n,n])
m = np.zeros([n,n])
f = np.zeros([n])
co = np.zeros([n])
fm = np.zeros([n])

x,w = np.polynomial.legendre.leggauss(n)

f = 1/(0.3**2+x**2)

for i in range(n):
   co[:] = 0.0 ; co[i] = 1.0

   p = np.polynomial.legendre.legval(x,co)

   a[:,i] = p
   m[:,i] = i*(i+1)*p

ai = np.linalg.inv(a)
c = np.matmul(m,ai)

b = np.identity(n)+nu*dt*c
bi = np.linalg.inv(b)

#------

xm = np.linspace(-1.0,1.0,nm)
co = np.matmul(ai,f)
fm = np.polynomial.legendre.legval(xm,co) 
ax.plot(xm,fm,'-k',linewidth=2)

for k in range(nt):
    f = np.matmul(bi,f)

co = np.matmul(ai,f)
fm = np.polynomial.legendre.legval(xm,co) 
ax.plot(xm,fm,'-m',linewidth=1)

plt.savefig('pitch'+str(nt)+'.pdf')
