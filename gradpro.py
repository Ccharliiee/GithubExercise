import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

def func():
    dim = 3
    gervec = list(itertools.product(range(2),repeat=dim))
    pts = []
    for r in range(1, len(gervec)):
        comb = itertools.combinations(gervec, r)
        for lists in comb:
            # print('list: ', lists)
            pt = np.array(lists).sum(axis=0, dtype=int)
            pts.append(list(pt))
            # print(pt)

    pts = np.array(pts)

    hull = ConvexHull(pts)
    # f = open("d" + str(dim) + ".txt", "w")
    # f.write(pts[hull.vertices])
    # f.close()

    # pts[hull.vertices].tofile("d" + str(dim) + ".txt", sep=",", format="%s")
    np.savetxt("d" + str(dim) + ".csv", pts[hull.vertices], fmt='%s', delimiter=',', newline='\n')

    print(pts[hull.vertices])

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot(pts[hull.vertices, 0], pts[hull.vertices, 1], pts[hull.vertices, 2], 'ko')
    plt.show()

ax = plt.axes(projection='3d')
pts=[(0,2,2), (2,0,2),(2,2,0)]
ax.view_init(30,220)
ax.scatter(pts[:][0], pts[:][1], pts[:][2])
ax.scatter(0,2,2)
ax.scatter(1,3,3)
ax.scatter(0,0,0)
plt.show()

# import sympy
# from sympy.abc import x,y,z,a
#
# d = sympy.Symbol('d')
#
# print(sympy.linsolve([x+a+4*y+z,x+a+y+4*z, x+a*4+y+z], (a, y, z)))
# sympy.init_printing(sympy.linsolve([1+d*y+z,1+y+d*z], (y, z)))
