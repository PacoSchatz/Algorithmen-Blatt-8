import random
import time

def selection_sort (arr):
    n = len(arr)
    out = [None] * n
    for i in range(n):        
        p = i
        for j in range(n):
            if arr[p] == None:
                p = j;
                continue
                
            if arr[j] != None and arr[j] < arr[p]:
                p = j
                
        out[i] = arr[p]
        arr[p] = None
        
    return out;
                
def pivot_half(arr):
    return int(len(arr) / 2);  
          
def quick_sort(arr, pivotfunc):
    if len(arr) <= 1:
        return arr
    
    pivot = pivotfunc(arr)
    
    aless = []
    aeq = []
    agreater = []
    
    for i in arr:
        if i < arr[pivot]:
            aless.append(i)
        elif i == arr[pivot]:
            aeq.append(i)
        else:
            agreater.append(i)
        
    return quick_sort(aless, pivotfunc) + aeq + quick_sort(agreater, pivotfunc)
    
    

def gen_array(size):
    return [random.randint(0,size) for _ in range(size)]
        
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
    

def check_sorted(itcount, samplesize, sortfunc, *args):
    passed = 0;
    exetime = 0;
    for i in range(itcount):
        arr = gen_array(samplesize)
        
        #use the legacy sort, copy first otherwise the array already is sorted
        arrsorted = arr.copy()
        arrsorted.sort()
        
        start = time.time_ns()
        arr = sortfunc(arr, *args)
        end = time.time_ns();
        
        exetime += (end - start)
        
        if arrsorted == arr:
            passed += 1

    print("Executed " + sortfunc.__name__ + " " + str(samplesize) + " times with a Array-Size of " + str(samplesize))
    print("Soring the Array took an avg. of " + str((exetime/samplesize)/1000) + " microseconds")
    print("\tPassed: " + str(passed))
    print("\tFailed: " + str(itcount - passed) + "\n")
        
def main():
    check_sorted(10, 1000, selection_sort)
    check_sorted(10, 1000, quick_sort, pivot_half)
    
if __name__ == "__main__":
    main()