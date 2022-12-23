import sorting_dll
import numpy as np
import sorting
import seaborn as sns   # zum plotten
import matplotlib.pyplot as plt #zum plotten

def test(func,*args):
    print("Starting Test: " + str(func))
    def _test(arr):
        arr_sorted = np.sort(arr.copy())
        func(arr, *args)
        assert np.array_equal(arr, arr_sorted)
    
    _test(np.array(dtype=np.intc, object=[1, 2, 3, 4]))
    #add more tests here
    print("\t Passed!")

sample_sizes = [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000]
def bench(itcount, func, *args):
    out = []
    for samplesize in sample_sizes:
        avg_time = 0;
        for i in range(0, itcount):
            arr = np.random.randint(samplesize, dtype=np.intc, size=samplesize)
            avg_time += func(arr, *args)
        out.append((avg_time / itcount))
    return out
        
    
test(sorting_dll.RunQuickSort)
test(sorting.selection_sort)
test(sorting.quick_sort, sorting.pivot_half)
test(sorting.quick_sort, sorting.pivot_start)
test(sorting.quick_sort, sorting.pivot_median)


sns.lineplot(x = sample_sizes, y = bench(1,sorting.selection_sort), linestyle="dashed", marker="o", label="C++ Quicksort") 
sns.lineplot(x = sample_sizes, y = bench(1,sorting.quick_sort, sorting.pivot_half), linestyle="dashed", marker="o", label="Py Quicksort") 
plt.title("Plot")    
plt.legend(loc="best")                                         
plt.xlabel("Array-Length")                                   
plt.ylabel("ns")
plt.show()