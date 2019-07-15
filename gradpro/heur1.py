import numpy as np
import gradpro.six003deluxe as sd


dim = 3
k = 2**(dim-1)

vred= sd.picr(2, 'perv_dcomp_nct')
print('sv:', vred)

for i,item in enumerate(vred):
    vred[i] = np.insert(item, 0, 0, axis=i%2)

print('svl:',vred, 'len', len(vred))


# vcand = np.append(vred, np.array([1,1,3])) 0….0, 0…01, 1…1d, 0k/2…k/2, k/2-1 … k/2-1 k-1
vcand = list(vred)
vcand.append(np.array([1,1,3]))
vcand.append(np.array([[0,0,1], [0,1,1], [1,0,1]]))
print('vcand:',vcand, 'len', len(vcand))

# vertices = np.array(vcand)
vertices = vcand[::2]
print('vertices:',vertices, 'len', len(vertices))

nonvertices = []
for i in range(dim):
    nonvertices.append([1]*(dim-1)+[i])
print('nonvertices:',nonvertices, 'len', len(nonvertices))

determinedpoints = np.array([[0]*dim, [0,0,1], [0,2,2]])
vcanddict = {}
for i in range(0, len(vcand),2):
    vcandval = []
    vcandval.append(vcand[i])
    vcandval.append(vcand[i+1])
    vcanddict[' '.join(np.array2string(vcand[i], separator=','))] = vcandval
print('vcandval: ', vcanddict)
for deterp in determinedpoints:
    vcanddict.pop(' '.join(np.array2string(deterp, separator=',')))
print('Uvcandval: ', vcanddict)