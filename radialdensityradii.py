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

filename1 ='/scratch/kl76/data/FISchr21/{}/{}/{}/all-C21-GM12878-{}-{}.gro'.format(arguments.arg_tx,arguments.arg_cx,arguments.arg_dSR,arguments.arg_cx,arguments.arg_dSR)

#GOAL IS TO CALC AND STORE RAD DENSITY AND TOTAL NUMBERS OF BEADS FOR EACH REGION FOR EACH FRAME
xcm = 196.4
ycm = 195.7
zcm = 195.9
cm = (xcm, ycm, zcm)

ii=0
plist = list()
a1rad = list()
a2rad = list()
b1rad = list()
b2rad = list()
b3rad = list()
a1 = open('a1-{}.txt'.format(arguments.arg_cx), 'w')
a2 = open('a2-{}.txt'.format(arguments.arg_cx), 'w')
b1 = open('b1-{}.txt'.format(arguments.arg_cx), 'w')
b2 = open('b2-{}.txt'.format(arguments.arg_cx), 'w')
b3 = open('b3-{}.txt'.format(arguments.arg_cx), 'w')
na = open('na-{}.txt'.format(arguments.arg_cx), 'w')
counters = open('counters-{}.txt'.format(arguments.arg_cx), 'w')
aa = 0
bb = 0
cc = 0
dd = 0
ee = 0
ff = 0
for i in range(1,17):
	with open('/scratch/kl76/data/FISchr21/{}/{}/{}/all-C21-GM12878-{}-{}.gro'.format(arguments.arg_tx,arguments.arg_cx,'r'+str(i),arguments.arg_cx,'r'+str(i))) as f:
		#print(f)
		for line in f:
			try: 	
				if 'step' in line:
					ii+=1
					#print(ii)
				row = line.strip(' ').strip('\n').split()
				x = float(row[3])
                		y = float(row[4])
                		z = float(row[5])
				#xlist.append(float(x))
				#ylist.append(float(y))
				#zlist.append(float(z))
				#print(lin)
				value = math.sqrt((x-xcm)**2 + (y-ycm)**2 + (z-zcm)**2)
                                if "ZA" in line:
					a1.write(str(value) + '\n')
					aa+=1
                                if "OA" in line:
                                        a2.write(str(value) + '\n')
					bb+=1
				if "FB" in line:
                                        b1.write(str(value) + '\n')
					cc+=1
                                if "SB" in line:
                                        b2.write(str(value) + '\n') 
					dd+=1                                       
                                if "TB" in line:
                                        b3.write(str(value) + '\n')
					ee+=1                                        
                                if "UN" in line:
                                        na.write(str(value) + '\n')
					ff+=1
			except:
    				pass
a1.close()
a2.close()
b1.close()
b2.close()
b3.close()
na.close()
print(ii)
counters.write('a1 = ' + str(aa) + '\n')
counters.write('a2 = ' + str(bb) + '\n')
counters.write('b1 = ' + str(cc) + '\n')
counters.write('b2 = ' + str(dd) + '\n')
counters.write('b3 = ' + str(ee) + '\n')
counters.write('na = ' + str(ff) + '\n')
counters.write('ii = ' + str(ii) + '\n')
counters.close()