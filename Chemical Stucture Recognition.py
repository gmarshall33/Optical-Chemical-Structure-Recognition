# This is the master script that uses modules 0-5 to convert an image of a molecule to SMILES string.

import modules.module0 as m0  # pre-processing
import modules.module1 as m1  # Node recognition
import modules.module2 as m2  # Node classification
import modules.module3 as m3  # Bond Detection
import modules.module4 as m4  # Bond Classifcation
import modules.module5 as m5  # Output formatting


class Cluster:
    # Here we will create a class for clusters. I will be experimenting with storing the data in this format
    # The molecule will be represented by a list of these clusters. Order matters
    def __init__(self, points, center):
        self.points = points
        self.center = center
        self.connections = set()  # the other clusters that this one is connected to.
    # other class methods?


# PRE-PROCESS
filepath = raw_input("File path to image: ")
std_img = m0.preproc_naive(filepath)

# CLUSTER FINDER
node_points, img_data = m1.corner_detect(std_img)
clusters, centers = m1.clust_centers(node_points, 25)

# FORMAT MOLECULE (list of Clusters)
molecule = []  # a given molecule is represented by a list of cluster objects
for i in range(len(clusters)):
    p = clusters[i][:]
    c = centers[i][:]
    molecule.append(Cluster(p, c))
    # Creates new cluster with points, center, and snippet data.. appends to molecule list

# CLUSTER CLASSIFIER
snippets = m2.snip(std_img, clusters)

# BOND FINDER
m3.connection_algo(molecule, img_data)

# BOND CLASSIFIER

# OUTPUT FORMATTING
m5.vis_molecule(molecule, img_data, save_fig=False, filename='untitled.png')
