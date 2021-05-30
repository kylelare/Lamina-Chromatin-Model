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

dx = 0.2 #difference in volume shells for radial density calculations
def v(r):
        return (float(r**3)*(math.pi)*(4)*1/3)-(float((r-dx)**3)*(math.pi)*(4)*1/3)


ii = 79808
#ii = 78703
a1=np.loadtxt('a1-{}.txt'.format(arguments.arg_cx))
a1 , z = np.histogram(a1, bins=62, range=[1.2,13.6])
print(z)
print(a1)
sum = 0
for i in a1:
	sum += i
print(sum)
a1v = a1.tolist()
zz = z.tolist()
a1rad = open('iia1-{}.txt'.format(arguments.arg_cx), 'w')
for (a1val, q) in zip(a1v, zz):
	value = ((a1val)/((v(q))*ii))
	print(q)
        a1rad.write(str(value/103) + '\n')
a1rad.close()

a2=np.loadtxt('a2-{}.txt'.format(arguments.arg_cx))
a2 , z = np.histogram(a2,  bins=62, range=[1.2,13.6])
print(a2)
a2v = a2.tolist()
zz = z.tolist()
a2rad = open('iia2-{}.txt'.format(arguments.arg_cx), 'w')
for (a2val, q) in zip(a2v, zz):
        value = ((a2val)/((v(q))*ii))
	a2rad.write(str(value/685) + '\n')
a2rad.close()

b1=np.loadtxt('b1-{}.txt'.format(arguments.arg_cx))
b1 , z = np.histogram(b1, bins=62, range=[1.2,13.6])
print(b1)
b1v = b1.tolist()
zz = z.tolist()
b1rad = open('iib1-{}.txt'.format(arguments.arg_cx), 'w')
for (b1val, q) in zip(b1v, zz):
        value = ((b1val)/((v(q))*ii))
	b1rad.write(str(value/190) + '\n')
b1rad.close()

b2=np.loadtxt('b2-{}.txt'.format(arguments.arg_cx))
b2 , z = np.histogram(b2, bins=62, range=[1.2,13.6])
print(b2)
b2v = b2.tolist()
zz = z.tolist()
b2rad = open('iib2-{}.txt'.format(arguments.arg_cx), 'w')
for (b2val, q) in zip(b2v, zz):
        value = ((b2val)/((v(q))*ii))
	b2rad.write(str(value/1596) + '\n')
b2rad.close()

b3=np.loadtxt('b3-{}.txt'.format(arguments.arg_cx))
b3 , z = np.histogram(b3, bins=62, range=[1.2,13.6])
print(b3)
b3v = b3.tolist()
zz = z.tolist()
b3rad = open('iib3-{}.txt'.format(arguments.arg_cx), 'w')
for (b3val, q) in zip(b3v, zz):
        value = ((b3val)/((v(q))*ii))
	b3rad.write(str(value/62) + '\n')
b3rad.close()

na=np.loadtxt('na-{}.txt'.format(arguments.arg_cx))
na , z = np.histogram(na, bins=62, range=[1.2,13.6])
print(na)
nav = na.tolist()
zz = z.tolist()
narad = open('iina-{}.txt'.format(arguments.arg_cx), 'w')
for (naval, q) in zip(nav, zz):
        value = ((naval)/((v(q))*ii))
	narad.write(str(value/40) + '\n')
narad.close()

