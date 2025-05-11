import heapq
import time
import random

arr = [random.randint(0, 100000) for _ in range(10000)]

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick(left) + [pivot] + quick(right)

def heap_sort(arr):
    return [heapq.heappop(arr) for _ in range(len(arr))]

arr1 = arr[:]
arr2 = arr[:]

start = time.time()
quick(arr1)
print("Quick Sort Time:", time.time() - start)

start = time.time()
heapq.heapify(arr2)
heap_sort(arr2)
print("Heap Sort Time:", time.time() - start)
