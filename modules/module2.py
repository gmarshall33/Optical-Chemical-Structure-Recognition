# This module is where the node classification will take place. Use image data about the interest regions as input to
# neural network for handwritten character recognition with added intersection data.
import cv2


def snip(img, clusters):
    snippet = []
    for clust in clusters:
        clust_x = [r[0] for r in clust]
        clust_y = [r[1] for r in clust]
        a = min(clust_x)
        b = max(clust_x)
        c = min(clust_y)
        d = max(clust_y)
        snippet.append(img[a:b+1, c:d+1])

    # Takes the region of the image containing the cluster
    # size of image snippet is the smallest rectangle inscribing the cluster
    return snippet

# TODO Normalize Snippet, train recognition network
