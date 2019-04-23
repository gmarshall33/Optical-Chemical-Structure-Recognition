# This module will contain the algorithm to convert the completed molecular data structure to SMILES string or anther
# standardized format.

# also include some visualization functions since haven't programed SMILES interpreter yet

import cv2
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import random
import numpy as np


def vis_clusters(img, dst, clusters):
    # VISUALIZATION INFO for corner detection and clustering results
    cv2.imshow('orginal', img)

    simg = img
    simg[dst > 0.001 * dst.max()] = [0, 0, 255]
    cv2.imshow('corners detected', simg)

    clustimg = img
    for i in range(len(clusters)):
        yeet = round(random.uniform(0, 1) * 255)
        for w in clusters[i]:
            clustimg[w[0], w[1], :] = [255 / (i + 1) * 2, 255 - yeet, yeet]
            cv2.imshow('w', clustimg)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    return clustimg


def vclust(img, dst, clusters):
    # copy of vis_clusters but without the imshow() windows for use in vis_molecule
    simg = img
    simg[dst > 0.001 * dst.max()] = [0, 0, 255]
    clustimg = img
    for i in range(len(clusters)):
        yeet = round(random.uniform(0, 1) * 255)
        for w in clusters[i]:
            clustimg[w[0], w[1], :] = [255 / (i + 1) * 2, 255 - yeet, yeet]
    return clustimg


def vis_centers(img, centers):
    zimg = img
    for cent in centers:
        zimg[cent[0]-3:cent[0]+3, cent[1]-3:cent[1]+3, :] = [0, 255, 0]
    cv2.imshow('centers', zimg)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    # colors the centers green on an img
    return zimg


def draw_lines(img, point1, angle):
    fig, ax = plt.subplots()
    ax.imshow(img)  # extent = [0, n, 0, m])
    endm = point1[0] + (100 * np.sin(angle))
    endn = point1[1] + (100 * np.cos(angle))

    # collection = mc.LineCollection(segments)
    # ax3.add_collection(collection)
    ax.plot([point1[1], endn], [point1[0], endm])
    plt.show()


def vis_molecule(molecule, img_data, save_fig=False, filename='untitled.png'):
    # PRODUCES PLOT WITH ORIGINAL IMAGE, CLUSTERS, AND CONNECTION GRAPH
    # molecule list of cluster class, img_data dictionary, optional params for if you want to save the figure
    segments = []
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
    fig.suptitle('Atoms and Bonds', fontsize=18)
    ax1.imshow(img_data['original'])  # image
    ax1.set_title('Original Image')
    ax1.axis('off')

    ax2.imshow(vclust(img_data['original'], img_data['dst'], [x.points for x in molecule]))  # clusters from vclust()
    ax2.set_title('Clusters from Corner Detection')
    ax2.axis('off')

    for node in range(len(molecule)):  # circles for nodes
        cent1 = molecule[node].center
        c1 = (cent1[1], -1*cent1[0])
        circle1 = plt.Circle((molecule[node].center[1], (molecule[node].center[0])*-1), 5, color='y')
        plt.annotate(node, c1)  # add number labels
        ax3.add_artist(circle1)

        for ind in molecule[node].connections:  # line segments between nodes
            cent2 = molecule[ind].center
            c2 = (cent2[1], -1*cent2[0])
            line = [c1, c2]
            segments.append(line)

    collection = mc.LineCollection(segments)
    ax3.add_collection(collection)
    ax3.set_title('Nodes and Connections')
    ax3.autoscale()
    ax3.margins(.5)
    ax3.axis('off')
    if save_fig:
        plt.savefig(filename)
    plt.show()


def vis_vote_angle(vote_angle):
    vote_angle.sort(reverse=True)  # list of tuples (votes, angle) from greatest to smallest votes
    allVotes = [v[0] for v in vote_angle]
    allAng = [d[1] for d in vote_angle]
    plt.plot(allAng, allVotes, 'o')
    plt.show()
