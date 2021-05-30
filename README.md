# Lamina-Chromatin-Model
This repository contains all of the files associated with the Lamina-Chromatin Model I developed with Dr. Sumitabha Brahmachari at Rice University.

Wall.py is the script that creates the simulated nuclear lamina to surround the chromosome. It requires a sequence input file, and two simulation files (the snapshot and the restraint file mentioned in wall.py) which are obtained from performing an initial collapse of the chromosme using the Minimal Chromatin Model in GROMACS.

Seq_C21.txt is a text file containing all of the chromatin subtypes making up chromosome 21 of human GM12878 lymphoblastoid cells and is a required input of wall.py so that the new monomers making up the nuclear lamina can be added to it in order for GROMACS to function properly during simulations. Sequence files for chromosome 21 and other chromosome can be found using the Nucleome Data Bank found at (https://ndb.rice.edu/)

I am still cleaning up and assembling all of the files that will be uploaded here so this repository is currently a work in progress.
