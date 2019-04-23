# This is the master script that uses modules 0-5 to convert an image of a molecule to SMILES string.
# >>> prompt for file
# >>> [output]
import modules.module0 as m0

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
