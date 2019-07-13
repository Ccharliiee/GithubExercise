import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
import queue
import pickle

class Point(object):

    def __init__(self, vertex, dcomp) -> None:
        super().__init__()
        self.vertex = vertex
        self.dcomp = dcomp

    def __str__(self) -> str:
        return str(self.vertex) + ' ' + str(self.dcomp)


def funcC1():
    dim = 2
    k = 2**(dim-1)
    gervec = list(itertools.product(range(2), repeat=dim))
    print('ger: ',gervec)
    pts = []
    ptsob = {}
    for r in range(1, len(gervec)):
        comb = itertools.combinations(gervec, r)
        for lists in comb:
            # print('lists: ', lists)
            pt = np.array(lists).sum(axis=0, dtype=int)
            ptob = Point(pt, lists)
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

def funcDcomp(dim):
    k = 2**(dim-1)
    gervec = list(itertools.product(range(2), repeat=dim))
    # print('ger: ',gervec)
    gervec.remove((0,)*dim)
    print('ger: ', gervec)
    pts = []
    ptsob = {}
    for r in range(1, len(gervec)):
        comb = itertools.combinations(gervec, r)
        for lists in comb:
            # print('lists: ', lists)
            pt = np.array(lists).sum(axis=0, dtype=int)
            if sum(pt) > dim * k / 2:
                continue
            # pt = np.sort(pt)
            ptsstr = ' '.join(np.array2string(pt, separator=','))
            ptob = Point(pt, np.array(lists))
            # print('pt: ', pt)
            if ptsstr in ptsob:
                ptsob[ptsstr] = 2
                continue
            ptsob[ptsstr] = ptob

    # print('pts: ', pts)

    ptsob = {key: val for key, val in ptsob.items() if val != 2}
    print('all vertices', ptsob)
    # np.savetxt("all d" + str(dim) + ".csv", pts[hull.vertices], fmt='%s', delimiter=',', newline='\n')


    perverticesset = set()
    dkverticesq = queue.PriorityQueue()
    pervertices = {}
    for key, val in ptsob.items():
        vertex = val.vertex
        # print('vertex； ', vertex)
        vertex = np.sort(vertex)
        vertexstr = ' '.join(np.array2string(vertex, separator=','))
        if vertexstr in perverticesset:
            continue
        if sum(vertex) == dim*k/2:
            perverticesset.add(vertexstr)
            dkverticesq.put(((vertex > k/2).sum(), key, val))
            continue
        perverticesset.add(vertexstr)
        pervertices[key] = val
        # print('pervertices', pervertices)
    if not dkverticesq.empty():
        dkvertices = dkverticesq.get()[1:]
        print(dkvertices)
        pervertices[dkvertices[0]] = dkvertices[1]
    # pervertices['[ 0 , 0 ]'] = Point(np.zeros(dim, dtype=np.int), ((0,)*dim,))
    pervertices[' '.join(np.array2string(np.zeros(dim, dtype=np.int), separator=','))] = Point(np.zeros(dim, dtype=np.int), np.array(((0,)*dim,)))
    # pervertices = np.array(pervertices)
    # print('pervertice: ', pervertices)
    # arr2save = np.array([[0, 0]], dtype=int)
    arr2save = []
    for key, val in pervertices.items():
        # print('kv: ', key, val)
        arr2save.append(val.vertex)
        arr2save.append(val.dcomp)
        # print('arr2save', arr2save)
    print('arr2save', arr2save)
    # np.savetxt("perv_d_dcomp" + str(dim) + ".csv",  arr2save, fmt='%s', delimiter=',', newline='\n')
    # np.save("perv_d_dcomp" + str(dim) + ".csv",  arr2save)
    return arr2save

def picw(dim, arr2save):
    with open("pickelfile/perv_d_dcomp" + str(dim) + ".pkl", 'wb') as fp:
        pickle.dump(arr2save, fp)

    with open('pickelfile/perv_d_dcomp' + str(dim) + '.pkl', 'rb') as fp:
        itemlist =pickle.load(fp)
    print('itemlist', itemlist)

def picr(dim):
    with open('pickelfile/perv_d_dcomp' + str(dim) + '.pkl', 'rb') as fp:
        itemlist =pickle.load(fp)
    print('gradpro.six003deluxe.picr    itemlist', itemlist)
    return itemlist


# funcDcomp(3)

# funcC1()
