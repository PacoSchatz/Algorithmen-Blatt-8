import sorting_dll
import numpy as np

arr = np.array(dtype=np.intc, object= [7, 5, 2, 6, 5, 0, 0, 7, 8, 1 ])
test = sorting_dll.RunQuickSort(arr)
print(test)