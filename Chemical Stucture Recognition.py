# This is the master script that uses modules 0-5 to convert an image of a molecule to SMILES string.
# >>> prompt for file
# >>> [output]

import modules.module0 as m0
import modules.module1 as m1
import modules.module2 as m2
import modules.module3 as m3
import modules.module4 as m4
import modules.module5 as m5


class Cluster:
    # Here we will create a class for clusters. I will be experimenting with storing the data in this format
    # The molecule will be represented by a list of these clusters
    def __init__(self, points, center, snippet):
        self.points = points
        self.center = center
        self.snippet = snippet
        self.connections = set()  # the other clusters that this one is connected to.
        # want to store the directions and probably length of lines originating from the center
    # other class methods?


# PRE-PROCESS

# NODE FINDER

# ORGANIZE
molecule = []  # a given molecule is represented by a list of cluster objects
for i in range(len(clusters)):
    p = clusters[i][:]
    c = centers[i][:]
    s = snippets[i]
    molecule.append(Cluster(p, c, s))
    # Creates new cluster with points, center, and snippet data.. appends to molecule list

# NODE CLASSIFIER

# BOND FINDER

# BOND CLASSIFIER

# OUTPUT FORMATTING
