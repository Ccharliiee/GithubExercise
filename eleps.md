
One way to see the algorithm is as a relatively efficient check of all possible 2^{2^d -1} choices for a subsum. Thus, an elementary check should be perform on any candidate:

let e_I denote the unit vector with x_i=1 for i\in I and all other coordinate set to zero.
Let eps_I be the epsilon in the subsum corresponding to e_I  (p =  sum_I eps_I e_I)


you can not have eps_{ij} =1 while eps_{i}=eps_{j}=0  (and neither eps_{ij} =0 while eps_{i}=eps_{j}=1
Thus when go along the algorithm (that is change some eps_I from 0 to 1 as you add the generator e_I) you should check the following (d choose 2) quantities:

for any 1\leq i < j \leq d,  check whether  2 eps_{ij}  + eps_{i} + eps_{j} = 2
if yes stop right away as this is not a vertex 

(9, **5** choose 2 is not too much)

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