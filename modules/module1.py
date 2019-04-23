# This module takes the standardized image from module 0 and uses corner detection and clustering to create the molecule
# class. this takes care of the node recognition phase and organizes the moelecular stucture as a list of node classes
import numpy as np
import cv2


def corner_detect(img):
    # image processing function intended for the first pass on a given molecule
    # includes scaling, gray-scale, gaussian blur, harris corner detection, dilation, normalization
    # returns the list of indices on the scaled img that pass the harris corner detection threshold

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # gray-scale
    gray = np.float32(gray)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)  # blur image to reduce noise
    dst = cv2.cornerHarris(blur, 10, 3, 0.06)  # corner detection
    dst = cv2.dilate(dst, None, None, None, 3)  # NOT NECESSARY JUST ENFORCING POINTS
    norm = dst / np.linalg.norm(dst)  # normalize output
    binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    # anywhere that is .1% as strong as the strongest corner is a corner point
    node_points = np.argwhere(norm > 0.001 * norm.max())

    img_data = {'original': img, 'gray': gray, 'blur': blur, 'norm': norm, 'dst': dst, 'binary': binary}

    return node_points, img_data


def clust_centers(indices, thresh):
    q = indices  # working queue
    first, q = q[0], q[1:]  # first center
    clusters = [[first]]  # list of list of clusters
    centers = [first]

    while len(q) > 0:
        added = False
        for i in range(len(clusters)):
            if (((centers[i][0]-q[0][0])**2) + ((centers[i][1]-q[0][1])**2)) ** 0.5 < thresh:
                clusters[i].append(q[0])
                q = q[1:]

                centers[i] = calc_center(clusters[i])
                added = True
                break
        if not added:
            clusters.append([q[0]])
            centers.append(q[0])
            q = q[1:]

    return clusters, centers


def calc_center(ind):
    xsum = 0
    ysum = 0
    for i in ind:
        xsum += i[0]
        ysum += i[1]
    xsum, ysum = xsum/len(ind), ysum/len(ind)  # average of all the points in a cluster
    return (xsum, ysum)  # tuple

# TODO devise more complete clustering algorithm.
