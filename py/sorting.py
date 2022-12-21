import random
import time

def selection_sort (arr):
    n = len(arr)
    for i in range(n):        
        p = i
        for j in range(i+1, n):
            if arr[j] < arr[p]:
                p = j
                
        tmp = arr[p];
        arr[p] = arr[i]
        arr[i] = tmp
    return arr;
                
def pivot_half(arr, start, end):
    return start + int((end -start) / 2);  
          
def quick_sort(arr, pivotfunc):
    
    def _quick_sort(start, end):
        if(start >= end):
            return
        
        p = arr[pivotfunc(arr, start, end)]
        cur_idx = start;
        for i in range(start, end):
            if (arr[i] < p):
                arr[i], arr[cur_idx] = arr[cur_idx], arr[i]
                cur_idx += 1
        
        mid_start = cur_idx
        
        for i in range(cur_idx, end):
            if(arr[i] == p):
                arr[i], arr[cur_idx] = arr[cur_idx], arr[i]
                cur_idx += 1
                
        _quick_sort(start, mid_start)
        _quick_sort(cur_idx, end)
               
    _quick_sort(0, len(arr))
    return arr    
    

def generate(size):
    return [random.randint(0,size) for _ in range(size)]
        
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
    

def run(itcount, samplesize, sortfunc, *args):
    passed = 0;
    exetime = 0;
    for i in range(itcount):
        arr = generate(samplesize)
        
        #use the legacy sort, copy first otherwise the array already is sorted
        arrsorted = arr.copy()
        arrsorted.sort()
        
        start = time.time_ns()
        arr = sortfunc(arr, *args)
        end = time.time_ns();
        
        exetime += (end - start)
        
        if arrsorted == arr:
            passed += 1

    print("Executed " + sortfunc.__name__ + " " + str(itcount) + " times with a Array-Size of " + str(samplesize))
    print("Soring the Array took an avg. of " + str(exetime/samplesize) + "ns")
    print("\tPassed: " + str(passed))
    print("\tFailed: " + str(itcount - passed) + "\n")
        
def main():
    run(10, 1000, selection_sort)
    run(10, 1000, quick_sort, pivot_half)
    
if __name__ == "__main__":
    main()