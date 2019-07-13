import numpy as np
import gradpro.six003deluxe as sd

startv = sd.picr(2)
print('sv:', startv)

for i,item in enumerate(startv):
    startv[i] = np.insert(item, 0, 0, axis=i%2)

print('svl:', startv)
