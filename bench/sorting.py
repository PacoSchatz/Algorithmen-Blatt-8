import time


def selection_sort (arr):
    start_time = time.time_ns()
    
    n = len(arr)
    for i in range(n):        
        p = i
        for j in range(i+1, n):
            if arr[j] < arr[p]:
                p = j
                
        tmp = arr[p]
        arr[p] = arr[i]
        arr[i] = tmp
        
    return time.time_ns() - start_time
                
def pivot_half(arr, start, end):
    return start + int((end -start) / 2)

def pivot_start(arr, start, end):
    return start

def pivot_median(arr, start, end):
    s = sum(arr) / (end - start)
    t = start
    dt = float('inf')
    for i in range(start, end):
        d = abs(arr[i] - s)
        if d < dt:
            dt = d
            t = i
    return t 
          
def quick_sort(arr, pivotfunc):
    start_time = time.time_ns()
    
    interval_stack = [[0,len(arr)]]
    while len(interval_stack) != 0:
        cur = interval_stack.pop(0)
    
        if(cur[0] >= cur[1]):
            continue
        
        p = arr[pivotfunc(arr, cur[0], cur[1])]
        write_idx = cur[0]
        for i in range(write_idx, cur[1]):
            if (arr[i] < p):
                arr[i], arr[write_idx] = arr[write_idx], arr[i]
                write_idx += 1
        
        mid = write_idx
        
        for i in range(write_idx, cur[1]):
            if(arr[i] == p):
                arr[i], arr[write_idx] = arr[write_idx], arr[i]
                write_idx += 1
        
        interval_stack.append([cur[0], mid])
        interval_stack.append([write_idx, cur[1]])
    
    return time.time_ns() - start_time
                

def native_sort(arr):
    start_time = time.time_ns()
    arr.sort()
    return time.time_ns() - start_time
    