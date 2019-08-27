import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

n = int(sys.argv[1])
mode = sys.argv[2]

def y(x):
    y = np.exp(np.pi*x)
    return y

def yp(x):
    yp = np.exp(np.cos(np.pi*x))
    return yp

x = np.linspace(-1.0,1.0,n)
dx = x[1]-x[0]

ws = np.zeros(n)
for i in range(n//2):
    ws[2*i] = 2.0/3.0
    ws[2*i+1] = 4.0/3.0

ws[0] = 1.0/3.0 ; ws[-1] = ws[0]

wt = np.ones(n)

wt[0] = 1.0/2.0 ; wt[-1] = wt[0]

if mode == 'np':
    e = (np.exp(np.pi)-np.exp(-np.pi))/np.pi
    e1 = dx*np.sum(wt*y(x))-e
    e2 = dx*np.sum(ws*y(x))-e
else:
    e=2.532131755504017
    e1 = dx*np.sum(wt*yp(x))-e
    e2 = dx*np.sum(ws*yp(x))-e

print("{:d} & {:.3e} & {:.3e} \pause".format(n,e1,e2)) 
