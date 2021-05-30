import glob
import itertools
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import argparse
#with open('/scratch/kl76/data/1.2/0.25/run1/Dist-C21-GM12878-0.25-run1.dat') as f:
	#for line in f:
		#row = line.split()
		#print(len(line))
parser = argparse.ArgumentParser(description='GAMinG - Genome Architecture MiChroM input files for Gromacs',prog='GAMinG')
parser.add_argument('-tx', action='store', default = 1.0, dest ='arg_tx')
parser.add_argument('-cx', action='store', default=2.0,dest ='arg_cx')
parser.add_argument('-dSR', action='store', default=3.0,dest ='arg_dSR')
arguments = parser.parse_args()

r1 = '/scratch/kl76/data/{}/{}/run1/Dist-C21-GM12878-{}-run1.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r2 = '/scratch/kl76/data/{}/{}/run2/Dist-C21-GM12878-{}-run2.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r3 = '/scratch/kl76/data/{}/{}/run3/Dist-C21-GM12878-{}-run3.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r4 = '/scratch/kl76/data/{}/{}/run4/Dist-C21-GM12878-{}-run4.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r5 = '/scratch/kl76/data/{}/{}/run5/Dist-C21-GM12878-{}-run5.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r6 = '/scratch/kl76/data/{}/{}/run6/Dist-C21-GM12878-{}-run6.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r7 = '/scratch/kl76/data/{}/{}/run7/Dist-C21-GM12878-{}-run7.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r8 = '/scratch/kl76/data/{}/{}/run8/Dist-C21-GM12878-{}-run8.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r9 = '/scratch/kl76/data/{}/{}/run9/Dist-C21-GM12878-{}-run9.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
r10 = '/scratch/kl76/data/{}/{}/run10/Dist-C21-GM12878-{}-run10.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
G=936
Nreallist= list()
Nreallist.append(r1)
Nreallist.append(r2)
Nreallist.append(r3)
Nreallist.append(r4)
Nreallist.append(r5)
#Nreallist.append(r6)
#Nreallist.append(r7)
#Nreallist.append(r8)
#Nreallist.append(r9)
#Nreallist.append(r10)
ii=0
d = np.zeros(shape=(G-1,G-1))
for yy in Nreallist:
  fin = yy
  #print yy
  #fin='/Diist-C21-GM12878-{}-{}-{}.dat'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_dSR)
  try:
      d+=np.loadtxt(fin, usecols = range(935), max_rows=935)
      ii+=1
      #print ii
  except (IOError): pass
if ii>0:
  print ii
  d=d/ii
  #print d	
  np.savetxt("/scratch/kl76/data/{}/{}/Dist-{}-{}-all.dat".format(arguments.arg_tx,arguments.arg_cx,arguments.arg_tx,arguments.arg_cx),d)
  #fig.savefig("HiC-{}-{}-{}.pdf".format(arguments.arg_tx,arguments.arg_cx,arguments.arg_dSR))
  plt.imshow(d,norm=mpl.colors.LogNorm(vmin=0.0001, vmax=1),cmap="Reds")
  plt.savefig('/scratch/kl76/data/{}/{}/Dist-all-{}-{}.png'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_tx,arguments.arg_cx))
  #plt.matshow(d,norm=mpl.colors.LogNorm(vmin=0.0001, vmax=1),cmap="Reds")
