import numpy as np
import itertools

from scipy.spatial.qhull import ConvexHull

import gradpro.six003deluxe as sd
import gradpro.heur1funcs as h1func
#############ask how to check permut



dim = 3
k = 2 ** (dim - 1)

################### init vcand ver nonver
def initial():
    k = 2 ** (dim - 1)
    vred = sd.picr(dim-1, 'perv_dcomp_nct') # nct: non center symm
    print('smallver:', vred)
    vredsym = []
    for i, item in enumerate(vred):
        # oddev = i % 2
        vred[i] = np.insert(item, 0, 0, axis=i % 2)
    #     if not oddev:
    #         vredsym.append(sorted(np.subtract([k] * dim, vred[i])))
    # vred = vred + vredsym
    # print('smallverlift:',vred, 'len', len(vred))

    vcand = list(vred)

    # vcand = np.append(vred, np.array([1,1,3]))#0….0, 0…01, 1…1d, 0k/2…k/2, k/2-1 … k/2-1 k-1
    ###############3
    vcand.append(np.array([1, 1, 3]))
    vcand.append(np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1]]))       # 1111d's generator
    ###############4
    # vcand.append(np.array([1, 1, 1, 4]))
    # vcand.append(np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]]))       # 1111d's generator
    # vcand.append(np.array([3, 3, 3, 7]))
    # vcand.append(np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]))  # k/2-1 … k/2-1 k-1's generator
    ###############5
    # vcand.append(np.array([1, 1, 1, 1, 5]))
    # vcand.append(np.array([[0, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 1]]))  # 1111d's generator
    # vcand.append(np.array([1, 9, 9, 9, 9]))
    # twokplus1 = [[1]*dim]
    # for gen in itertools.product(range(2), repeat=dim-1):
    #     twokplus1.append(np.insert(gen, 0, 0))
    # vcand.append(np.array(twokplus1)) # k/2-1 … k/2-1 k-1's generator

    # print('vcandbasic:', vcand, 'len', len(vcand))

    # vertices = np.array(vcand)
    vertices = vcand[::2]
    # print('vertices:',vertices, 'len', len(vertices))

    nonvertices = []
    for i in range(dim):
        nonvertices.append([1] * (dim - 1) + [i])
    # print('nonvertices:',nonvertices, 'len', len(nonvertices))

    determinedpoints = np.array([[0] * dim, [0] * (dim-1)+[1], [0]+[k//2]*(dim-1)])
    vcanddict = {}
    for i in range(0, len(vcand), 2):
        vcandval = []
        vcandval.append(vcand[i])
        vcandval.append(vcand[i + 1])
        vcanddict[np.array2string(vcand[i], separator=',')] = vcandval
    # print('vcandval: ', vcanddict)
    for deterp in determinedpoints:
        vcanddict.pop(np.array2string(deterp, separator=','))
    # print('Udetervcandval: ', vcanddict)

    vcandobs = []
    for verger in vcanddict.values():
        vcandob = sd.Point(verger[0], verger[1])
        vcandobs.append(vcandob)
    return vcandobs, vertices, nonvertices
##########vcandobs is with vertex and generator

########################################

def runheu1():
    vcandobs, vertices, nonvertices = initial()
    print('vcandobs: ', vcandobs)
    print('vertices:', vertices, 'len', len(vertices))
    print('nonvertices:', nonvertices, 'len', len(nonvertices))

    ################################################hash vertex non vertex
    verticesdict={}
    nonverticesdict={}

    for ver in vertices:
        verticesdict[np.array2string(np.array(ver), separator=',')] = ver
    for nonver in nonvertices:
        nonverticesdict[np.array2string(np.array(nonver), separator=',')] = nonver

    print('verticesdict:', verticesdict, 'len', len(verticesdict))
    print('nonvertices:', nonverticesdict, 'len', len(nonverticesdict))
    ###################################################

    ################### get all edges in dim
    edges = list(itertools.product(range(2), repeat=dim))
    edgesdict = {}
    for edge in np.array(edges[1:]):
        edgesdict[np.array2string(edge, separator=',')] = edge
    print('edges:', edgesdict)
    #############################

    undeterpts={}
    twodksum = dim+1
    twodk = [0,0]
    for vcandob in vcandobs:  #######starting point
        edgeavail = edgesdict.copy()

        for gernerator in vcandob.dcomp:
            gerstr = np.array2string(np.array(gernerator), separator=',')
            if gerstr in edgesdict.keys():
                edgeavail.pop(gerstr)
        # print('point', vcandob)
        # print('edgeavailable:', edgeavail.values())

        for forward in edgeavail.values():
            newpoint = np.add(vcandob.vertex, forward)
            newpointstr = np.array2string(np.array(sorted(newpoint)), separator=',')
            dcomp = np.append(vcandob.dcomp, [forward], axis=0)  ######add new vertex? back to iteration
            ptob = sd.Point(newpoint, dcomp, vcandob.vertex)
            if newpointstr in verticesdict or newpointstr in nonverticesdict or newpointstr in undeterpts\
                    or sum(np.isin(newpoint, (0, k))) or sum(newpoint) > dim*k/2:
                continue
            # elif newpointstr in nonverticesdict:
            #     continue
            # elif newpointstr in undeterpts:
            #     continue
            # elif sum(np.isin(newpoint, (0, k))):
            #     continue
            # elif sum(newpoint) > dim*k/2:
            #     continue
            elif sum(newpoint) == dim*k/2 and (newpoint > k/2).sum() >= twodksum:
                continue
            elif h1func.conemembasmb(newpoint):
                nonvertices.append(newpoint)
                nonverticesdict[newpointstr] = newpoint
                continue
            elif not h1func.epscheck(ptob):
                nonvertices.append(newpoint)
                nonverticesdict[newpointstr] = newpoint
                continue
            else:
                if sum(newpoint) == dim*k/2:
                    twodksum = (newpoint > k/2).sum()
                    twodk[0] = newpointstr
                    twodk[1] = ptob
                else:
                    undeterpts[newpointstr] = ptob
                    vcandobs.append(ptob)#will we meet a same pt 1+
                # print('ptob：', ptob)
                # vcanddict[''.join(np.array2string(newpoint, separator=','))] = newpoint, dcomp
    if twodk[0] != 0:
        undeterpts[twodk[0]]=twodk[1]
    print('undeterpts ', undeterpts.keys())
    return undeterpts, verticesdict
########only vertices no generator

def verificationbk():
    vv = []
    vv.append(''.join(np.array2string(np.array([1, 1, 4, 4]), separator=',')))
    vv.append(''.join(np.array2string(np.array([1, 2, 2, 5]), separator=',')))
    vv.append(''.join(np.array2string(np.array([1, 3, 5, 5] ), separator=',')))
    vv.append(''.join(np.array2string(np.array([2, 2, 3, 6]), separator=',')))
    vv.append(''.join(np.array2string(np.array([2, 2, 4, 6]), separator=',')))
    vv.append(''.join(np.array2string(np.array([1, 2, 4, 5]), separator=',')))
    fg=True
    for v in vv:
        if v not in runheu1()[0].keys():
            fg=False
            print('missed: ', v)
    for v in runheu1()[0].keys():
        if v not in vv:
            print('wrong: ', v)
    print('FINALLLY: ', fg)
# verificationbk()

def verificationall():
    vground = sd.picr(dim, 'perv_dcomp')
    print('verificationall', len(vground[::2]), vground[::2])
    resrunhau1 = runheu1()
    resultvcand = {**resrunhau1[0], **resrunhau1[1]}
    print(len(resultvcand), len(vground[::2]))
    # print(resultvcand)
    # print(vground)
    for ver in vground[::2]:
        if ''.join(np.array2string(np.array(ver), separator=',')) not in resultvcand:
            print(False, ver)

    ####################d=5 only
    # vground = sd.picr(dim, 'perv')
    # print('verificationall', len(vground), vground)
    # vgrounddict ={}
    # for ver in vground:
    #     vgrounddict[np.array2string(np.array(ver), separator=',')]=ver
    # resultvcand = runheu1()
    # resultvcand = {**resultvcand[0], **resultvcand[1]}
    # print('len(resultvcand), len(vground): ',len(resultvcand), len(vground))
    # for ver in vground: #check missed
    #     if np.array2string(np.array(ver), separator=',') not in resultvcand:
    #         print(False, ver)
    # pts = []
    # for ptr, ptob in resultvcand.items():#check wrong
    #     # print('ptsfromstr: ', np.fromstring(ptr[1:-1], dtype=int, sep=','))
    #     if ptr == np.array2string(np.array([2, 8, 10, 10, 10]), separator=','):
    #         print('EXIST: ', [2, 8, 10, 10, 10])
    #         continue
    #     pts.append(np.fromstring(ptr[1:-1], dtype=int, sep=','))
    #
    #     if ptr not in vgrounddict:
    #         print('wrong point: ', ptob)
    # pts = np.array(pts)
    # hull = ConvexHull(pts)
    # print('hull: ', len(pts[hull.vertices]), pts[hull.vertices], 'end')
    # ptsdict = {}
    # for pt in pts[hull.vertices]:
    #     ptsdict[np.array2string(np.array(pt), separator=',')] = pt
    # for ver in vground:  #check missed
    #     if np.array2string(np.array(ver), separator=',') not in ptsdict:
    #         print(False, ver)
    # for pstr in ptsdict.keys(): #check wrong
    #     if pstr not in vgrounddict:
    #         print('wrong point: ', pstr)
verificationall()