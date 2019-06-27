import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
def func():
    dim = 4
    gervec = list(itertools.product(range(2), repeat=dim))
    pts = []
    for r in range(1, len(gervec)):
        comb = itertools.combinations(gervec, r)
    for lists in comb:
    # print('list: ', lists)
        pt = np.array(lists).sum(axis=0, dtype=int)
    pts.append(list(pt))
    # print(pt)

    pts = np.array(pts)

    hull = ConvexHull(pts)
    # f = open("d" + str(dim) + ".txt", "w")
    # f.write(pts[hull.vertices])
    # f.close()

    # pts[hull.vertices].tofile("d" + str(dim) + ".txt", sep=",", format="%s")
    np.savetxt("d" + str(dim) + ".csv", pts[hull.vertices], fmt='%s', delimiter=',', newline='\n')

    print(pts[hull.vertices])


