import ctypes
import numpy as np

lib = ctypes.cdll.LoadLibrary("./sorting.dll");

lib.RunQuickSort.argtypes = [np.ctypeslib.ndpointer(dtype=np.intc, ndim=1,flags="C"), ctypes.c_size_t]
lib.RunQuickSort.restype = ctypes.c_size_t

def RunQuickSort(arr):
    return lib.RunQuickSort(arr, len(arr))

        