# Lamina-Chromatin-Model
This repository contains all of the files associated with the Lamina-Chromatin Model I developed with Dr. Sumitabha Brahmachari at Rice University.

In order to run this model you will need a copy of Gaming.py which can be obtained from https://ndb.rice.edu/ and in addition to that you will also need GROMACS to run the simulations on your computer.

wall.py is the script that creates the simulated nuclear lamina to surround a chromosome. It requires a sequence input file, and two simulation files (the snapshot and the restraint file mentioned in wall.py) which are obtained from performing an initial collapse of the chromosme using the Minimal Chromatin Model in GROMACS.

seq_C21.txt is a text file containing all of the chromatin subtypes making up chromosome 21 of human GM12878 lymphoblastoid cells and is a required input of wall.py so that the new monomers making up the nuclear lamina can be added to it in order for GROMACS to function properly during simulations. Sequence files for chromosome 21 and other chromosome can be found using the Nucleome Data Bank found at (https://ndb.rice.edu/)

If you want to create your own randomized sequence file instead of getting one from the Nucleome Data Bank, you can do that using the seqgen.py script.

dirmakr.sh will create an organized directory system and run simulations in them. $cx is the parameter for the the heterochromatin-lamina interaction strength (0.0 = no interaction, 0.2 = average interaction, 0.4 = strong interaction). The #SBATCH lines can be removed or filled out depending on if you choose to run your simulations using slurm or not.

groaverage.py will average the positions of heterochromatin across each simulation trajectory and histogramplot.py will plot the fraction of heterochromatin interaction with the wall and the movement of heterochromatin towards the wall for each interaction strength

averagehic.py will average hi-c matrices and create a new hi-c map png file showing the averaged hi-x matrix.

I am still cleaning up and assembling all of the files that will be uploaded here so this repository is currently a work in progress.
