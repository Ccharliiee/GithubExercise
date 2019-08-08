# from gradpro.heur1 import dim, k
import numpy as np
import itertools
import collections
import gradpro.six003deluxe as sd

dim = 3
k = 2 ** (dim - 1)


def elcreate():
    inequalites = collections.defaultdict(list)
    for cnum in range(2, dim + 1):  # a loop from d choose 2 to to d choose d
        # print('cnum: ', cnum)
        for comb in itertools.combinations(range(dim), cnum):  # indices comb in d choose n
            # print('comb:', comb)
            el = np.zeros(dim, dtype=int)
            np.put(el, comb, 1)
            # print(el)
            inequality = [np.array2string(el, separator=',')] # destinatiion 1vector
            for i in itertools.combinations(comb, cnum - 1):
                # print('i: ', i)
                eli = np.zeros(dim, dtype=int)
                if cnum > 2:  # cnum > 2, i is all its decomposition
                    elri = np.zeros(dim, dtype=int)
                    oneindex = list(x for x in comb if x not in i)
                    np.put(elri, oneindex, 1)
                    inequality.append(np.array2string(elri, separator=','))
                np.put(eli, i, 1)
                inequality.append(np.array2string(eli, separator=','))
            # print('inequality： ', inequality)
            inequalites[cnum].append(inequality)
    # print('inequalites: ', inequalites)
    return inequalites

def elcreate11():
    inequalites = collections.defaultdict(list)
    for cnum in range(2, dim + 1):  # a loop from d choose 2 to to d choose d
        # print('cnum: ', cnum)
        for comb in itertools.combinations(range(dim), cnum):  # indices comb in d choose n
            # print('comb:', comb)
            el = np.zeros(dim, dtype=int)
            np.put(el, comb, 1)        #largest vector in this iteration
            # print(el)
            inequality = [np.array2string(el, separator=',')] # destinatiion 1vector
            for i in range((cnum+1)//2, cnum):
                # print('i: ', i)
                for j in itertools.combinations(comb, i):
                    # print('j: ', j)
                    eli = np.zeros(dim, dtype=int)
                    if cnum > 2:  # cnum > 2, i is all its decomposition
                        elri = np.zeros(dim, dtype=int)
                        oneindex = list(x for x in comb if x not in j)
                        np.put(elri, oneindex, 1)
                        inequality.append(np.array2string(elri, separator=','))
                    np.put(eli, j, 1)
                    inequality.append(np.array2string(eli, separator=','))
                # print('inequality： ', inequality)
                inequalites[cnum].append(inequality)
    # print('inequalites: ', inequalites)
    return inequalites
# elcreate11()

def epscheck(point:sd.Point):
    ###### create generatordict for passed in point
    generatordict = collections.defaultdict(int)
    for ger in point.dcomp:
        gerstr = np.array2string(np.array(ger), separator=',')
        # print(gerstr)
        generatordict[gerstr] = 1
    # print(generatordict)
    ###########/

    allepsdict = elcreate11()
    for k,v in allepsdict.items(): #k meams d choose k
        # print(k, v)
        if k==2:
            for vector in v: #2 [['[1,1,0]', '[1,0,0]', '[0,1,0]'], ['[1,0,1]', '[1,0,0]', '[0,0,1]'], ['[0,1,1]', '[0,1,0]', '[0,0,1]']]
                # print('vector: ', vector)
                if k*generatordict[vector[0]] + generatordict[vector[1]] + generatordict[vector[2]] == 2:
                    return False
        else:
            for vec in v:
                for i in range(1, len(vec),2): #3 [['[1,1,1]', '[0,0,1]', '[1,1,0]', '[0,1,0]', '[1,0,1]', '[1,0,0]', '[0,1,1]']]
                    # print('i', i)
                    # print('vector: ', vec[0], vec[i], vec[i+1])
                    if k*generatordict[vec[0]] + generatordict[vec[i]] + (k-1)*generatordict[vec[i+1]] == k:
                        return False
    return True
# point1=sd.Point([1,1,0], [[0,1,0], [1,0,0]])
# point2=sd.Point([1, 1, 1, 4], [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]])
# point3=sd.Point([1, 1, 3, 4], [[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 0, 1]])
# point4=sd.Point([2, 2, 5, 5], [[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]])
# print(epscheck(point4))

def conemembershipstemplate(point, coef1='', coef2='', const=0, coordsumthresh=dim * k / 2,
                            leqflag=True):  # if leq is in ineqs, leqflag=T
    coordsum = sum(point)
    if coordsum <= coordsumthresh and coef1 != '':  # if '', not in this case
        for i0 in point:  # check apex 0
            if coordsum - i0 > coef1 * i0 and leqflag or coordsum - i0 < coef1 * i0 and not leqflag:  # handle leq or geq
                # print('000 sk')
                return False
    elif coordsum >= coordsumthresh and coef2 != '':
        for i0 in point:  # check apex s(k)
            if coordsum - i0 > coef2 * i0 + const and leqflag or coordsum - i0 < coef2 * i0 + const and not leqflag:  # handle leq or geq
                return False
    # else:
    #     # print(insider)
    #     return True
    return True


def conememberships(point):
    coordsum = sum(point)
    insider = True
    if coordsum < 2 * dim - 1:
        for i0 in point:
            # if coordsum - i0 > (2*dim-2)*i0:
            if coordsum - i0 > (2 * dim - 2) * i0:
                insider = False
                print('000 111d')
                break
        return insider
    elif coordsum > 2 * dim - 1:
        for i0 in point:
            if coordsum - i0 > (k - 2) * (dim - 1) / (k - 1) * i0 + k * (dim - 1) / (k - 1):
                insider = False
                print('111d sk')
                break
        return insider
    else:
        print(insider)
        return insider


# conememberships([3, 3, 3])

#####################test1
# print(conemembershipstemplate([1, 1, 1], 2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1), 2 * dim - 1))
#
# print(conemembershipstemplate([1, 2, 2], dim-2, dim, -k, (dim-1)*k/2, False))
#
# print(conemembershipstemplate([2.5, 2, 2], '', dim-1-(1/k), 1, 1))
#
# print(conemembershipstemplate([0.5, 1.5, 1.5],(1/(k/2 +1)) + dim-2, dim+ (2/(k-2)), (-(2*k)/(k-2)) -k, (k/2 +1)*(dim-1) +1, False))
#
# print(conemembershipstemplate([2, 1.5, 2],(dim-1 -(1/k)), '', 0, dim*k -1, False))
#
# print(conemembershipstemplate([4, 4, 4],(k-2)*(dim-1)/(k-1), 2*(dim-1), -k*(dim-1), dim*k-2*dim-1, False))
#
# print(conemembershipstemplate([1, 1, 2], dim, '', 0, dim*k/2 + k/2))
#
# print(conemembershipstemplate([2.5, 2.5, 3.5], (dim*k-2*dim+2)/(k-2) , (dim-2) + 2/(k+2),  k*(1 - 2/(k+2)), dim*k/2 + k/2 -dim))
##################################test1/


#####################test2
point = [2, 2, 3, 6]


#
# print(conemembershipstemplate(point, 2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1), 2 * dim - 1))
#
# print(conemembershipstemplate(point, dim-2, dim, -k, (dim-1)*k/2, False))
#
# print(conemembershipstemplate(point, '', dim-1-(1/k), 1, 1))
#
# print(conemembershipstemplate(point,(1/(k/2 +1)) + dim-2, dim+ (2/(k-2)), (-(2*k)/(k-2)) -k, (k/2 +1)*(dim-1) +1, False))
#
# print(conemembershipstemplate(point,(dim-1 -(1/k)), '', 0, dim*k -1, False))
#
# print(conemembershipstemplate(point,(k-2)*(dim-1)/(k-1), 2*(dim-1), -k*(dim-1), dim*k-2*dim-1, False))
#
# print(conemembershipstemplate(point, dim, '', 0, dim*k/2 + k/2))
#
# print(conemembershipstemplate(point, (dim*k-2*dim+2)/(k-2) , (dim-2) + 2/(k+2),  k*(1 - 2/(k+2)), dim*k/2 + k/2 -dim))
##################################test2/

def conemembasmb(point):
    # if conemembershipstemplate(point, 2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1), 2 * dim - 1) or
    # conemembershipstemplate(point, dim - 2, dim, -k, (dim - 1) * k / 2, False) or conemembershipstemplate(point, '', dim-1-(1/k), 1, 1) or
    #     conemembershipstemplate(point, (1 / (k / 2 + 1)) + dim - 2, dim + (2 / (k - 2)), (-(2 * k) / (k - 2)) - k,
    #                             (k / 2 + 1) * (dim - 1) + 1, False) or conemembershipstemplate(point,(dim-1 -(1/k)), '', 0, dim*k -1, False) or
    #     conemembershipstemplate(point, (k - 2) * (dim - 1) / (k - 1), 2 * (dim - 1), -k * (dim - 1),
    #                             dim * k - 2 * dim - 1, False) or conemembershipstemplate(point, dim, '', 0, dim*k/2 + k/2) or
    #     conemembershipstemplate(point, (dim * k - 2 * dim + 2) / (k - 2), (dim - 2) + 2 / (k + 2),
    #                             k * (1 - 2 / (k + 2)), dim * k / 2 + k / 2 - dim)
    conemembs = [conemembershipstemplate(point, 2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1),
                                         2 * dim - 1),
                 conemembershipstemplate(point, dim - 2, dim, -k, (dim - 1) * k / 2, False),
                 conemembershipstemplate(point, '', dim - 1 - (1 / k), 1, 1),
                 conemembershipstemplate(point, (1 / (k / 2 + 1)) + dim - 2, dim + (2 / (k - 2)),
                                         (-(2 * k) / (k - 2)) - k, (k / 2 + 1) * (dim - 1) + 1, False),
                 conemembershipstemplate(point, (dim - 1 - (1 / k)), '', 0, dim * k - 1, False),
                 conemembershipstemplate(point, (k - 2) * (dim - 1) / (k - 1), 2 * (dim - 1), -k * (dim - 1),
                                         dim * k - 2 * dim - 1, False),
                 conemembershipstemplate(point, dim, '', 0, dim * k / 2 + k / 2),
                 conemembershipstemplate(point, (dim * k - 2 * dim + 2) / (k - 2), (dim - 2) + 2 / (k + 2),
                                         k * (1 - 2 / (k + 2)), dim * k / 2 + k / 2 - dim)
                 ]
    # for conememb in conemembs:
    #     if conememb:
    #         return True
    # return False
    conemembargs = [[2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1), 2 * dim - 1, True],
                    [dim - 2, dim, -k, (dim - 1) * k / 2, False],
                    ['', dim - 1 - (1 / k), 1, 1, True],
                    [(1 / (k / 2 + 1)) + dim - 2, dim + (2 / (k - 2)), (-(2 * k) / (k - 2)) - k,
                     (k / 2 + 1) * (dim - 1) + 1, False],
                    [(dim - 1 - (1 / k)), '', 0, dim * k - 1, False],
                    [(k - 2) * (dim - 1) / (k - 1), 2 * (dim - 1), -k * (dim - 1), dim * k - 2 * dim - 1, False],
                    [dim, '', 0, dim * k / 2 + k / 2, True],
                    [(dim * k - 2 * dim + 2) / (k - 2), (dim - 2) + 2 / (k + 2), k * (1 - 2 / (k + 2)),
                     dim * k / 2 + k / 2 - dim, True]

                    ]
    for i, carg in enumerate(conemembargs):
        if conemembershipstemplate(point, carg[0], carg[1], carg[2], carg[3], carg[4]):
            # print(i, 'index: ', carg)
            return True
    return False


# print(conemembasmb(point))


# print(np.fromstring('[0 0 0 0 0], [0 0 0 0 1], [0 0 0 1 2], [0 0 0 2 2], [0 0 1 1 3], [0 0 1 3 3], [0 0 2 2 4], [0 0 2 3 4], [0 0 3 4 4], [0 0 4 4 4], [0 1 1 1 4], [0 1 1 4 4], [0 1 2 2 5], [0 1 2 4 5], [0 1 3 5 5], [0 1 5 5 5], [0 2 2 3 6], [0 2 2 4 6], [0 2 4 6 6], [0 2 5 6 6], [0 3 3 3 7], [0 3 3 5 7], [0 3 4 6 7], [0 3 6 6 7], [0 4 4 4 8], [0 4 4 5 8], [0 4 4 7 7], [0 4 5 6 8], [0 4 6 6 8], [0 4 7 7 7], [0 5 5 7 8], [0 5 7 7 8], [0 6 6 8 8], [0 6 7 8 8], [0 7 8 8 8], [0 8 8 8 8], [1 1 1 1 5], [1 1 1 5 5], [1 1 2 2 6], [1 1 2 5 6], [1 1 3 6 6], [1 1 6 6 6], [1 2 2 3 7], [1 2 2 5 7], [1 2 4 7 7], [1 2 6 7 7], [1 3 3 3 8], [1 3 3 6 8], [1 3 4 7 8], [1 3 7 7 8], [1 4 4 4 9], [1 4 4 6 9], [1 4 4 8 8], [1 4 5 7 9], [1 4 7 7 9], [1 4 8 8 8], [1 5 5 8 9], [1 5 8 8 9], [1 6 6 9 9], [1 6 8 9 9], [1 7 9 9 9], [1 9 9 9 9], [2 2 2 4 8], [2 2 2 5 8], [2 2 5 8 8], [2 2 6 8 8], [2 3 3 4 9], [2 3 3 6 9], [2 3 5 8 9], [2 3 7 8 9], [ 2 4 4 5 10], [ 2 4 4 6 10], [2 4 5 9 9], [ 2 4 6 8 10], [ 2 4 7 8 10], [2 4 8 9 9], [ 2 5 6 9 10], [ 2 5 8 9 10], [ 2 6 7 10 10], [ 2 6 8 10 10], [ 2 8 10 10 10], [ 3 3 4 4 10], [ 3 3 4 7 10], [ 3 3 5 8 10], [ 3 3 8 8 10], [ 3 4 5 5 11], [ 3 4 5 7 11], [ 3 4 6 8 11], [ 3 4 8 8 11], [ 3 4 9 9 10], [ 3 5 5 10 10], [ 3 5 9 9 11], [ 3 6 6 10 11], [ 3 7 7 11 11], [ 4 4 4 4 11], [ 4 4 4 8 11], [ 4 4 5 9 11], [ 4 4 6 6 12], [ 4 4 6 7 12], [ 4 4 7 8 12], [ 4 4 8 8 12], [ 4 4 10 10 10], [ 4 5 5 5 12], [ 4 5 5 8 12], [ 4 5 5 10 11], [ 4 5 6 9 12], [ 4 6 6 10 12], [ 5 5 5 11 11], [ 5 5 6 6 13], [ 5 5 6 8 13], [ 5 5 7 9 13], [ 6 6 6 7 14]',
#               dtype=int, sep=' '
#
#               ))
# print('[0 0 0 0 0], [0 0 0 0 1], [0 0 0 1 2], [0 0 0 2 2], [0 0 1 1 3], [0 0 1 3 3], [0 0 2 2 4], [0 0 2 3 4], [0 0 3 4 4], [0 0 4 4 4], [0 1 1 1 4], [0 1 1 4 4], [0 1 2 2 5], [0 1 2 4 5], [0 1 3 5 5], [0 1 5 5 5], [0 2 2 3 6], [0 2 2 4 6], [0 2 4 6 6], [0 2 5 6 6], [0 3 3 3 7], [0 3 3 5 7], [0 3 4 6 7], [0 3 6 6 7], [0 4 4 4 8], [0 4 4 5 8], [0 4 4 7 7], [0 4 5 6 8], [0 4 6 6 8], [0 4 7 7 7], [0 5 5 7 8], [0 5 7 7 8], [0 6 6 8 8], [0 6 7 8 8], [0 7 8 8 8], [0 8 8 8 8], [1 1 1 1 5], [1 1 1 5 5], [1 1 2 2 6], [1 1 2 5 6], [1 1 3 6 6], [1 1 6 6 6], [1 2 2 3 7], [1 2 2 5 7], [1 2 4 7 7], [1 2 6 7 7], [1 3 3 3 8], [1 3 3 6 8], [1 3 4 7 8], [1 3 7 7 8], [1 4 4 4 9], [1 4 4 6 9], [1 4 4 8 8], [1 4 5 7 9], [1 4 7 7 9], [1 4 8 8 8], [1 5 5 8 9], [1 5 8 8 9], [1 6 6 9 9], [1 6 8 9 9], [1 7 9 9 9], [1 9 9 9 9], [2 2 2 4 8], [2 2 2 5 8], [2 2 5 8 8], [2 2 6 8 8], [2 3 3 4 9], [2 3 3 6 9], [2 3 5 8 9], [2 3 7 8 9], [ 2 4 4 5 10], [ 2 4 4 6 10], [2 4 5 9 9], [ 2 4 6 8 10], [ 2 4 7 8 10], [2 4 8 9 9], [ 2 5 6 9 10], [ 2 5 8 9 10], [ 2 6 7 10 10], [ 2 6 8 10 10], [ 2 8 10 10 10], [ 3 3 4 4 10], [ 3 3 4 7 10], [ 3 3 5 8 10], [ 3 3 8 8 10], [ 3 4 5 5 11], [ 3 4 5 7 11], [ 3 4 6 8 11], [ 3 4 8 8 11], [ 3 4 9 9 10], [ 3 5 5 10 10], [ 3 5 9 9 11], [ 3 6 6 10 11], [ 3 7 7 11 11], [ 4 4 4 4 11], [ 4 4 4 8 11], [ 4 4 5 9 11], [ 4 4 6 6 12], [ 4 4 6 7 12], [ 4 4 7 8 12], [ 4 4 8 8 12], [ 4 4 10 10 10], [ 4 5 5 5 12], [ 4 5 5 8 12], [ 4 5 5 10 11], [ 4 5 6 9 12], [ 4 6 6 10 12], [ 5 5 5 11 11], [ 5 5 6 6 13], [ 5 5 6 8 13], [ 5 5 7 9 13], '
#       '[ 6 6 6 7 14]'.split(','))

fivedelbracket = '[0 0 0 0 0], [0 0 0 0 1], [0 0 0 1 2], [0 0 0 2 2], [0 0 1 1 3], [0 0 1 3 3], [0 0 2 2 4], ' \
                 '[0 0 2 3 4], [0 0 3 4 4], [0 0 4 4 4], [0 1 1 1 4], [0 1 1 4 4], [0 1 2 2 5], [0 1 2 4 5], ' \
                 '[0 1 3 5 5], [0 1 5 5 5], [0 2 2 3 6], [0 2 2 4 6], [0 2 4 6 6], [0 2 5 6 6], [0 3 3 3 7], ' \
                 '[0 3 3 5 7], [0 3 4 6 7], [0 3 6 6 7], [0 4 4 4 8], [0 4 4 5 8], [0 4 4 7 7], [0 4 5 6 8], ' \
                 '[0 4 6 6 8], [0 4 7 7 7], [0 5 5 7 8], [0 5 7 7 8], [0 6 6 8 8], [0 6 7 8 8], [0 7 8 8 8], ' \
                 '[0 8 8 8 8], [1 1 1 1 5], [1 1 1 5 5], [1 1 2 2 6], [1 1 2 5 6], [1 1 3 6 6], [1 1 6 6 6], ' \
                 '[1 2 2 3 7], [1 2 2 5 7], [1 2 4 7 7], [1 2 6 7 7], [1 3 3 3 8], [1 3 3 6 8], [1 3 4 7 8], ' \
                 '[1 3 7 7 8], [1 4 4 4 9], [1 4 4 6 9], [1 4 4 8 8], [1 4 5 7 9], [1 4 7 7 9], [1 4 8 8 8], ' \
                 '[1 5 5 8 9], [1 5 8 8 9], [1 6 6 9 9], [1 6 8 9 9], [1 7 9 9 9], [1 9 9 9 9], [2 2 2 4 8], ' \
                 '[2 2 2 5 8], [2 2 5 8 8], [2 2 6 8 8], [2 3 3 4 9], [2 3 3 6 9], [2 3 5 8 9], [2 3 7 8 9], ' \
                 '[ 2 4 4 5 10], [ 2 4 4 6 10], [2 4 5 9 9], [ 2 4 6 8 10], [ 2 4 7 8 10], [2 4 8 9 9], ' \
                 '[ 2 5 6 9 10], [ 2 5 8 9 10], [ 2 6 7 10 10], [ 2 6 8 10 10], [ 2 8 10 10 10], [ 3 3 4 4 10], ' \
                 '[ 3 3 4 7 10], [ 3 3 5 8 10], [ 3 3 8 8 10], [ 3 4 5 5 11], [ 3 4 5 7 11], [ 3 4 6 8 11], ' \
                 '[ 3 4 8 8 11], [ 3 4 9 9 10], [ 3 5 5 10 10], [ 3 5 9 9 11], [ 3 6 6 10 11], [ 3 7 7 11 11], ' \
                 '[ 4 4 4 4 11], [ 4 4 4 8 11], [ 4 4 5 9 11], [ 4 4 6 6 12], [ 4 4 6 7 12], [ 4 4 7 8 12], ' \
                 '[ 4 4 8 8 12], [ 4 4 10 10 10], [ 4 5 5 5 12], [ 4 5 5 8 12], [ 4 5 5 10 11], [ 4 5 6 9 12], ' \
                 '[ 4 6 6 10 12], [ 5 5 5 11 11], [ 5 5 6 6 13], [ 5 5 6 8 13], [ 5 5 7 9 13],[ 6 6 6 7 14]'.replace(
    '[', '').replace(']', '')
# print(fivedelbracket)
fivew2com = '[0 0 0 0 0], [0 0 0 0 1], [0 0 0 1 2], [0 0 0 2 2], [0 0 1 1 3], [0 0 1 3 3], [0 0 2 2 4], ' \
            '[0 0 2 3 4], [0 0 3 4 4], [0 0 4 4 4], [0 1 1 1 4], [0 1 1 4 4], [0 1 2 2 5], [0 1 2 4 5], ' \
            '[0 1 3 5 5], [0 1 5 5 5], [0 2 2 3 6], [0 2 2 4 6], [0 2 4 6 6], [0 2 5 6 6], [0 3 3 3 7], ' \
            '[0 3 3 5 7], [0 3 4 6 7], [0 3 6 6 7], [0 4 4 4 8], [0 4 4 5 8], [0 4 4 7 7], [0 4 5 6 8], ' \
            '[0 4 6 6 8], [0 4 7 7 7], [0 5 5 7 8], [0 5 7 7 8], [0 6 6 8 8], [0 6 7 8 8], [0 7 8 8 8], ' \
            '[0 8 8 8 8], [1 1 1 1 5], [1 1 1 5 5], [1 1 2 2 6], [1 1 2 5 6], [1 1 3 6 6], [1 1 6 6 6], ' \
            '[1 2 2 3 7], [1 2 2 5 7], [1 2 4 7 7], [1 2 6 7 7], [1 3 3 3 8], [1 3 3 6 8], [1 3 4 7 8], ' \
            '[1 3 7 7 8], [1 4 4 4 9], [1 4 4 6 9], [1 4 4 8 8], [1 4 5 7 9], [1 4 7 7 9], [1 4 8 8 8], ' \
            '[1 5 5 8 9], [1 5 8 8 9], [1 6 6 9 9], [1 6 8 9 9], [1 7 9 9 9], [1 9 9 9 9], [2 2 2 4 8], ' \
            '[2 2 2 5 8], [2 2 5 8 8], [2 2 6 8 8], [2 3 3 4 9], [2 3 3 6 9], [2 3 5 8 9], [2 3 7 8 9], ' \
            '[ 2 4 4 5 10], [ 2 4 4 6 10], [2 4 5 9 9], [ 2 4 6 8 10], [ 2 4 7 8 10], [2 4 8 9 9], ' \
            '[ 2 5 6 9 10], [ 2 5 8 9 10], [ 2 6 7 10 10], [ 2 6 8 10 10], [ 2 8 10 10 10], [ 3 3 4 4 10], ' \
            '[ 3 3 4 7 10], [ 3 3 5 8 10], [ 3 3 8 8 10], [ 3 4 5 5 11], [ 3 4 5 7 11], [ 3 4 6 8 11], ' \
            '[ 3 4 8 8 11], [ 3 4 9 9 10], [ 3 5 5 10 10], [ 3 5 9 9 11], [ 3 6 6 10 11], [ 3 7 7 11 11], ' \
            '[ 4 4 4 4 11], [ 4 4 4 8 11], [ 4 4 5 9 11], [ 4 4 6 6 12], [ 4 4 6 7 12], [ 4 4 7 8 12], ' \
            '[ 4 4 8 8 12], [ 4 4 10 10 10], [ 4 5 5 5 12], [ 4 5 5 8 12], [ 4 5 5 10 11], [ 4 5 6 9 12], ' \
            '[ 4 6 6 10 12], [ 5 5 5 11 11], [ 5 5 6 6 13], [ 5 5 6 8 13], [ 5 5 7 9 13],[ 6 6 6 7 14]'.replace(' ',
                                                                                                                ',').replace(
    ',,', ',')
# print(fivew2com)

# print(np.array([[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,2],[0,0,0,2,2],[0,0,1,1,3],[0,0,1,3,3],[0,0,2,2,4],[0,0,2,3,4],[0,0,3,4,4],
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
# [5,5,6,6,13],[5,5,6,8,13],[5,5,7,9,13],[6,6,6,7,14],[6,6,6,7,14]]))

# print(conemembasmb([1, 2, 4, 7, 7]))
