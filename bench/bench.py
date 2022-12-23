from math import log2
import sorting_dll
import numpy as np
import sorting
import matplotlib.pyplot as plt
import os

def test(func,*args):
    print("Starting Test: " + str(func))
    def _test(arr):
        arr_sorted = np.sort(arr.copy())
        func(arr, *args)
        assert np.array_equal(arr, arr_sorted)
    
    _test(np.array(dtype=np.intc, object=[1, 1, 1, 1]))
    _test(np.array(dtype=np.intc, object=[1, 2, 3, 4]))
    _test(np.array(dtype=np.intc, object=[4, 3, 2, 1]))
    _test(np.array(dtype=np.intc, object=[1, 2, 1]))
    _test(np.array(dtype=np.intc, object=[1]))
    _test(np.array(dtype=np.intc, object=[]))
    #add more tests here
    print("\t Passed!")

sample_sizes = [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000]
def bench(itcount, func, *args):
    out = []
    for samplesize in sample_sizes:
        avg_time = 0
        for i in range(0, itcount):
            arr = np.random.randint(samplesize, dtype=np.intc, size=samplesize)
            avg_time += func(arr, *args)
        out.append(int(avg_time / itcount))
    print("Finished Benchmarking: " + str(func))
    return out
 
    
test(sorting_dll.RunQuickSort)
test(sorting.selection_sort)
test(sorting.quick_sort, sorting.pivot_half)
test(sorting.quick_sort, sorting.pivot_start)
test(sorting.quick_sort, sorting.pivot_median)

def save_figure(name):
    plt.xlabel("Array-Length")
    plt.ylabel("Time in ns")
    plt.legend(loc='best')
    plt.title(name)
    plt.savefig(name +".png",dpi=300)
    plt.clf()
    os.startfile(name + ".png")

#we reduced the itcount for benchs which take long
print("Starting Benching...")
pys = bench(3,sorting.selection_sort)
pyqh = bench(30,sorting.quick_sort, sorting.pivot_half)
pyqm = bench(3,sorting.quick_sort, sorting.pivot_median)
pyqs = bench(10,sorting.quick_sort, sorting.pivot_start)
plt.plot(sample_sizes, pyqh,"--", label="Python Quicksort (half)")
save_figure("PythonQuickHalf")
plt.plot(sample_sizes, pyqm, "--", label="Python Quicksort (median)") #this is really slow.
save_figure("PythonQuickMedian")
plt.plot(sample_sizes, pyqs, "--", label="Python Quicksort (start)")
save_figure("PythonQuickStart")
plt.plot(sample_sizes, pys,"--", label="Python Selectionsort")
save_figure("PythonSelection")
plt.plot(sample_sizes, pyqh,"--", label="Python Quicksort (half)")
plt.plot(sample_sizes, [n * log2(n) * 700  for n in sample_sizes.copy()],"--", label="Approximation")
save_figure("ApproximationQuickSort")
plt.plot(sample_sizes, pys,"--", label="Python Quicksort (half)")
plt.plot(sample_sizes, [n * n * 110  for n in sample_sizes.copy()],"--", label="Approximation")
save_figure("ApproximationSelectionSort")
plt.plot(sample_sizes, pyqh,"--", label="Python Quicksort (half)")
plt.plot(sample_sizes, pyqm, "--", label="Python Quicksort (median)") #this is really slow.
plt.plot(sample_sizes, pyqs, "--", label="Python Quicksort (start)")
plt.plot(sample_sizes, pys,"--", label="Python Selectionsort")
save_figure("PythonAll")

cppq = bench(30,sorting_dll.RunQuickSort)
plt.plot(sample_sizes, cppq,"--", label="C++ Quicksort")
plt.plot(sample_sizes, bench(30,sorting.native_sort),"--", label="Python Sort")
save_figure("PythonSortVSCpp")

plt.plot(sample_sizes, cppq,"--", label="C++ Quicksort")
plt.plot(sample_sizes, pyqh,"--", label="Python Quicksort")
save_figure("LanguageSpeedComparison")