import math
import numpy as np
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='GAMinG - Genome Architecture MiChroM input files for Gromacs',prog='GAMinG')
parser.add_argument('-tx', action='store', default = 1.0, dest ='arg_tx')
parser.add_argument('-cx', action='store', default=2.0,dest ='arg_cx')
arguments = parser.parse_args()

#averagefile = '/scratch/kl76/data/{}/{}/all-average-{}.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
#sigmafile = '/scratch/kl76/data/{}/{}/all-average-{}.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
#filename1 = '/scratch/kl76/data/{}/{}/run1/all-C21-GM12878-{}-run1.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
#filename2 = '/scratch/kl76/data/{}/{}/run2/all-C21-GM12878-{}-run2.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
#filename3 = '/scratch/kl76/data/{}/{}/run3/all-C21-GM12878-{}-run3.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
#filename4 = '/scratch/kl76/data/{}/{}/run4/all-C21-GM12878-{}-run4.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)
#filename5 = '/scratch/kl76/data/{}/{}/run5/all-C21-GM12878-{}-run5.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx)

distlist = list()
runs=5
cm=[68.62981297118152,68.86099698273586,69.16500000326313] #Center of Mass of system
r= 9.098654279151768 #Radius of system

#Averaging the positions of heterochrmatin beads across all simulation trajectories
averagef=open("/scratch/kl76/data/{}/{}/averagefile{}.txt".format(arguments.arg_tx,arguments.arg_cx,arguments.arg_cx),'w')
ii=0
for ll in range(2,runs+1):
    filename = '/scratch/kl76/data/{}/{}/run{}/all-C21-GM12878-{}-run{}.gro'.format(arguments.arg_tx,arguments.arg_cx,ll,arguments.arg_cx,ll)
    distlist = list()
    with open(filename) as a:
    	snaps=0    
    	for line in a:
            try:
                if "step" in line and len(distlist)>0:
                    distframe = sum(distlist)/len(distlist)
                    averagef.write('{0:6.6f} {1:3.6f} \n'.format(distframe, float(ii)/len(distlist)))
                    print(distframe, float(ii)/len(distlist), max(distlist))
                    distlist = []
                    ii=0
                    snaps+=1
                if "TB" in line: #Keepin
                    row = line.split()
                    posx = float(row[3])
                    posy = float(row[4])
                    posz = float(row[5])
                    dist = float(math.sqrt((posx-cm[0])**2+(posy-cm[1])**2+(posz-cm[2])**2))
                    distlist.append(dist)
                    if dist >= (r-2):
                        ii+=1
                #if snaps>=3: break
            except (ValueError,IndexError,IOError): pass        
averagef.close()
