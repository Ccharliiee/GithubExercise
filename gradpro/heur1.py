import numpy as np
import itertools
import gradpro.six003deluxe as sd

#############ask how to check permut

dim = 3

################### init vcand ver nonver
def initial(dim):
    k = 2**(dim-1)
    vred= sd.picr(2, 'perv_dcomp_nct')
    print('smallver:', vred)

    for i,item in enumerate(vred):
        vred[i] = np.insert(item, 0, 0, axis=i%2)

    # print('smallverlift:',vred, 'len', len(vred))


    # vcand = np.append(vred, np.array([1,1,3])) 0….0, 0…01, 1…1d, 0k/2…k/2, k/2-1 … k/2-1 k-1
    vcand = list(vred)
    vcand.append(np.array([1,1,3]))
    vcand.append(np.array([[0,0,1], [0,1,1], [1,0,1]]))
    # print('vcandbasic:', vcand, 'len', len(vcand))

    # vertices = np.array(vcand)
    vertices = vcand[::2]
    # print('vertices:',vertices, 'len', len(vertices))

    nonvertices = []
    for i in range(dim):
        nonvertices.append([1]*(dim-1)+[i])
    # print('nonvertices:',nonvertices, 'len', len(nonvertices))

    determinedpoints = np.array([[0]*dim, [0,0,1], [0,2,2]])
    vcanddict = {}
    for i in range(0, len(vcand),2):
        vcandval = []
        vcandval.append(vcand[i])
        vcandval.append(vcand[i+1])
        vcanddict[' '.join(np.array2string(vcand[i], separator=','))] = vcandval
    # print('vcandval: ', vcanddict)
    for deterp in determinedpoints:
        vcanddict.pop(' '.join(np.array2string(deterp, separator=',')))
    # print('Udetervcandval: ', vcanddict)

    return vcanddict, vertices, nonvertices

########################################


vcanddict, vertices, nonvertices = initial(dim)
print('vcanddict: ', vcanddict)
print('vertices:',vertices, 'len', len(vertices))
print('nonvertices:',nonvertices, 'len', len(nonvertices))
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
    print('edgeva:', edgeavail.values())

    for forward in edgeavail.values():
        newpoint = np.add(val[0], forward)
        print('newp ', newpoint)