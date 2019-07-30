#### ask how to check permut
### TF TEST
[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,2],[0,0,0,2,2],[0,0,1,1,3],[0,0,1,3,3],[0,0,2,2,4],[0,0,2,3,4],[0,0,3,4,4],
[0,0,4,4,4],[0,1,1,1,4],[0,1,1,4,4],[0,1,2,2,5],[0,1,2,4,5],[0,1,3,5,5],[0,1,5,5,5],[0,2,2,3,6],[0,2,2,4,6],
[0,2,4,6,6],[0,2,5,6,6],[0,3,3,3,7],[0,3,3,5,7],[0,3,4,6,7],[0,3,6,6,7],[0,4,4,4,8],[0,4,4,5,8],[0,4,4,7,7],
[0,4,5,6,8],[0,4,6,6,8],[0,4,7,7,7],[0,5,5,7,8],[0,5,7,7,8],[0,6,6,8,8],[0,6,7,8,8],[0,7,8,8,8],[0,8,8,8,8],
[1,1,1,1,5],[1,1,1,5,5],[1,1,2,2,6],[1,1,2,5,6],[1,1,3,6,6],[1,1,6,6,6],[1,2,2,3,7],[1,2,2,5,7],[1,2,4,7,7],
[1,2,6,7,7],[1,3,3,3,8],[1,3,3,6,8],[1,3,4,7,8],[1,3,7,7,8],[1,4,4,4,9],[1,4,4,6,9],[1,4,4,8,8],[1,4,5,7,9],
[1,4,7,7,9],[1,4,8,8,8],[1,5,5,8,9],[1,5,8,8,9],[1,6,6,9,9],[1,6,8,9,9],[1,7,9,9,9],[1,9,9,9,9],[2,2,2,4,8],
[2,2,2,5,8],[2,2,5,8,8],[2,2,6,8,8],[2,3,3,4,9],[2,3,3,6,9],[2,3,5,8,9],[2,3,7,8,9],[,2,4,4,5,10],[,2,4,4,6,10],
[2,4,5,9,9],[,2,4,6,8,10],[,2,4,7,8,10],[2,4,8,9,9],[,2,5,6,9,10],[,2,5,8,9,10],[,2,6,7,10,10],[,2,6,8,10,10],
[,2,8,10,10,10],[,3,3,4,4,10],[,3,3,4,7,10],[,3,3,5,8,10],[,3,3,8,8,10],[,3,4,5,5,11],[,3,4,5,7,11],
[,3,4,6,8,11],[,3,4,8,8,11],[,3,4,9,9,10],[,3,5,5,10,10],[,3,5,9,9,11],[,3,6,6,10,11],[,3,7,7,11,11],
[,4,4,4,4,11],[,4,4,4,8,11],[,4,4,5,9,11],[,4,4,6,6,12],[,4,4,6,7,12],[,4,4,7,8,12],[,4,4,8,8,12],
[,4,4,10,10,10],[,4,5,5,5,12],[,4,5,5,8,12],[,4,5,5,10,11],[,4,5,6,9,12],[,4,6,6,10,12],[,5,5,5,11,11],
[,5,5,6,6,13],[,5,5,6,8,13],[,5,5,7,9,13],[,6,6,6,7,14]


let k=2^{d-1} and s(d)=(k…..k)   d < sum x_i leq \leq dk/2 


1 .   **Vred** = lift  a(d-1) to (0,a(d-1)), (0, s(d-1)-a(d-1)) 
'(0, s(d-1)-a(d-1)) need to be sorted'

lift their decomposition as well

2 .  Vcand = Vred + 1111..d

3 . **Verteices** = some points are known to be vertices for any d 
0….0, 0…01, 1…1d, 0k/2…k/2, k/2-1 … k/2-1 k-1(d<=4), =**Vcand**

4 . **nonVerteices** = 11111x (x<d)is never a vertex 
unless x=d (two decomposition are possible) 

5 . initiate undetermined list **Vund**(Vcand - known determined points

known determined points = _(the origin , 0….01,  0k/2…k/2 )_

6 . for each vertex in Vund, add edges(generators) up to permutations  
until all points in Vund are determined(their neighborhood are verfied)

find edges: from generator first remove their decomposition, 
~~then reduce the remaining edges up to permutation of 
the current undetermined point 
by getting the index fo permutation first~~ 
and choosing the smallest permutation available

###### WHEN MEET THE SAME NEW POINT 1+
cannot tell this is a non-vertex

7 . check whether it's in Verteices, nonVerteices, red, if yes,do 6(continue). 

8 . check sum x_i <= dk/2, if no, remove it. do 6

9 . if no in 8, check cone membership, if yes,move it to nonVerteices, do 6


 _1.1cone of apex 0 and base formed the d vertices 11…11d_
 
 sum x_i \leq 2d-1
 
 sum x_i \neq i0 \leq 2(d-1)x_i0   for i0 =1….d (a1=(2d-2)a2)
 
 
_1.2 cone of apex (k,k,k,....) and base formed the d vertices 11…11d_

 sum x_i \geq 2d-1

 sum x_i \neq i0 \leq ((k-2)(d-1)(x_i0-1))/k-1 +2(d-1)   for i0 =1….d  
 (k-2)(d-1)/(k-1) x_i0 + k(d-1)/(k-1)
 
 _2.1cone of apex 0 and base formed by the d vertices 0k/2….k/2_

sum x_i \leq (d-1)k/2

sum x_i \neq i0 \geq (d-2) x_i0   for i0 =1….d  a1=(d-2)a2  

 _2.2 cone of apex (k,k,k,....) and base formed by the d vertices 0k/2….k/2_

sum x_i \geq (d-1)k/2

sum x_i \neq i0 \geq dx<sub>i0</sub> - k   for i0 =1….d  a1=-da2 

 _3 cone of apex (k,k,k,....) no need for origin and base formed 
 by the d vertices 0000..1_

sum x_i \geq 1

sum x_i \neq i0 \leq (d-1-1/k)x<sub>i0</sub> + 1   for i0 =1….d  a1=-da2 

 _4.1 cone of apex origin no need for (k,k,k,....) and base formed 
 by the d vertices 1,k/2+1…k/2+1_
 
 sum x_i \leq (d-1)k/2 +d  (k/2 +1)(d-1) +1
 
 sum x_i \neq i0 \geq (1/(k/2 +1) + d-2)x<sub>i0</sub>    for i0 =1….d  
 a1=-(1/(k/2 +1) + d-2)a2

 _4.2 cone of apex (k,k,k,....)(only for d > 4) and base formed 
 by the d vertices 1,k/2+1…k/2+1_

sum x_i \geq (d-1)k/2 +d  (k/2 +1)(d-1) +1
 
sum x_i \neq i0 \geq (d+ 2/(k-2) )x<sub>i0</sub> - 2k/(k-2) -k   for i0 =1….d  


_5 cone of apex 0 and base formed by the d vertices k-1 k.... k_

~~sum x_i \leq dk -1~~
 
sum x_i \neq i0 \geq (d-1 -1/k)x<sub>i0</sub>   for i0 =1….d  

_6.1 cone of apex 0  and base formed by the d vertices k-1…k-1,k-d_

sum x_i \leq dk-2d-1 (> dk/2 when d>3, could skip then)
 
sum x_i \neq i0 \geq ((k-2)(d-1)/(k-1) x<sub>i0</sub>   for i0 =1….d  
a1 = -(k-2)(d-1)/(k-1) a2

_6.2 cone of apex s(k) (only for k<4) and base formed 
by the d vertices k-1…k-1,k-d_

sum x_i \geq dk-2d-1
 
sum x_i \neq i0 \geq (2x<sub>i0</sub> - k)(d-1)

2(d-1)x<sub>i0</sub> -k(d-1)
 for i0 =1….d 
a1 = -(k-3)(d-1)/(k-2) a2  -2(d-1)     -k(d-1)


_7 cone of apex 0 (no need for (k,k,k,....)) and base formed 
by the d vertices k/2…k/2,k_

sum x_i \leq  dk/2 
 
sum x_i \neq i0 \leq d x<sub>i0</sub>   for i0 =1….d  
a1 = -2d a2

_8.1 cone of apex 0 and base formed by the d vertices k/2-1 … k/2-1 k-1_

sum x_i \leq  dk/2 
 
sum x_i \neq i0 \leq (dk-2d+2)/(k-2) x<sub>i0</sub>   for i0 =1….d  
a1 = - (dk-2d+2)/(k-2) a2

_8.2 cone of apex s(k) (only for d<=4) and base formed by the d vertices k/2-1 … k/2-1 k-1_

sum x_i \leq  dk/2 
 
sum x_i \neq i0 \leq ((d-2) + 2/(k+2) )x<sub>i0</sub> + k(1 - 2/k+2)   for i0 =1….d  
a1 = - (-d+2 - 2/(k+2)) a2

10 . if no in 9, check decomposation number, if > 1,move it to nonVerteices, 
do 6

**check decomposation by eps**

we decompose the starting vertex (maintain list of dcomposition/eps
of starting vertex), than add edges(e_l， store the points with eps:
5 choose 1 5 choose 2 5 choose 3 5 choose 4 5 choose 5),
We store the index as key,eps value as value in a dict：'012': 1
and check the eps sum from d choose 2 to d choose d

**check decomposation by heuristic**

try to decompose using big family vs small family

Check : 123 is not a vertex by decomposition heuristic 
starting from left and smallest : 
100 + 023 = 100 + 010 + 013 = 100 + 010 + 001 + 011 
starting from left and largest:
111 + 012 and 012 is a vertex so 111 + 010 + 011)
