
One way to see the algorithm is as a relatively efficient check of all possible 2^{2^d -1} choices for a subsum. Thus, an elementary check should be perform on any candidate:

let e_I denote the unit vector with x_i=1 for i\in I and all other coordinate set to zero.
Let eps_I be the epsilon in the subsum corresponding to e_I  (p =  sum_I eps_I e_I)


you can not have eps_{ij} =1 while eps_{i}=eps_{j}=0  (and neither eps_{ij} =0 while eps_{i}=eps_{j}=1
Thus when go along the algorithm (that is change some eps_I from 0 to 1 as you add the generator e_I) you should check the following (d choose 2) quantities:

for any 1\leq i < j \leq d,  check whether  
2 eps_{ij}  + eps_{i} + eps_{j} = 2
if yes stop right away as this is not a vertex 

(9, **5** choose 2 is not too much)

_**The sum for replacement can have 2 dcomops?
none of a subsum of point is dcompedable
**_

_we decompose the starting vertex (maintain list of dcomposition/eps
 of starting vertex?),
 than add edges(e_l) and check the eps sum from 5 choose 2 to 5 choose 5?_

_~~Or initiate a list of clearly doubly decomposable?~~_  **too hard**

5 choose 2, 10 points, 20 choices

5 choose 3, 10 points, 40 choices

5 choose 4, 5 points, 55 choices



similarly for any 1\leq i < j < k \leq d,  check whether  3 eps_{ijk}  + 2 eps_{ij} + eps_{k} = 3
you also have to consider 3 eps_{ijk}  + 2 eps_{jk} + eps_{i} and 3 eps_{ik}  + 2 eps_{ik} + eps_{j}
as well as 3 eps_{ijk}  + eps_{i}  + eps_{j} + eps_{k}

if any of these quantities is equal to 3, stop right away as this is not a vertex 


If we perform this heuristic from d choose 2 to d choose d, then in 'd choose n'  check, we can only perform the check of its (n-1) 1s, 1-vector decomposition:
If:
n*el{i0, i1, ..., i(n-1)} + n-1*el{ i0, i1, ..., i(n-2)  } + 1*el{ i(n-1)  } != n
n*el{i0, i1, ..., i(n-1)} + n-1*el{ i0, i1, ..., i(n-3), i(n-1) } + 1*el{ i(n-2)  } != n 
......
n*el{i0, i1, ..., i(n-1)} + n-1*el{ i0, i2, ..., i(n-1)  } + 1*el{ i2  } != n
n*el{i0, i1, ..., i(n-1)} + n-1*el{ i1, i2, ..., i(n-1)  } + 1*el{ i0)  } != n 
then: other equations are satisfied because of the check before  'd choose n'  check.

For d=3, in 3 choose 3, only check 3 eps_{ijk}  + 2 eps_{ij} + eps_{k} = 3, 3 eps_{ijk}  + 2 eps_{jk} + eps_{i} !=3, and 3 eps_{ik}  + 2 eps_{ik} + eps_{j} !=3.
 3 eps_{ijk}  + eps_{i}  + eps_{j} + eps_{k} != 3 must be satisfied if  2 eps_{ij}  + eps_{i} + eps_{j} ！= 2，  2 eps_{ik}  + eps_{i} + eps_{k} ！= 2
 2 eps_{ij}  + eps_{j} + eps_{k} != 2 are satisfied.

Proof
Let m be s subset of n.
Case 1. eps{n}=1, eps{m} =1.
Case 2. eps{n}=0, eps{m} =1, 
and length(compliment1)eps{compliment1} +  length(compliment2) eps{compliment2} +... +length(complimentp)eps{complimentp} < length(n) - length(m)  

For d choose n：
n*eps{i0, i1, ..., i(n-1)} + n-1*eps{ i0, i1, ..., i(n-2)  } + 1*eps{ i(n-1)  } != n

n*eps{i0, i1, ..., i(n-1)} + n-1*eps{ i0, i1, ..., i(n-3), i(n-1) } + 1*eps{ i(n-2)  } != n

......

n*eps{i0, i1, ..., i(n-1)} + n-1*eps{ i0, i2, ..., i(n-1)  } + 1*eps{ i2  } != n

n*eps{i0, i1, ..., i(n-1)} + n-1*eps{ i1, i2, ..., i(n-1)  } + 1*eps{ i0)  } != n

then: other equations are satisfied because of the check before  'd choose n'  check.



Proof: 
If n*el{i0, i1, ..., i(n-1)} + n-1*el{ i0, i1, ..., i(n-2)  } + 1*el{ i(n-1)  } > n:

eps{i0, i1, ..., i(n-1)}=1, if eps{ i(n-1) =1

then n*eps{i0, i1, ..., i(n-1)} + any decomposition of n-1*eps{ i0, i1, ..., i(n-2)  } + 1*eps{ i(n-1)  } != n.

if eps{ i(n-1)} =0 then eps{ i0, i1, ..., i(n-2)  } = 1 and any decomposition of it is used partially or entirely since it passes previous check.
then n*eps{i0, i1, ..., i(n-1)} + any decomposition of n-1*eps{ i0, i1, ..., i(n-2)  } + 1*eps{ i(n-1)  } != n.

And it works for all n inequalities.



If n*el{i0, i1, ..., i(n-1)} + n-1*el{ i0, i1, ..., i(n-2)  } + 1*el{ i(n-1)  } < n:

eps{i0, i1, ..., i(n-1)}=0, if eps{ i(n-1) =1
then eps{ i0, i1, ..., i(n-2)  } = 0 and none of its decomposition is used entirely.
then n*eps{i0, i1, ..., i(n-1)} + any decomposition of n-1*eps{ i0, i1, ..., i(n-2)  } + 1*eps{ i(n-1)  } != n.

if eps{ i(n-1) =0, 
then n*eps{i0, i1, ..., i(n-1)} + any decomposition of n-1*eps{ i0, i1, ..., i(n-2)  } + 1*eps{ i(n-1)  } != n.