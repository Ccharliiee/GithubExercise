import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
import queue

def funcC():
    dim = 2
    k = 2**(dim-1)
    gervec = list(itertools.product(range(2), repeat=dim))
    print('ger: ',gervec)
    pts = []
    for r in range(1, len(gervec)):
        comb = itertools.combinations(gervec, r)
        for lists in comb:
            # print('lists: ', lists)
            pt = np.array(lists).sum(axis=0, dtype=int)
            # print('pt: ', pt)
            pts.append(list(pt))
    # print('pts: ', pts)

    pts = np.array(pts)

    hull = ConvexHull(pts)
    # f = open("d" + str(dim) + ".txt", "w")
    # f.write(pts[hull.vertices])
    # f.close()

    # pts[hull.vertices].tofile("d" + str(dim) + ".txt", sep=",", format="%s")
    # np.savetxt("all d" + str(dim) + ".csv", pts[hull.vertices], fmt='%s', delimiter=',', newline='\n')
    print('all vertices',pts[hull.vertices])


    perverticesset = set()
    dkverticesq = queue.PriorityQueue()
    pervertices = []
    for vertex in pts[hull.vertices]:
        print('vertex； ', vertex)
        vertex = np.sort(vertex)
        if sum(vertex) > dim*k/2:
            continue
        vertexstr = ' '.join(np.array2string(vertex, separator=','))
        if vertexstr in perverticesset:
            continue
        if sum(vertex) == dim*k/2:
            perverticesset.add(vertexstr)
            dkverticesq.put(((vertex > k/2).sum(), vertex))
            continue
        perverticesset.add(vertexstr)
        pervertices.append(vertex)
        print('pervertices', pervertices)
    if not dkverticesq.empty():
        dkvertices = dkverticesq.get()[1]
        pervertices.append(dkvertices)
    # pervertices = np.array(pervertices)
    np.savetxt("perv d" + str(dim) + ".csv",  pervertices, fmt='%s', delimiter=',', newline='\n')
    print('pervertice: ', pervertices)

funcC()
