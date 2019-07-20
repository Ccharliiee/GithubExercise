import numpy as np
import itertools
import gradpro.six003deluxe as sd
from gradpro.heur1funcs import conemembasmb as cmb
#############ask how to check permut




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

    # vcand = np.append(vred, np.array([1,1,3])) 0….0, 0…01, 1…1d, 0k/2…k/2, k/2-1 … k/2-1 k-1
    vcand = list(vred)
    vcand.append(np.array([1, 1, 1, 4]))
    vcand.append(np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]]))       # 1111d's generator
    # print('vcandbasic:', vcand, 'len', len(vcand))

    # vertices = np.array(vcand)
    vertices = vcand[::2]
    # print('vertices:',vertices, 'len', len(vertices))

    nonvertices = []
    for i in range(dim):
        nonvertices.append([1] * (dim - 1) + [i])
    # print('nonvertices:',nonvertices, 'len', len(nonvertices))

    determinedpoints = np.array([[0] * dim, [0, 0, 0, 1], [0, 4, 4, 4]])
    vcanddict = {}
    for i in range(0, len(vcand), 2):
        vcandval = []
        vcandval.append(vcand[i])
        vcandval.append(vcand[i + 1])
        vcanddict[' '.join(np.array2string(vcand[i], separator=','))] = vcandval
    # print('vcandval: ', vcanddict)
    for deterp in determinedpoints:
        vcanddict.pop(' '.join(np.array2string(deterp, separator=',')))
    # print('Udetervcandval: ', vcanddict)

    return vcanddict, vertices, nonvertices


########################################
dim = 4
k = 2 ** (dim - 1)
vcanddict, vertices, nonvertices = initial()
print('vcanddict: ', vcanddict)
print('vertices:', vertices, 'len', len(vertices))
print('nonvertices:', nonvertices, 'len', len(nonvertices))

#################################################hash vertex non vertex
verticesdict={}
nonverticesdict={}
undeterpts={}
for ver in vertices:
    verticesdict[' '.join(np.array2string(np.array(ver), separator=','))] = ver
for nonver in nonverticesdict:
    nonverticesdict[' '.join(np.array2string(np.array(nonver), separator=','))] = nonver

print('verticesdict:', verticesdict, 'len', len(verticesdict))
print('nonvertices:', nonverticesdict, 'len', len(nonverticesdict))
###################################################
edges = list(itertools.product(range(2), repeat=dim))
edgesdict = {}
for edge in np.array(edges[1:]):
    edgesdict[' '.join(np.array2string(edge, separator=','))] = edge
print('edges:', edgesdict)
for key, val in vcanddict.items():
    edgeavail = edgesdict.copy()

    for gernerator in val[1]:
        gerstr = ' '.join(np.array2string(np.array(gernerator), separator=','))
        if gerstr in edgesdict.keys():
            edgeavail.pop(gerstr)
    print('point', val)
    print('edgeavailable:', edgeavail.values())

    for forward in edgeavail.values():
        newpoint = np.add(val[0], forward)
        newpointstr = ' '.join(np.array2string(np.array(sorted(newpoint)), separator=','))
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
        elif cmb(newpoint):
            nonvertices.append(newpoint)
            nonverticesdict[newpointstr] = newpoint
            continue
        else:
            undeterpts[newpointstr] = newpoint
print('undeterpts ', undeterpts.keys())
vv = []
vv.append(' '.join(np.array2string(np.array([1, 1, 4, 4]), separator=',')))
vv.append(' '.join(np.array2string(np.array([1, 2, 2, 5]), separator=',')))
vv.append(' '.join(np.array2string(np.array([1, 3, 5, 5] ), separator=',')))
vv.append(' '.join(np.array2string(np.array([2, 2, 3, 6]), separator=',')))
vv.append(' '.join(np.array2string(np.array([2, 2, 4, 6]), separator=',')))
vv.append(' '.join(np.array2string(np.array([1, 2, 4, 5]), separator=',')))
fg=True
for v in vv:
    if v not in undeterpts.keys():
        fg=False
        print('missed: ', v)
print('FINALLLY: ', fg)