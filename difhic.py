import glob
import itertools
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

dif1 = '/scratch/kl76/data/1.7/0.0/Dist-1.7-0.0-all.dat'
dif2 = '/scratch/kl76/data/1.7/0.2/Dist-1.7-0.2-all.dat'
dif3 = '/scratch/kl76/data/1.7/0.4/Dist-1.7-0.4-all.dat'

a = np.loadtxt(dif1, usecols = range(935), max_rows=935)
b = np.loadtxt(dif2, usecols = range(935), max_rows=935)
c = np.loadtxt(dif3, usecols = range(935), max_rows=935)
d = b - a #weak interaction - no interaction
e = c - a #strong interaction - no interaction
f = c - b #strong interaction - weak interaction

#Plotting the difference between each set of Hi-C matrices
fig, ax = plt.subplots(nrows=2,ncols=2)
p1 = ax[0][0].imshow(d,norm=mpl.colors.SymLogNorm(linthresh = .0001, vmin=-0.15, vmax=.15), cmap="RdBu")
p2 = ax[0][1].imshow(e,norm=mpl.colors.SymLogNorm(linthresh = .0001, vmin=-0.15, vmax=.15), cmap="RdBu")
p3 = ax[1][0].imshow(f,norm=mpl.colors.SymLogNorm(linthresh = .0001, vmin=-0.15, vmax=.15), cmap="RdBu")
p4 = ax[1][1].axis('off')
plt.colorbar(p1,ax=ax[0][0])
plt.colorbar(p2,ax=ax[0][1])
plt.colorbar(p3,ax=ax[1][0])
plt.savefig('/scratch/kl76/data/1.7/Diff-hic-all.png')

""" #Plotting the original maps
vmin = 5e-5
#plt.imshow(e,norm=mpl.colors.LogNorm(vmin=1e-7, vmax=1), cmap="Reds")
fig, ax = plt.subplots(nrows=2,ncols=2)
p1 = ax[0][0].imshow(a,norm=mpl.colors.LogNorm(vmin=vmin, vmax=1), cmap="Reds")
p2 = ax[0][1].imshow(b,norm=mpl.colors.LogNorm(vmin=vmin, vmax=1), cmap="Reds")
p3 = ax[1][0].imshow(c,norm=mpl.colors.LogNorm(vmin=vmin, vmax=1), cmap="Reds")
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
p4 = ax[1][1].axis('off')
#plt.colorbar(p1,ax=ax[0][0])
#plt.colorbar(p2,ax=ax[0][1])
plt.colorbar(p3,ax=ax[1][0])
plt.savefig('/scratch/kl76/data/1.7/Dist-hic-all.png')
"""