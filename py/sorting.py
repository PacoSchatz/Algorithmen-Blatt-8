import random
import time
import statistics

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
                
def pivot_half(arr, start, end):
    return start + int((end -start) / 2)

def pivot_start(arr, start, end):
    return start

def pivot_median(arr, start, end):
    s = sum(arr) / (end - start);
    t = start;
    dt = float('inf')
    for i in range(start, end):
        d = abs(arr[i] - s)
        if d < dt:
            dt = d
            t = i
    return t 
          
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
    

def generate(size):
    return [random.randint(0,size) for _ in range(size)]
        
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))    

def native_sort(arr):
    arr.sort()

def run(itcount, samplesize, sortfunc, *args):
    
    def test(t, a):
        start = time.time_ns()
        sortfunc(a, *args)
        end = time.time_ns();
        print("Test " + str(t) + " took " + str(end - start) + " ns");
        if(not is_sorted(a)):
            print("\tTest not passed")

    test(1, [1])
    test(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200])
    test(3, [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ])
    test(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    
    passed = 0;
    exetime = 0;
    for i in range(itcount):
        arr = generate(samplesize)
        
        #use the legacy sort, copy first otherwise the array already is sorted
        arrsorted = arr.copy()
        arrsorted.sort()
        
        start = time.time_ns()
        sortfunc(arr, *args)
        end = time.time_ns();
        
        exetime += (end - start)
        
        if arrsorted == arr:
            passed += 1

    print("Executed " + sortfunc.__name__ + str(args) +" " + str(itcount) + " times with a Array-Size of " + str(samplesize))
    print("Soring the Array took an avg. of " + str(exetime/samplesize) + "ns")
    print("\tPassed: " + str(passed))
    print("\tFailed: " + str(itcount - passed) + "\n")
        
def main():
    run(10, 10000, selection_sort)
    run(10, 10000, quick_sort, pivot_half)
    run(10, 10000, quick_sort, pivot_median)
    run(10, 10000, quick_sort, pivot_start)
    run(10, 10000, native_sort)
    
if __name__ == "__main__":
    main()