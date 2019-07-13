import numpy as np
import gradpro.six003deluxe as sd

vred= sd.picr(2, 'perv_dcomp_nct')
print('sv:', vred)

for i,item in enumerate(vred):
    vred[i] = np.insert(item, 0, 0, axis=i%2)

print('svl:',vred)
