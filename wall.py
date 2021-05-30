import math
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser(description='wall builder',prog='wall')
#parser.add_argument('-s', action='store', default=1.0, dest='arg_s', help='Sigma value {float} (default: %(default)s)') 
parser.add_argument('-dens', action='store', nargs=1, dest='arg_dens',required=False, default=1.0,  help='Density of Wall Beads: {int}/(unit area of wall)')

try:
    arguments = parser.parse_args()
    print('Density:', arguments.arg_dens, '/unit area of wall')
except IOError:
    msg = sys.msg_info()[1]
    parser.error(str(msg))                    

filename1 = 'C21-GM12878-init-snap.gro'
file_seq = 'seqwall.txt'
seqfile = 'seq_C21.txt'
xlist = list()
ylist = list()
zlist = list()
plist = list()
dlist = list()
with open(filename1) as f:
    f.readline()
    Nchr = int(f.readline())
    for line in f:
        try:
            row = line.strip(' ').strip('\n').split()
            #print(row)
            x = float(row[3])
            #print(x)
            xlist.append(float(x))
            y = float(row[4])
            ylist.append(float(y))
            z = float(row[5])
            zlist.append(float(z))
            plist.append([x, y, z])
        except (ValueError, IndexError):
            print('pass')
#print(plist)
xcm = np.mean(xlist)
ycm = np.mean(ylist)
zcm = np.mean(zlist)
cm = (xcm, ycm, zcm)
#print('center at ',xcm, ycm, zcm)
for i in plist:
    dlist.append(math.sqrt((i[0]-xcm)**2 + (i[1]-ycm)**2 + (i[2]-zcm)**2))
r = (max(dlist))
print(r)
beadlist =list()
# Wall in Y-Z plane
blc = (cm[0]+r,cm[1]-r,cm[2]-r)
brc = (cm[0]+r,cm[1]+r,cm[2]-r)
tlc = (cm[0]+r,cm[1]-r,cm[2]+r)
trc = (cm[0]+r,cm[1]+r,cm[2]+r)
nwallx =10
nwally=10
"""
for i in range(nwallx):
    for j in range(nwally):
        #beadlist.append[cm[0]+r,cm[1]-r+i,cm[2]-r+j]
        beadlist.append([blc[0], blc[1]+i, blc[2]+j])
"""
#print(beadlist)
sigma=1.0
a=np.pi*sigma**2/4
N=4*np.pi*r**2/a
d=np.sqrt(a)
M_theta=np.int(np.around(r*np.pi/d))
d_theta=r*np.pi/M_theta
d_phi=a/d_theta
Nw=0
print(M_theta, d_theta,d_phi, a)
for m in range(M_theta):
    theta=np.pi*(m+0.5)/M_theta
    M_phi=np.int(np.around(2*np.pi*r*np.sin(theta)/d_phi))
    print(m, M_phi)
    for n in range(M_phi):
        phi=2*np.pi*n/M_phi
        beadlist.append([cm[0]+r*np.sin(theta)*np.cos(phi),
                        cm[1]+r*np.sin(theta)*np.sin(phi),
                        cm[2]+r*np.cos(theta)])
        Nw+=1

print(N, Nw)
#i = range(100)
with open('wall-init-snap.gro', 'w') as G:
    G.write("Chromatin\n{:6d}\n".format(Nchr+Nw))
    for line in open(filename1):
        if len(line.split())>3:
            G.write(line)
    for ii,beadpos in enumerate(beadlist):
        jj = ii+Nchr+1
        out="{0:5d}{1:5s}{2:5s}{3:5d}{4:8.3f}{5:8.3f}{6:8.3f}{7:8.3f}{8:8.3f}{9:8.3f}\n".format(jj,'ChrZ', '   ZZ', jj, beadpos[0],beadpos[1],beadpos[2], 0, 0, 0)
        G.write(out)
    with open(filename1) as f:
        G.write(list(f)[-1])

with open('walls-restraint.gro', 'w') as F:
    F.write('Chromatin\n{:6d}\n'.format(Nchr+Nw))
    with open('C21-GM12878-restraint.gro','r') as res:
        res.readline()
        res.readline()
        for ii,line in enumerate(res):
            if ii<Nchr: 
                F.write(line)
                val=float(line.split()[-1])
        for nn in range(Nw):
            jj=nn+Nchr+1
            F.write("{0:5d}{1:5s}{2:5s}{3:5d}{4:8.3f}{5:8.3f}{6:8.3f}\n".format(jj,'ChrZ', 'ZZ', jj, val,val,val))
    with open('C21-GM12878-restraint.gro') as f:
        F.write(list(f)[-1])

def createList(r1,r2):
    return [item for item in range(r1,r2+1)]
chromatinlist = list()
r1, r2 = 1, Nchr
r3, r4 = Nchr+1, Nw+Nchr
column1 = (createList(r1,r2))
column2 = (createList(r3,r4))
with open(seqfile) as Q:
        #Q.readline()
        for line in Q:
                    row = line.strip(' ').strip('\n').split()
                    #print(row[1])
                    chromatin = str(row[1])
                    #print(chromatin)
                    chromatinlist.append(str(chromatin))
#print(chromatinlist)
with open('seqwall.txt', 'w') as H:
    for index in range(len(column1)):
        #print(int(index))
        #print(chromatinlist[int(index)])
        #print(range(len(column1)))
        H.write((str(column1[index])) + " " + chromatinlist[int(index)] + "\n")
    for index in range(len(column2)):
        H.write((str(column2[index])) + " " + "Z1" "\n")
