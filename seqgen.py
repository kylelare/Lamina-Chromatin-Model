import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.collections as collections

# Create a chromosome sequence of random monomers
G = 2000 #sequence length
random.seed(90)
ii = 0
jj = 0
fig, ax = plt.subplots(1, 1, figsize=(7, 5))
with open('seq.txt', 'w') as fout:
    while ii < G:
        ty = random.choice(['A1', 'B3'])
        num = np.int(random.gauss(5, 4))
        for ll in range(num):
            ii += 1
            p = '{} {}\n'.format(ii, ty)
            # print(p)
            fout.write(p)

            if ty is 'A1':
                jj += 1
                ax.axvline(x=ii, c='b')
            else:
                ax.axvline(x=ii, c='r')

print(jj / ii)

#Find the percentages of each chromatin subtype making up the new chromosome
A1list = list()
A2list = list()
B1list = list()
B2list = list()
B3list = list()
NAlist = list()

filename1 = 'C:\\Users\\thesg\\seq.txt'
with open(filename1) as f:
    for line in f:
        #print(line)
        if 'A1' in line:
            A1list.append('A1')
        if 'A2' in line:
            A2list.append('A2')
        if 'B1' in line:
            B1list.append('B1')
        if 'B2' in line:
            B2list.append('B2')
        if 'B3' in line:
            B3list.append('B3')
        if 'NA' in line:
            NAlist.append('NA')
print('A1:', len(A1list), (','), (len(A1list)/G)*100, '%')
print('A2:', len(A2list), (','), (len(A2list)/G)*100, '%')
print('B1:', len(B1list), (','), (len(B1list)/G)*100, '%')
print('B2:', len(B2list), (','), (len(B2list)/G)*100, '%')
print('B3:', len(B3list), (','), (len(B3list)/G)*100, '%')
print('NA:', len(NAlist), (','), (len(NAlist)/G)*100, '%')

#Create a color bar to accompany Hi-C maps and identify which regions make up heterochromatin
filename1 = 'C:\\Users\\thesg\\seq.txt'
seqlist = list()
with open(filename1) as f:
    for line in f:
        if 'A' in line:
            seqlist.append('A')
        if 'B1' in line:
            seqlist.append('B')
        if 'B2' in line:
            seqlist.append('B')
        if 'B3' in line:
            seqlist.append('B3')
fig, ax = plt.subplots()
for i in [i for i,x in enumerate(seqlist) if x == "A"]:
    ax.axvline(.01*i, ymin = 0, ymax =0.5, linewidth=.5, color='m')
for i in [i for i,x in enumerate(seqlist) if x == "B"]:
    ax.axvline(.01*i, ymin = 0, ymax =0.5, linewidth=.5, color='y')
for i in [i for i,x in enumerate(seqlist) if x == "B3"]:
    ax.axvline(.01*i, ymin = 0, ymax =0.5, linewidth=.5, color='g')
for i in [i for i,x in enumerate(seqlist) if x == "A"]:
    ax.axvline(.01*i, ymin = 0.5, ymax =1.0, linewidth=.5, color='w')
for i in [i for i,x in enumerate(seqlist) if x == "B"]:
    ax.axvline(.01*i, ymin = 0.5, ymax =1.0, linewidth=.5, color='w')
for i in [i for i,x in enumerate(seqlist) if x == "B3"]:
    ax.axvline(.01*i, ymin = 0.5, ymax =1.0, linewidth=.5, color='g') #Identifying regions containing heterochromatin
plt.show()
