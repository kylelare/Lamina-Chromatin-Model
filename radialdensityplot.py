import argparse
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from collections import Counter

parser = argparse.ArgumentParser(description='GAMinG - Genome Architecture MiChroM input files for Gromacs',prog='GAMinG')
parser.add_argument('-tx', action='store', default = 1.0, dest ='arg_tx')
parser.add_argument('-cx', action='store', default=2.0,dest ='arg_cx')
parser.add_argument('-dSR', action='store', default=3.0,dest ='arg_dSR')
arguments = parser.parse_args()

a1vals = np.loadtxt('iia1-{}.txt'.format(arguments.arg_cx))
a2vals = np.loadtxt('iia2-{}.txt'.format(arguments.arg_cx))
b1vals = np.loadtxt('iib1-{}.txt'.format(arguments.arg_cx))
b2vals = np.loadtxt('iib2-{}.txt'.format(arguments.arg_cx))
b3vals = np.loadtxt('iib3-{}.txt'.format(arguments.arg_cx))
navals = np.loadtxt('iina-{}.txt'.format(arguments.arg_cx))

print(xbins2)
plt.plot(xbins2,a1vals,label="A1")
plt.plot(xbins2,a2vals,label="A2")
plt.plot(xbins2,b1vals,label="B1")
plt.plot(xbins2,b2vals,label="B2")
plt.plot(xbins2,b3vals,label="B3")
plt.plot(xbins2,navals,label="NA")
plt.legend(prop={'size': 15})
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.ylim(0,1)
plt.title("Radial Density Plot")
plt.xlabel("Radial Distance [$\sigma]")
plt.ylabel("Radial Density [1/$\sigma$**3]")
plt.savefig('/scratch/kl76/data/FISchr21/radialdensity-onlyA-{}.png'.format(arguments.arg_cx))

