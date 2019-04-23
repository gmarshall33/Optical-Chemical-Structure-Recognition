# This is where bonds between atoms will be recognized using simple hough type functions

import numpy as np


def detect_lines(img, center, threshold):
    # given a 1) inverse binary image, where the lines of interest are white and background is black
    # 2) an index pair corresponding to the center of an interest region on the image,
    # and 3) the max length of the line you want to detect
    # >> find possible lines originating from that center
    y, x = center[0], center[1]
    theta = np.linspace(0, 2*np.pi, num=360)  # consider polar  coordinates x = r*cos(theta) y = r*sin(theta)
    theta = theta.tolist()
    out = []  # list of the number of votes each angle got
    points = []  # points corresponding to votes for each angle (mostly for visualization purposes)
    for o in theta:
        r = 1  # radius, initially one for every angle
        votes = 0
        line_pts = []  # points for the current line
        while r <= threshold:  # r will increase every iteration until it reaches the max length which is threshold
            m = int(round(r*np.sin(o)))
            n = int(round(r*np.cos(o)))  # have to add n,m to x,y to adjust for location of center
            try:
                if img[m+y, n+x] > 0:  # if the current point on the image is not black...
                    votes += 1
                    line_pts.append([m+y, n+x])
            except IndexError:
                pass
            r += 1
        points.append(line_pts)  # add current line points to the master list of points
        out.append((votes, o))
        # out is a list of tuples containing (votes, corresponding angle)
    return out, points
    # points are returned mostly for plotting purposes


def check_direction(center_cluster, theta, other_cluster, max_percent_error=1):
    # Given a center node, strong direction angle, and another node for comparison...
    # >>> determine if the center is in the given direction from the node (returns boolean)
    cent = center_cluster.center
    center = other_cluster.center
    m, n = cent[0], cent[1]
    d = (((m-center[0])**2) + ((n - center[1])**2))**0.5  # distance formula
    if d == 0:
        return None
        # if we are checking a center with itself return none
    # thus begins the trigonometry and unit circle stuff:::
    psi = np.arcsin((center[0]-m) / d)
    if (theta >= 0) and (theta <= np.pi/2):
        # in quadrant 1 :  psi = theta
        if percent_error(psi, theta) < max_percent_error:
            return True
    elif theta >= (np.pi/2) and (theta <= 1.5 * np.pi):
        # in quadrant 2 and 3 :  psi = (pi)-theta
        if percent_error(psi, (np.pi - theta)) < max_percent_error:
            return True
    elif (theta <= 1.5 * np.pi) and (theta <= 2*np.pi):
        # in quadrant 4 :  pis = theta - 2(pi)
        if percent_error(psi, (theta - (2*np.pi))) < max_percent_error:
            return True
    else:
        return False
# TODO there are bugs in this function that mess up the angles, also this isn't sufficient criteria to connect nodes

def percent_error(x, y):  # helper function
    if y < .1:
        x += np.pi*2
        y += np.pi*2
    return (abs(x-y)/y)*100


def calc_dist(ind):
    # input a list of centers, will generate a distance matrix for reference when 'sorting'
    (m, n) = np.shape(ind)
    distance_matrix = np.zeros((m, m))
    for c in range(len(ind)):
        for p in range(len(ind)):
            distance_matrix[c, p] = (((ind[c][1] - ind[p][1]) ** 2) + ((ind[c][0] - ind[p][0]) ** 2)) ** .5
    return distance_matrix
    # TODO optimize... upper and lower triangulars are mirrored, diagonal is zeros


def strong_directions(vote_angle, thresh=.65):
    # given list of tuples (votes, angles) >>> return list of angles with many votes
    # SORT ANGLES BY MOST VOTES
    vote_angle.sort(reverse=True)  # list of tuples (votes, angle) from greatest to smallest votes
    allVotes = [v[0] for v in vote_angle]
    maxVote = max(allVotes)
    allAng = [d[1] for d in vote_angle]
    strongAng = [allAng[i] for i in range(len(allVotes)) if allVotes[i] >= (maxVote*thresh)]  # list comprehension flex
    return strongAng  # a list of the strongest angles ( <=(thresh)% of the  maximum votes) default 65%


def nodes_by_dist(distance_matrix, center_index):
    # given a square distance matrix and index for the center node
    # >>> return indices of nodes sorted by distance to the center node
    d = np.argsort(distance_matrix[center_index, :])
    d = d.tolist()
    d = map(int, d)
    return d  # list of indices corresponding to molecule[index] , sorted by distance closest to farthest


def bond_clusters(molecule, ind1, ind2):
    molecule[ind1].connections.add(ind2)
    molecule[ind2].connections.add(ind1)
    # not worried about duplicated because connections is a set. [unordered unique entries, iterable]





