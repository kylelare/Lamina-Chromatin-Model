 import numpy as np
import matplotlib.pyplot as plt
average0 ='C:\\Users\\thesg\\averagefile0.0.txt'
average1 ='C:\\Users\\thesg\\averagefile0.1.txt'
average2 ='C:\\Users\\thesg\\averagefile0.2.txt'
average3 ='C:\\Users\\thesg\\averagefile0.3.txt'
average4 ='C:\\Users\\thesg\\averagefile0.4.txt'

averages0 = list()
averages1 = list()
averages2 = list()
averages3 = list()
averages4 = list()
fracs0 = list()
fracs1 = list()
fracs2 = list()
fracs3 = list()
fracs4 = list()

walldist = 13.5 #Wall Radius
with open(average0) as average0:
    for line in average0:
        row = line.split()
        averages0.append(walldist - float(row[0]))
        fracs0.append(float(row[1]))
with open(average1) as average1:
    for line in average1:
        row = line.split()
        averages1.append(walldist - float(row[0]))
        fracs1.append(float(row[1]))
        #print(fracs1)
with open(average2) as average2:
    for line in average2:
        row = line.split()
        #print(float(row[0]))
        averages2.append(walldist - float(row[0]))
        fracs2.append(float(row[1]))
        #print(fracs2)
with open(average3) as average3:
    for line in average3:
        row = line.split()
        averages3.append(walldist - float(row[0]))
        fracs3.append(float(row[1]))
        #print(fracs4)
with open(average4) as average4:
    for line in average4:
        row = line.split()
        averages4.append(walldist - float(row[0]))
        #print(averages4)
        fracs4.append(float(row[1]))
#print(averages2)
#print(averages4)

#Histogram showing average distance of heterochromatin from the wall for each interaction strength
plt.figure(figsize=[10,8])
plt.hist(averages0,bins= np.arange(1,10,0.1),label='$\epsilon$ = 0.0',density=True,alpha=.5)
plt.hist(averages1,bins= np.arange(1,6,0.1),label='$\epsilon$ = -0.1',density=True,alpha=.5)
plt.hist(averages2,bins= np.arange(1,10,0.1),label='$\epsilon$ = -0.2',density=True,alpha=.5)
plt.hist(averages3,bins= np.arange(1,6,0.1),label='$\epsilon$ = -0.3',density=True,alpha=.5)
plt.hist(averages4,bins= np.arange(1,10,0.1),label='$\epsilon$ = -0.4',density=True,alpha=.5)
plt.legend(loc='upper center',prop={'size': 25})
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Average Distance of HC from the wall ($\sigma$)',fontsize=25)
plt.xticks(fontsize=20)
plt.xlim(1,8)
plt.yticks(fontsize=20)
y = plt.ylabel('Frequency',fontsize=25)
plt.title('Average Distance of Heterochromatin Beads \n from the Wall',fontsize=25)
plt.grid(False)
plt.show()

#Histogram showing the average fraction of heterochromatin interacting with the wall for each interaction strength
plt.figure(figsize=[10,8])
plt.hist(fracs0,bins= np.arange(0,1,0.02), label='$\epsilon$ = 0.0',density=True,alpha=.5)
plt.hist(fracs1,bins= np.arange(0,1,0.02), label='$\epsilon$ = -0.1',density=True,alpha=.5)
plt.hist(fracs2,bins= np.arange(0,1,0.02), label='$\epsilon$ = -0.2',density=True,alpha=.5)
plt.hist(fracs3,bins= np.arange(0,1,0.02), label='$\epsilon$ = -0.3',density=True,alpha=.5)
plt.hist(fracs4,bins= np.arange(0,1,0.02), label='$\epsilon$ = -0.4',density=True,alpha=.5)
plt.legend(loc='upper center',prop={'size': 25})
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Fraction of HC beads near the wall',fontsize=25)
plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],fontsize=20)
plt.xlim(0, 1)
plt.yticks(fontsize=20)
plt.ylabel('Frequency',fontsize=25)
plt.title('Fraction of Heterochromatin Beads \n Near the Wall',fontsize=25)
plt.grid(False)
plt.show()
