from gradpro.heur1 import dim, k
import numpy as np


def conemembershipstemplate(point, coef1='', coef2='', const=0, coordsumthresh=dim * k / 2,
                            leqflag=True):  # if leq is in ineqs, leqflag=T
    coordsum = sum(point)
    if coordsum < coordsumthresh and coef1 != '':  # if '', not in this case
        for i0 in point: #check apex 0
            if coordsum - i0 > coef1 * i0 and leqflag or coordsum - i0 < coef1 * i0 and not leqflag:  # handle leq or geq
                # print('000 sk')
                return False
    elif coordsum > coordsumthresh and coef2 != '':
        for i0 in point: #check apex s(k)
            if coordsum - i0 > coef2 * i0 + const and leqflag or coordsum - i0 < coef2 * i0 + const and not leqflag:  # handle leq or geq
                return False
    else:
        # print(insider)
        return True
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
point = [1, 2, 3]
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

def runconemembstempl(point):
    # if conemembershipstemplate(point, 2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1), 2 * dim - 1) or
    # conemembershipstemplate(point, dim - 2, dim, -k, (dim - 1) * k / 2, False) or conemembershipstemplate(point, '', dim-1-(1/k), 1, 1) or
    #     conemembershipstemplate(point, (1 / (k / 2 + 1)) + dim - 2, dim + (2 / (k - 2)), (-(2 * k) / (k - 2)) - k,
    #                             (k / 2 + 1) * (dim - 1) + 1, False) or conemembershipstemplate(point,(dim-1 -(1/k)), '', 0, dim*k -1, False) or
    #     conemembershipstemplate(point, (k - 2) * (dim - 1) / (k - 1), 2 * (dim - 1), -k * (dim - 1),
    #                             dim * k - 2 * dim - 1, False) or conemembershipstemplate(point, dim, '', 0, dim*k/2 + k/2) or
    #     conemembershipstemplate(point, (dim * k - 2 * dim + 2) / (k - 2), (dim - 2) + 2 / (k + 2),
    #                             k * (1 - 2 / (k + 2)), dim * k / 2 + k / 2 - dim)
    conemembs =[conemembershipstemplate(point, 2 * dim - 2, (k - 2) * (dim - 1) / (k - 1), k * (dim - 1) / (k - 1), 2 * dim - 1),
                conemembershipstemplate(point, dim - 2, dim, -k, (dim - 1) * k / 2, False),
                conemembershipstemplate(point, '', dim-1-(1/k), 1, 1),
                conemembershipstemplate(point, (1 / (k / 2 + 1)) + dim - 2, dim + (2 / (k - 2)),(-(2 * k) / (k - 2)) - k, (k / 2 + 1) * (dim - 1) + 1, False),
                conemembershipstemplate(point, (dim - 1 - (1 / k)), '', 0, dim * k - 1, False),
                conemembershipstemplate(point, (k - 2) * (dim - 1) / (k - 1), 2 * (dim - 1), -k * (dim - 1), dim * k - 2 * dim - 1, False),
                conemembershipstemplate(point, dim, '', 0, dim * k / 2 + k / 2),
                conemembershipstemplate(point, (dim * k - 2 * dim + 2) / (k - 2), (dim - 2) + 2 / (k + 2), k * (1 - 2 / (k + 2)), dim * k / 2 + k / 2 - dim)
                ]
    for conememb in conemembs:
        if conememb:
            return True
    return False

print(runconemembstempl(point))