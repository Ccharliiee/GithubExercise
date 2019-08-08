import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
import queue
import pickle
import time

class Point(object):

    def __init__(self, vertex, dcomp, pre='from last or manual') -> None:
        super().__init__()
        self.vertex = vertex
        self.dcomp = dcomp
        self.pre = pre

    def __str__(self) -> str:
        return str(self.vertex) + ', ' + str(self.dcomp) + ' pre:' + str(self.pre)

    def __repr__(self) -> str:
        return str(self.vertex) + ', ' + str(self.dcomp) + ' pre:' + str(self.pre)

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
    # np.savetxt("perv d" + str(dim) + ".csv",  pervertices, fmt='%s', delimiter=',', newline='\n')
    print('pervertice: ', pervertices)

def funcDcomp(dim):
    k = 2**(dim-1)
    gervec = list(itertools.product(range(2), repeat=dim))
    # print('ger: ',gervec)
    gervec.remove((0,)*dim)
    print('ger: ', gervec)
    ptsobnct = {}
    ptsob = {}
    for r in range(1, len(gervec)+1):
        print('rth:', r)
        comb = itertools.combinations(gervec, r)
        for lists in comb:
            # print('lists: ', lists)
            pt = np.array(lists).sum(axis=0, dtype=int)
            ptsstr = ''.join(np.array2string(pt, separator=','))

#######################only keep vertex up to central symmetery
            if sum(pt) > dim * k / 2:
                # print('pt: ', pt)
                if ptsstr in ptsobnct:
                    ptsobnct[ptsstr] = 2
                else:
                    ptob = Point(pt, np.array(lists))
                    ptsobnct[ptsstr] = ptob

#######################only keep vertex up to central symmetery
            else:
            # pt = np.sort(pt)
            # print('pt: ', pt)
                if ptsstr in ptsob:
                    ptsob[ptsstr] = 2
                    ptsobnct[ptsstr] = 2
                else:
                    ptob = Point(pt, np.array(lists))
                    ptsob[ptsstr] = ptob
                    ptsobnct[ptsstr] = ptob

    # print('pts: ', pts)

    ptsob = {key: val for key, val in ptsob.items() if val != 2}
    ptsobnct = {key: val for key, val in ptsobnct.items() if val != 2}
    # print('all vertices', ptsob)

    # np.savetxt("all d" + str(dim) + ".csv", pts[hull.vertices], fmt='%s', delimiter=',', newline='\n')

    def reduceruptoperm(ptsob, uptocentral=True):
    #################reduce up to permutation
        perverticesset = set()
        dkverticesq = queue.PriorityQueue()
        pervertices = {}
        for key, val in ptsob.items():
            vertex = val.vertex
            # print('vertex； ', vertex)
            vertex = np.sort(vertex)
            vertexstr = ''.join(np.array2string(vertex, separator=','))
            if vertexstr in perverticesset: ########because the smallest permutation is visited first
                continue

    ################# sum x_i = dk/2 minimize the number of coordinates larger than k/2
            if sum(vertex) == dim*k/2 and uptocentral:
                perverticesset.add(vertexstr)
                dkverticesq.put(((vertex > k/2).sum(), key, val))
                continue
    ################ sum x_i = dk/2 minimize the number of coordinates larger than k/2

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
        return pervertices

    pervertices = reduceruptoperm(ptsob)
    # arr2save = np.array([[0, 0]], dtype=int)
    arr2save = []
    for key, val in pervertices.items():
        # print('kv: ', key, val)
        arr2save.append(val.vertex)
        arr2save.append(val.dcomp)
        # print('arr2save', arr2save)
    # print('arr2save', len(arr2save), arr2save)

    # np.savetxt("perv_d_dcomp" + str(dim) + ".csv",  arr2save, fmt='%s', delimiter=',', newline='\n')
    # np.save("perv_d_dcomp" + str(dim) + ".csv",  arr2save)

    ################################save all vertices
    arr2saveall = []
    for key, val in reduceruptoperm(ptsobnct, False).items():
        # print('kv: ', key, val)
        arr2saveall.append(val.vertex)
        arr2saveall.append(val.dcomp)
        # print('arr2save', arr2save)
    # print('arr2saveall', len(arr2saveall), arr2saveall)
    return arr2save, arr2saveall


def picw(dim, arr2save, filenameprefix='perv_d_dcomp'):
    with open("pickelfile/"+ filenameprefix + str(dim) + ".pkl", 'wb') as fp:
        pickle.dump(arr2save, fp)

    with open("pickelfile/"+ filenameprefix + str(dim) + ".pkl", 'rb') as fp:
        itemlist =pickle.load(fp)
    print('gradpro.six003deluxe.picw    itemlist', itemlist)

def picr(dim, filenameprefix='perv_d_dcomp'):
    with open("pickelfile/"+ filenameprefix + str(dim) + ".pkl", 'rb') as fp:
        itemlist =pickle.load(fp)
    # print('gradpro.six003deluxe.picr    itemlist', itemlist)
    return itemlist

def funcDcomp5plus(dim):
    k = 2**(dim-1)
    gervec = list(itertools.product(range(2), repeat=dim))
    # print('ger: ',gervec)
    gervec.remove((0,)*dim)
    print('ger: ', gervec)
    ptsobnct = {}
    ptsnct2st = set()
    for r in range(1, len(gervec)+1):
        print('rth:', r)
        start_time = time.time()
        comb = itertools.combinations(gervec, r)
        for lists in comb:
            # print('lists: ', lists)
            pt = np.array(lists).sum(axis=0, dtype=int)
            ptsstr = np.array2string(pt, separator=',')
            if ptsstr in ptsnct2st:
                continue
            elif ptsstr in ptsobnct:
                ptsobnct[ptsstr] = 2
                ptsnct2st.add(ptsstr)
            else:
                ptob = Point(pt, np.array(lists))
                ptsobnct[ptsstr] = ptob

        print('time rth: ', time.time()-start_time)


    ptsobnct = {key: val for key, val in ptsobnct.items() if val != 2}
    # print('all vertices', ptsob)

    # np.savetxt("all d" + str(dim) + ".csv", pts[hull.vertices], fmt='%s', delimiter=',', newline='\n')

    def reduceruptoperm(ptsob, uptocentral=True):
    #################reduce up to permutation
        perverticesset = set()
        dkverticesq = queue.PriorityQueue()
        pervertices = {}
        for key, val in ptsob.items():
            vertex = val.vertex
            # print('vertex； ', vertex)
            vertex = np.sort(vertex)
            vertexstr = ''.join(np.array2string(vertex, separator=','))
            if vertexstr in perverticesset: ########because the smallest permutation is visited first
                continue

    ################# sum x_i = dk/2 minimize the number of coordinates larger than k/2
            if sum(vertex) == dim*k/2 and uptocentral:
                perverticesset.add(vertexstr)
                dkverticesq.put(((vertex > k/2).sum(), key, val))
                continue
    ################ sum x_i = dk/2 minimize the number of coordinates larger than k/2

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
        return pervertices

    ################################save all vertices
    arr2saveall = []
    for key, val in reduceruptoperm(ptsobnct, False).items():
        # print('kv: ', key, val)
        arr2saveall.append(val.vertex)
        arr2saveall.append(val.dcomp)
        # print('arr2save', arr2save)
    # print('arr2saveall', len(arr2saveall), arr2saveall)
    return arr2saveall


# res= funcDcomp5plus(4)
# print(len(res), res)
# picw(5, funcDcomp5plus(5), 'testperv_dcomp_nct')
# picw(4, funcDcomp(4, True), 'perv_dcomp')
# funcC1()

# picw(5, [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,2],[0,0,0,2,2],[0,0,1,1,3],[0,0,1,3,3],[0,0,2,2,4],[0,0,2,3,4],[0,0,3,4,4],
# [0,0,4,4,4],[0,1,1,1,4],[0,1,1,4,4],[0,1,2,2,5],[0,1,2,4,5],[0,1,3,5,5],[0,1,5,5,5],[0,2,2,3,6],[0,2,2,4,6],
# [0,2,4,6,6],[0,2,5,6,6],[0,3,3,3,7],[0,3,3,5,7],[0,3,4,6,7],[0,3,6,6,7],[0,4,4,4,8],[0,4,4,5,8],[0,4,4,7,7],
# [0,4,5,6,8],[0,4,6,6,8],[0,4,7,7,7],[0,5,5,7,8],[0,5,7,7,8],[0,6,6,8,8],[0,6,7,8,8],[0,7,8,8,8],[0,8,8,8,8],
# [1,1,1,1,5],[1,1,1,5,5],[1,1,2,2,6],[1,1,2,5,6],[1,1,3,6,6],[1,1,6,6,6],[1,2,2,3,7],[1,2,2,5,7],[1,2,4,7,7],
# [1,2,6,7,7],[1,3,3,3,8],[1,3,3,6,8],[1,3,4,7,8],[1,3,7,7,8],[1,4,4,4,9],[1,4,4,6,9],[1,4,4,8,8],[1,4,5,7,9],
# [1,4,7,7,9],[1,4,8,8,8],[1,5,5,8,9],[1,5,8,8,9],[1,6,6,9,9],[1,6,8,9,9],[1,7,9,9,9],[1,9,9,9,9],[2,2,2,4,8],
# [2,2,2,5,8],[2,2,5,8,8],[2,2,6,8,8],[2,3,3,4,9],[2,3,3,6,9],[2,3,5,8,9],[2,3,7,8,9],[2,4,4,5,10],[2,4,4,6,10],
# [2,4,5,9,9],[2,4,6,8,10],[2,4,7,8,10],[2,4,8,9,9],[2,5,6,9,10],[2,5,8,9,10],[2,6,7,10,10],[2,6,8,10,10],
# [3,3,4,4,10],[3,3,4,7,10],[3,3,5,8,10],[3,3,8,8,10],[3,4,5,5,11],[3,4,5,7,11],
# [3,4,6,8,11],[3,4,8,8,11],[3,4,9,9,10],[3,5,5,10,10],[3,5,9,9,11],[3,6,6,10,11],[3,7,7,11,11],
# [4,4,4,4,11],[4,4,4,8,11],[4,4,5,9,11],[4,4,6,6,12],[4,4,6,7,12],[4,4,7,8,12],[4,4,8,8,12],
# [4,4,10,10,10],[4,5,5,5,12],[4,5,5,8,12],[4,5,5,10,11],[4,5,6,9,12],[4,6,6,10,12],[5,5,5,11,11],
# [5,5,6,6,13],[5,5,6,8,13],[5,5,7,9,13],[6,6,6,7,14],[6,6,6,8,14]], 'perv')

# twodvertices = funcDcomp(5)
# picw(5, twodvertices[1], 'testperv_dcomp_nct')
# picw(5, twodvertices[0], 'testperv_dcomp')

# leqflag=False
# print(3 > 4 and leqflag or 3 < 4 and not leqflag )
# res = picr(3)
# print(picr(3))