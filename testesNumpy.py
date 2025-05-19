import numpy as np

array = np.arange(10,21,2)
print(array)

array2 = np.arange(8,60,3)
print(array2)

array3 = np.concatenate([array,array2])
print(np.sort(array3))

