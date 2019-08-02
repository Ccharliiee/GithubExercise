import numpy as np
import itertools
import gradpro.six003deluxe as sd
import gradpro.heur1funcs as h1func
#############ask how to check permut



dim = 5
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
    # vcand.append(np.array([1, 1, 3]))
    # vcand.append(np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1]]))       # 1111d's generator
    ###############4
    # vcand.append(np.array([1, 1, 1, 4]))
    # vcand.append(np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]]))       # 1111d's generator
    # vcand.append(np.array([3, 3, 3, 7]))
    # vcand.append(np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]))  # k/2-1 … k/2-1 k-1's generator
    ###############5
    vcand.append(np.array([1, 1, 1, 1, 5]))
    vcand.append(np.array([[0, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 1]]))  # 1111d's generator
    vcand.append(np.array([1, 9, 9, 9, 9]))
    twokplus1 = [[1]*dim]
    for gen in itertools.product(range(2), repeat=dim-1):
        twokplus1.append(np.insert(gen, 0, 0))
    vcand.append(np.array(twokplus1)) # k/2-1 … k/2-1 k-1's generator

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
        vcanddict[''.join(np.array2string(vcand[i], separator=','))] = vcandval
    # print('vcandval: ', vcanddict)
    for deterp in determinedpoints:
        vcanddict.pop(''.join(np.array2string(deterp, separator=',')))
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
        verticesdict[''.join(np.array2string(np.array(ver), separator=','))] = ver
    for nonver in nonverticesdict:
        nonverticesdict[''.join(np.array2string(np.array(nonver), separator=','))] = nonver

    print('verticesdict:', verticesdict, 'len', len(verticesdict))
    print('nonvertices:', nonverticesdict, 'len', len(nonverticesdict))
    ###################################################

    ################### get all edges in dim
    edges = list(itertools.product(range(2), repeat=dim))
    edgesdict = {}
    for edge in np.array(edges[1:]):
        edgesdict[''.join(np.array2string(edge, separator=','))] = edge
    print('edges:', edgesdict)
    #############################

    undeterpts={}
    for vcandob in vcandobs:  #######starting point
        edgeavail = edgesdict.copy()

        for gernerator in vcandob.dcomp:
            gerstr = ''.join(np.array2string(np.array(gernerator), separator=','))
            if gerstr in edgesdict.keys():
                edgeavail.pop(gerstr)
        # print('point', vcandob)
        # print('edgeavailable:', edgeavail.values())

        for forward in edgeavail.values():
            newpoint = np.add(vcandob.vertex, forward)
            newpointstr = ''.join(np.array2string(np.array(sorted(newpoint)), separator=','))
            dcomp = np.append(vcandob.dcomp, [forward], axis=0)  ######add new vertex? back to iteration
            ptob = sd.Point(newpoint, dcomp)
            if newpointstr in verticesdict:
                continue
            elif newpointstr in nonverticesdict:
                continue
            elif newpointstr in undeterpts:
                continue
            elif sum(np.isin(newpoint, (0, k))):
                continue
            elif sum(newpoint) > dim*k/2:
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
                undeterpts[newpointstr] = newpoint
                vcandobs.append(ptob)#will we meet a same pt 1+
                print('ptob：', ptob)
                # vcanddict[''.join(np.array2string(newpoint, separator=','))] = newpoint, dcomp
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
    print('FINALLLY: ', fg)


def verificationall():
    # vground = sd.picr(dim, 'perv_dcomp')
    # print('verificationall', len(vground[::2]), vground[::2])
    # resrunhau1 = runheu1()
    # resultvcand = {**resrunhau1[0], **resrunhau1[1]}
    # print(len(resultvcand), len(vground[::2]))
    # # print(resultvcand)
    # # print(vground)
    # for ver in vground[::2]:
    #     if ''.join(np.array2string(np.array(ver), separator=',')) not in resultvcand:
    #         print(False, ver)

    ####################d=5 only
    vground = sd.picr(dim, 'perv')
    print('verificationall', len(vground), vground)
    resultvcand = {**runheu1()[0], **runheu1()[1]}
    print(len(resultvcand), len(vground))
    for ver in vground:
        if ''.join(np.array2string(np.array(ver), separator=',')) not in resultvcand:
            print(False, ver)
verificationall()